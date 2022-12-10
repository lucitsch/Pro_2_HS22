from flask import Flask
#Flask Paket wird importieren
from flask import render_template
#um die html Datein zu verwenden
from flask import request

app = Flask(__name__)

#Starseite
@app.route("/")
def start():
    return render_template('index.html')


@app.route("/sommerferien", methods=['GET', 'POST'])
def sommer():
    if request.method == 'POST':
        print(request.form.getlist('mycheckbox'))
        return 'Ihre Auswahl wurde gespeicher. Klicken Sie weiter um Ihre Packliste einzusehen'
    return render_template('sommerkleider.html')

@app.route("/winterferien", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form.getlist('mycheckbox'))
        return 'Ihre Auswahl wurde gespeicher. Klicken Sie weiter um Ihre Packliste einzusehen'
    return render_template('winterkleider.html')


if __name__ == "__main__":
    app.run(debug=True, port=5007)