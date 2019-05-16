from flask import Flask, request
from Bio.Seq import Seq
import re

app = Flask(__name__)


@app.route('/')
def hello_world():
    return ('<!DOCTYPE html>\n'
            '<html lang="en">\n'
            '<head>\n'
            '    <meta charset="UTF-8">\n'
            '    <title>Afvink4</title>\n'
            '</head>\n'
            '<body>\n'
            '<form method = "POST">Seq:\n'
            '    <input type="text" name = "seq">\n'
            '    <input type ="submit" value="Submit"></form>\n'
            '</body>\n'
            '</html>')


@app.route('/', methods=['POST'])
def hello():
    teruggeven = ""
    dna = request.form["seq"]
    coding_dna = Seq(dna)
    lengte = len(coding_dna)
    if not re.search("[^ATCG]", dna):
        messenger_rna = coding_dna.transcribe()
        eiwit = messenger_rna.translate()
        teruggeven = "Seq " + coding_dna + " is DNA en " + str(
            lengte) + " base lang." + "reverse complement is: " + messenger_rna + " protein translation is " + eiwit
    elif not re.search("[^AUCG]", dna):
        messenger_rna = coding_dna.transcribe()
        eiwit = messenger_rna.translate()
        teruggeven = "Seq " + coding_dna + " is RNA en " + str(
            lengte) + " base lang." + " Protein translation is " + eiwit
    elif re.search("[BJOUXZ]", dna) == None:
        teruggeven = "Seq " + coding_dna + " is een Eiwit en " + str(lengte) + " base lang."
    else:
        teruggeven = "Dis niks, geif maah un echte sekwensie"

    return ('<!DOCTYPE html>\n'
            '<html lang="en">\n'
            '<head>\n'
            '    <meta charset="UTF-8">\n'
            '    <title>Afvink4</title>\n'
            '</head>\n'
            '<body>\n'
            '<form method = "POST">Seq:\n'
            '    <input type="text" name = "seq">\n'
            '    <input type ="submit" value="Submit"></form>\n'
            '</body>\n'
            '</html>')
if __name__ == '__main__':
    app.run()
