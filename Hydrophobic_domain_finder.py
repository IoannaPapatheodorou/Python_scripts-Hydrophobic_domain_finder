
aminoacids = ["G", "P", "A", "V", "L", "I", "M", "C", "F", "Y", "W", "H", "K", "R", "Q", "N", "E", "D", "S", "T"]
hydrophobics = ["A", "V", "L", "I", "P", "F", "C"]
non_hydrophobics = ["G", "M", "Y", "W", "H", "K", "R", "Q", "N", "E", "D", "S", "T"]


#Checking if the retrieved sequence could be indeed a hydrophobic domain
def domain_quality_control(final_sequence):
    for i in range(0, len(final_sequence),1):
        if any(s in final_sequence[i] for s in non_hydrophobics):
            return "None"
        if len(final_sequence) <= 3:
            return "None"
    return "True"


#searching for domains in the protein
def DOMAIN_finder(protein):
    print("Proceeding to search for domains in protein: ", protein)

    domain_seq = hydro_domain_start(protein)
    
    if domain_seq == "None":
        print("Your protein doesn't contain hydrophobic domains. Scanning of DNA sequence is done!")
        return
    
    final_sequence, remaining_sequence = hydro_domain_end(domain_seq)

    if final_sequence == "None":
        print("No hydrophobic residues found. Scanning of DNA sequence is done!")
        return
    
    domain_quality_control(final_sequence)
    
    if domain_quality_control(final_sequence) == "None":
        print("Detected domain is considered too small. Proceeding with the rest of the sequence.\n")
        DOMAIN_finder(remaining_sequence)  
        return 

    if domain_quality_control(final_sequence) == "True":
        print("This is a hydrophobic domain.\n")
        print("Continuing to search for other domains.\n")
    
    DOMAIN_finder(remaining_sequence)  

    if len(remaining_sequence) == 0:
        print("Scanning of DNA sequence is done!")


#finding the start of the hydrophobic domain
def hydro_domain_start(protein):
    for x in range (0, len(protein), 1):
        if any(s in protein[x] for s in hydrophobics):
            domain_seq = protein[x:]
            domain_start = abs(x+1)
            print("Start of domain found at position", domain_start, "of the protein.The remaining sequence is:", domain_seq)
            return domain_seq
    return "None"


#finding the end of the hydrophobic domain
def hydro_domain_end(domain_seq):
    for x in range (0, len(domain_seq), 1):
        if any(s in domain_seq[x] for s in non_hydrophobics):
            final_sequence = domain_seq[:x]
            remaining_sequence = domain_seq[x:]
            domain_end = abs(x)
            print("End of domain found ", domain_end, " residue(s) away from the starting residue of the sequence.")
            print("Possible sequence of the domain is: ", final_sequence, ".\n")
            return final_sequence, remaining_sequence
    return "None", "None"


#translating an ORF to protein
def translator(sequence):
    protein = sequence.replace("ATA", "I").replace("ATC", "I").replace("ATT", "I").replace("ATG", "M").replace("ACA", "T").replace("ACC", "T").replace("ACG", "T").replace("ACT", "T").replace("AAC", "N").replace("AAT", "N").replace("AAA", "K").replace("AAG", "K").replace("AGC", "S").replace("AGT", "S").replace("AGA", "R").replace("AGG", "R").replace('CTA', 'L').replace('CTC', 'L').replace('CTG', 'L').replace('CTT','L').replace('CCA','P').replace('CCC','P').replace('CCG','P').replace('CCT','P').replace('CAC','H').replace('CAT','H').replace('CAA','Q').replace('CAG','Q').replace('CGA','R').replace('CGC','R').replace('CGG','R').replace('CGT','R').replace('GTA','V').replace('GTC','V').replace('GTG','V').replace('GTT','V').replace('GCA','A').replace('GCC','A').replace('GCG','A').replace('GCT','A').replace('GAC','D').replace('GAT','D').replace('GAA','E').replace('GAG','E').replace('GGA','G').replace('GGC','G').replace('GGG','G').replace('GGT','G').replace('TCA','S').replace('TCC','S').replace('TCG','S').replace('TCT','S').replace('TTC','F').replace('TTT','F').replace('TTA','L').replace('TTG','L').replace('TAC','Y').replace('TAT','Y').replace('TAA','_').replace('TAG','_').replace('TGC','C').replace('TGT','C').replace('TGA','_').replace('TGG','W')
 
    print("Your ORF was translated.")
    DOMAIN_finder(protein)
    return protein


#B, J, O, U, X, Z don't correspond to aminiacids but may be inserted in the sequence by typing mistake
def typing_errors(sequence):         
    if "B" in sequence:
        print("Your sequence contains letters that don't correspond to amoniacids. Can't proceed.\n")
    elif "J" in sequence:
        print("Your sequence contains letters that don't correspond to amoniacids. Can't proceed.\n")
    elif "O" in sequence:
        print("Your sequence contains letters that don't correspond to amoniacids. Can't proceed.\n")
    elif "U" in sequence:
        print("Your sequence contains letters that don't correspond to amoniacids. Can't proceed.\n")
    elif "X" in sequence:
        print("Your sequence contains letters that don't correspond to amoniacids. Can't proceed.\n")
    elif "Z" in sequence:
        print("Your sequence contains letters that don't correspond to amoniacids. Can't proceed.\n")
    else:
        print("Your protein contains only letters that correspond to aminoacids.\n")
        protein = sequence
        DOMAIN_finder(protein)


#checking if the inserted sequence is a protein or ORF sequence
def ORF_check(sequence):
    print("Your sequence does not contain methionine. Could your sequence be an ORF?\n")
    answer= input("Please enter 'yes' or 'no'.\n")
    if answer == "yes":
        print("OK, proceeding to translation of your ORF to protein.\n")
        translator(sequence)

    if answer == "no":
        print("If your sequence is not an ORF or protein sequence the process can't continue.Please enter a different sequence.\n")
        main()


#code starts here
def main():
    sequence = input("\nThis is a program detecting different protein domains.\nPlease type your protein sequence below in one-letter code.\n")
    #Methionine (M) is always incorporated in the first place of a protein during translation (although it may be later cleeved in post-translational modifications).
    if "M" in sequence:
        print("\nYour sequence seems like a protein sequence. Proceeding to check for typing errors.\n")
        typing_errors(sequence)
    else:
        ORF_check(sequence)

if __name__ == "__main__":
    main()
