from flask import Flask, request, jsonify
from functools import reduce
import statistics

app = Flask(__name__)

# Statistische Berechnungen
@app.route('/statistik', methods=['POST'])
def statistik():
    daten = request.json['zahlen']
    durchschnitt = statistics.mean(daten)
    median = statistics.median(daten)
    standardabweichung = statistics.stdev(daten)
    return jsonify({
        'durchschnitt': durchschnitt,
        'median': median,
        'standardabweichung': standardabweichung
    })

# Textmanipulation
@app.route('/text/umkehren', methods=['POST'])
def text_umkehren():
    text = request.json['text']
    umgekehrter_text = text[::-1]
    return jsonify({'umgekehrter_text': umgekehrter_text})

@app.route('/text/grossbuchstaben', methods=['POST'])
def text_grossbuchstaben():
    text = request.json['text']
    text_in_grossbuchstaben = text.upper()
    return jsonify({'text_in_grossbuchstaben': text_in_grossbuchstaben})

@app.route('/text/ist_palindrom', methods=['POST'])
def ist_palindrom():
    text = request.json['text']
    ist_palindrom = text == text[::-1]
    return jsonify({'ist_palindrom': ist_palindrom})

# Datenfilterung und -aggregation
@app.route('/daten/filtern', methods=['POST'])
def daten_filtern():
    daten = request.json['zahlen']
    schwellwert = request.json['schwellwert']
    gefilterte_daten = list(filter(lambda x: x > schwellwert, daten))
    return jsonify({'gefilterte_daten': gefilterte_daten})

@app.route('/daten/aggregieren', methods=['POST'])
def daten_aggregieren():
    daten = request.json['zahlen']
    aggregierte_daten = reduce(lambda x, y: x + y, daten)
    return jsonify({'aggregierte_daten': aggregierte_daten})

if __name__ == '__main__':
    app.run(debug=True)
