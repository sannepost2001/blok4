app = Flask(__name__)


@app.route('/')
@app.route('/<path:filename>', methods=['GET', 'POST'])
def pagina(filename):
    if filename == "bacterie.html":
        # """ Als er op zoeken op bacterie naam wordt gebruikt dan wordt de bacterie.html pagina aangeroepen.
        # deze pagina moet nog aangevuld worden met de data die je kruigt als je filterd op het zoekword
        # """

        searchword = ""
        zoekwoord = ""
        teruggeven = ""
        giveback = ""
        if request.method == 'POST':
            conn = mysql.connector.connect(host="hannl-hlo-bioinformatica-mysqlsrv.mysql.database.azure.com",
                                           user="kxxxf@hannl-hlo-bioinformatica-mysqlsrv", db="kxxxf",
                                           password="ConnectionPWD")
            cursor = conn.cursor()

            try:
                zoekwoord = request.form["zoekwoord"]
            except KeyError:
                zoekwoord = ""

            try:
                searchword = request.form["searchword"]
            except KeyError:
                searchword = ""

            if zoekwoord != "":
                # Query die zoekt op het zoekwoord
                cursor.execute("""select blast.name, blast.accessioncode, functionality.function from blast join functionint
                                  on blast.id = functionint.BLAST_id join functionality on functionint.functionality_id = 
                                  functionality.id where blast.name like '%" + zoekwoord + "%'""")
                records = cursor.fetchall()  # lijst met al de namen die het zoekwoord in de naam hebben

                teruggeven = ("<p2>Gevonden data van het zoeken op protiën naam:</p2><br>\n"
                              + "<table id=\"myTable\" style=\"width:777px; height: 400px;\">"
                              + "   <tr>\n"
                              + "   <th onclick=\"sortTable(0)\">Naam</th>\n"
                              + "   <th onclick=\"sortTable(1)\">Accessiecode:</th>\n"
                              + "   <th onclick=\"sortTable(2)\">Functie:</th>\n"
                              + "   </tr>")
                for rows in records:
                    for row in rows:
                        teruggeven = teruggeven + "<tr>"
                        teruggeven = teruggeven + "<td>" + (row[0]) + "</td>"
                        teruggeven = teruggeven + "<td>" + (row[1]) + "</td>"
                        teruggeven = teruggeven + "<td>" + (row[2]) + "</td>"
                        teruggeven = teruggeven + "</tr>"
                teruggeven = teruggeven + "</table>"
            if searchword != "":
                cursor.execute("""select taxonomy.name, blast.name from taxonomy join blast on blast.TAXONOMY_id = 
                                              taxonomy.id join taxonomy b on b.TAXONOMY_id = taxonomy.id where taxonomy.name like 
                                              '%" + searchword + "%'""")
                data = cursor.fetchall()
                cursor.close()
                conn.close()
                # maakt een tabel van de gevonden data
                giveback = ("<p2>Gevonden data van het zoeken op taxonomy:</p2><br>\n"
                            + "<table id=\"myTable\" style=\"width:777px; height: 400px;\">"
                            + "   <tr>\n"
                            + "   <th onclick=\"sortTable(0)\">Naam</th>\n"
                            + "   <th onclick=\"sortTable(1)\">Taxonomy</th>\n"
                            + "   </tr>")

                for a in data:
                    for i in a:
                        giveback = giveback + "<tr>"
                        giveback = giveback + "<td>" + (i[0]) + "</td>"
                        giveback = giveback + "<td>" + (i[1, 2]) + "</td>"
                        giveback = giveback + "</tr>"

                giveback = giveback + "</table>"

            return render_template("bacterie.html", teruggeven=teruggeven, zoekwoord=zoekwoord, giveback=giveback,
                                   searchword=searchword)

    elif filename == "tabel.html":
        """"""
        # try:
        teruggeven = ""
        sql = ""
        naam = ""
        coverage = ""
        score = ""
        identity = ""
        evalue = ""
        if request.method == 'POST':
            conn = mysql.connector.connect(host="hannl-hlo-bioinformatica-mysqlsrv.mysql.database.azure.com",
                                           user="kxxxf@hannl-hlo-bioinformatica-mysqlsrv", db="kxxxf",
                                           password="ConnectionPWD")
            cursor = conn.cursor()
            naam = request.form["naam"]
            coverage = request.form["coverage"]
            score = request.form["score"]
            identity = request.form["identity"]
            evalue = request.form["evalue"]
            if naam != "":
                #
                sql = sql + " and blast.name like '%" + naam + "%'"
            if coverage != "":
                #
                sql = sql + " and querycoverage > " + coverage
            if score != "":
                #
                sql = sql + " and sequence.score > " + score
            if identity != "":
                #
                sql = sql + " and percidentity > " + identity
            if evalue != "":
                #
                sql = sql + " and evalue < " + evalue + "%'"
            #
            cursor.execute("select blast.name, evalue, bits, querycoverage, percidentity from blast where 1=1" + sql)
            records = cursor.fetchall()  # lijst met al de namen die het zoekwoord in de naam hebben
            cursor.close()
            conn.close()
            teruggeven = ("<table id=\"myTable\" style=\"width:777px; height: 400px;\">"
                          + "    <tr>\n"
                          + "    <th onclick=\"sortTable(0)\">Naam</th>\n"
                          + "    <th onclick=\"sortTable(1)\">E-value:</th>\n"
                          + "    <th onclick=\"sortTable(2)\">(Bit)score:</th>\n"
                          + "    <th onclick=\"sortTable(3)\">Coverage:</th>\n"
                          + "    <th onclick=\"sortTable(4)\">%identity:</th>\n"
                          + "    </tr>")
            for row in records:
                teruggeven = teruggeven + "<tr>"
                teruggeven = teruggeven + "<td>" + str((row[0])) + "</td>"
                teruggeven = teruggeven + "<td>" + str((row[1])) + "</td>"
                teruggeven = teruggeven + "<td>" + str((row[2])) + "</td>"
                teruggeven = teruggeven + "<td>" + str((row[3])) + "</td>"
                teruggeven = teruggeven + "<td>" + str((row[4])) + "</td>"
                teruggeven = teruggeven + "</tr>"
            teruggeven = teruggeven + "</table>"
        return (render_template("tabel.html", teruggeven=teruggeven, naam=naam, identity=identity, score=score,
                                evalue=evalue, coverage=coverage))
