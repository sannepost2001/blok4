from flask import Flask, request
from Bio.Seq import Seq

app = Flask(__name__)


@app.route('/')
def hello_world():
    return ('<!DOCTYPE html>\n'
            '<html lang="en">\n'
            '<head>\n'
            '    <meta charset="UTF-8">\n'
            '    <title>Afvink2</title>\n'
            '</head>\n'
            '<body>\n'
            '<form method = "POST">Seq:\n'
            '    <input type="text" name = "seq">\n'
            '    <input type ="submit" value="Submit"></form>\n'
            '</body>\n'
            '</html>')


@app.route('/', methods=['POST'])
def hello():
    coding_dna = request.form["seq"]
    lengte = len(coding_dna)
    for letter in coding_dna:
        if letter in "atcg":
            messenger_rna = coding_dna.transcribe()
            eiwit = messenger_rna.translate()
            return "Seq " + coding_dna + " is DNA en " + str(lengte) + " base lang." + "reverse complement is: " \
                   + messenger_rna + " protein translation is " + eiwit
        elif letter in "aucg":
            eiwit = my_seq.translate()
            return "Seq " + seq + " is RNA en " + str(lengte) + " base lang." + " Protein translation is " \
                   + eiwit
        elif letter not in "bjouxz":
            return "Seq " + seq + " is een Eiwit en " + str(lengte) + " base lang."
        else:
            return "Dis niks"


coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
print(coding_dna)
template_dna = coding_dna.reverse_complement()
print(template_dna)
messenger_rna = coding_dna.transcribe()
print(messenger_rna)


if __name__ == '__main__':
    app.run()
