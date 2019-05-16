from flask import Flask, request

app = Flask(__name__)

trna = {'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
        'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
        'tta': 'L', 'tca': 'S', 'taa': '*', 'tga': '*',
        'ttg': 'L', 'tcg': 'S', 'tag': '*', 'tgg': 'W',
        'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
        'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
        'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
        'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
        'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
        'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
        'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
        'atg': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R',
        'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
        'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
        'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
        'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'
        }


@app.route('/', methods=['get', 'post'])
@app.route('/demo', methods=['get', 'post'])
def hello_world():
    param_kleur = request.form.get("kleur")
    if param_kleur == None: param_kleur = "green"
    return '''<body bgcolor="{}">Hello World! 
    <form method="post">
    <br>Kleur:<input type="text" name="kleur"><br>
    Username: <input type="text" name="username"><br>
    Wachtwoord: <input type="password" name="wachtwoord"><br>
    <input type="submit" value="klik">
    </form>
    '''.format(param_kleur)


def web():
    seq = request.form.get('dna')
    seq = seq.lower()
    protein = ""
    for i in range(0, len(seq), 3):
        codon = seq[i:i + 3]
        if len(codon) == 3:
            protein += trna[codon]
    return '''<dna = "{}"> DNA seq
    <form method = "post">
    <input type= "text" name= "dna"><br>
    <input type = "submit" value = "klik">
    </form>'''


if __name__ == '__main__':
    app.run()
