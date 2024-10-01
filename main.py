from flask import Flask, request, redirect, render_template, make_response, session
from bibiotheques import Bibliotheques
from livre import Livre
from journal import Journal
from dvd import Dvd
from personne import Personne

config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "wm7ze*2b",
    "database": "bu",
}

app = Flask(__name__)
app.secret_key = 'wm7ze*2b'
bibio = Bibliotheques(config)


@app.route("/")
def index():
    datas = bibio.get_all_document()
    user_login = session.get('login', None)  # Récupère le login de la session
    user_nom = session.get('nom', None)  # Récupère le nom de la session (si tu veux le passer)

    return render_template("index.html",
                           livres=datas["livre"],
                           journals=datas["journal"],
                           dvds=datas["dvd"],
                           login=user_login,
                           nom=user_nom)


@app.route("/livre/<cote>")
def livre(cote):
    data = Livre.get(config, cote)
    user_login = session.get('login', None)  # Récupère le login de la session
    user_nom = session.get('nom', None)  # Récupère le nom de la session
    return render_template("livre.html",
                           cote=data[0][0],
                           salle=data[0][1],
                           titre=data[0][2],
                           auteur=data[0][3],
                           sur_place=data[0][4],
                           online=data[0][5],
                           debut_emprunt=data[0][6],
                           fin_emprunt=data[0][7],
                           login=user_login,
                           nom=user_nom)


@app.route("/dvd/<cote>")
def dvd(cote):
    data = Dvd.get(config, cote)
    user_login = session.get('login', None)  # Récupère le login de la session
    user_nom = session.get('nom', None)  # Récupère le nom de la session
    return render_template("dvd.html",
                           cote=data[0][0],
                           salle=data[0][1],
                           titre=data[0][2],
                           auteur=data[0][3],
                           sur_place=data[0][4],
                           online=data[0][5],
                           debut_emprunt=data[0][6],
                           fin_emprunt=data[0][7],
                           login=user_login,
                           nom=user_nom)


@app.route("/journal/<cote>")
def journal(cote):
    data = Journal.get(config, cote)
    user_login = session.get('login', None)  # Récupère le login de la session
    user_nom = session.get('nom', None)  # Récupère le nom de la session
    return render_template("journal.html",
                           cote=data[0][0],
                           salle=data[0][1],
                           titre=data[0][2],
                           date_publication=data[0][3],
                           sur_place=data[0][4],
                           online=data[0][5],
                           debut_emprunt=data[0][6],
                           fin_emprunt=data[0][7],
                           login=user_login,
                           nom=user_nom)

@app.route("/auth", methods=["GET"])
def auth_get():
    if 'num' in session:
        return redirect("/")

    return render_template("login.html")


@app.route("/auth", methods=["POST"])
def auth_post():
    login = request.form.get("login")
    password = request.form.get("password")

    if Personne.connection(config, login, password):
        data = Personne.get(config, login)
        session['num'] = str(data[0][0])
        session['login'] = login
        return redirect("/")
    else:
        return redirect("/auth")


@app.route("/user")
def user():
    if 'num' in session:
        user_data = Personne.get(config, session['login'])
        return render_template("user.html",
                               num=user_data[0][0],
                               perm=user_data[0][1],
                               nom=user_data[0][2],
                               prenom=user_data[0][3],
                               login=user_data[0][4],
                               password=user_data[0][5])
    else:
        return redirect("/auth")


@app.route("/logout")
def logout():
    # Supprime les données de session pour déconnecter l'utilisateur
    session.pop('num', None)
    session.pop('login', None)
    return redirect("/auth")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
