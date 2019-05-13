from Bio.Seq import Seq
import re
from Bio.Alphabet import IUPAC

# my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC", IUPAC.unambiguous_dna)
# print( my_seq)
# print(my_seq.complement())
# print(my_seq.reverse_complement())
#
# from Bio.Seq import Seq
# from Bio.Alphabet import IUPAC
# coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
# print(coding_dna)
# template_dna = coding_dna.reverse_complement()
# print(template_dna)
# messenger_rna = coding_dna.transcribe()
# print(messenger_rna)
# print(messenger_rna.translate())
dna = "AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG"
coding_dna = Seq(dna)

lengte = len(coding_dna)

if re.search("[^ATCG]", dna) == None:
    dna = True
    messenger_rna = coding_dna.transcribe()
    eiwit = messenger_rna.translate()
    print("Seq " + coding_dna + " is DNA en " + str(
        lengte) + " base lang." + "reverse complement is: " + messenger_rna + " protein translation is " + eiwit)
elif re.search("[^AUCG]", dna) == None:
    rna = True
    messenger_rna = coding_dna.transcribe()
    eiwit = messenger_rna.translate()
    print("Seq " + coding_dna + " is RNA en " + str(lengte) + " base lang." + " Protein translation is " + eiwit)
elif re.search("[BJOUXZ]", dna) == None:
    eiwit = True
    print("Seq " + coding_dna + " is een Eiwit en " + str(lengte) + " base lang.")
else:
    print("Dis niks")
