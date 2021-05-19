from app import app


@app.route("/ivr")
def ivr():
    ################################
    ######## You code here! ########
    ################################

    return "ok!!", 200


if __name__ == "__main__":
    app.run(debug=True)
