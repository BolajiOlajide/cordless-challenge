from flask import Flask, request

app = Flask(__name__)

@app.route('/ivr')
def ivr():
        ################################
        ######## You code here! ########
        ################################

        return "ok!!", 200

if __name__ == "__main__":
    app.run(debug=True)
