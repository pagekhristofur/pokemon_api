import csv
from flask import Flask

app = Flask(__name__)

#best practices:
#organizing data into a csv
#hiding data curation into a seperate fucntion
#used correct name spaces
#kept app very simple with refactoring return statements
#provided error handling using optional parameters
#used naming convention for app start, using a well defined hook (globally)
#created a virtual env for encapsulated application
#added an empty line at the name of the file PEP


def parse_pokemon_csv():
    parse_output = {}
    with open('pokemon.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            tokens = row[0].split(",")
            pokemon_id = tokens[0]
            name = tokens[1]
            parse_output[pokemon_id] = name
    return parse_output


pokemon_list = parse_pokemon_csv()


@app.route("/api/v3/pokemon")
def get_all():
    response = ""
    for id, name in pokemon_list.items():
        response += f"{id} | {name}\n"
    return response


@app.route("/api/v3/pokemon/<id>")
def get_id(id):
    if id in pokemon_list:
        return f"{id} | {pokemon_list[id]}\n"
    return "Stick to versions RED BLUE and YELLOW doofus!!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
