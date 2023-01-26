# Python_scripts-Hydrophobic_domain_finder


Hydrophobic domain finder in Python

This repository contains a simple script in Python language. The Python file (.py) contains the necessary code for detecting hydrophobic domains in a protein. The steps of the script are the following:

1. The user is asked to provide a protein sequence written in one-letter code.

2. For convenience purposes, the user can also insert an ORF (or part of an ORF) that contains translatable codons. If the user inserts an ORF instead of a protein sequence they will be asked to confirm that their sequence is indeed an ORF. Upon confirmation, the ORF will be translated to protein (the provided codons will be translated to aminoacids in one-letter code). If the user doesn't confirm that the inserted sequence is an ORF, they will be asked again to provide a protein sequence written in one-letter code.

3. The protein sequence will be checked for typing errors. If the user has inserted by mistake a letter that doesn't correspond to an aminoacid they will be notified and the program will stop running. 

4. If there are no typing mistakes in the inserted protein, then the sequence of aminoacids will be scanned in order to detect hydrophobic aminoacids. The user will be notified on the position of the hydrophobic aminoacid and the remaining sequence. 

5. The program then detects the first non-hydrophobic aminoacid that appears aftr the detected hydrophobic aminoacid. The presence of a non-hydriphobic aminoacid is considered as the endpoint of the potential hydrophobic domain. 

6. The potential hydropobic domain goes through a step of "quality control" to make sure that its length is appropriate. If there are no more than 3 consective hydrophobic aminoacids then the length is considered too small and the region is not taken as a hydrophobic domain. If there are more than 3 consecutive hydrophobic aminoacids then the region is considered as a hydropbohic domain. The user is notified about the result of the "quality control". 

7. Once the detection of a domain / region is done, the program continues scanning the rest of the sequence in order to detect more potential hydrophobic domains (see steps 4-6). The user is notified once scanning of the whole sequence is done.
