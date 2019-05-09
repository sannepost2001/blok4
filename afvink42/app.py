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
    seq = request.form["seq"]
    my_seq = Seq(seq)
    lengte = len(seq)
    for letter in seq:
        if letter in "atcg":
            rna = my_seq.reverse_complement()
            eiwit = my_seq.translate()
            return "Seq " + seq + " is DNA en " + str(lengte) + " base lang." + "reverse complement is: " \
                   + rna + " protein translation is " + eiwit
        elif letter in "aucg":
            eiwit = my_seq.translate()
            return "Seq " + seq + " is RNA en " + str(lengte) + " base lang." + " Protein translation is " \
                   + eiwit
        elif letter not in "bjouxz":
            return "Seq " + seq + " is een Eiwit en " + str(lengte) + " base lang."
        else:
            return "Dis niks"


if __name__ == '__main__':
    app.run()
