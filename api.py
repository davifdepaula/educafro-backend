from flask import Flask

app = Flask(__name__)


@app.route('/status')
def status():
    return 'Educafro is alive and well \o/'

if __name__ == "__main__":

    app.run(debug=True)
