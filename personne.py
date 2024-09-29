class Personne:
    """
    Classe représentant une personne, avec des attributs tels que numéro, permissions, nom, prénom, login et mot de passe.

    Attributs :
    ----------
    num : str
        Le numéro d'identification de la personne.
    perm : str
        Les permissions associées à la personne (ex : admin, user).
    nom : str
        Le nom de famille de la personne.
    prenom : str
        Le prénom de la personne.
    login : str
        Le login utilisé pour l'authentification.
    password : str
        Le mot de passe utilisé pour l'authentification.

    Méthodes :
    ---------
    __init__(num: str, perm: str, nom: str, prenom: str, login: str, password: str):
        Initialise une instance de la classe Personne.

    connection(login: str, password: str) -> bool:
        Vérifie si le login et le mot de passe donnés correspondent à ceux de la personne.
    """

    def __init__(self, num: str, perm: str, nom: str, prenom: str, login: str, password: str):
        """
        Initialise une nouvelle instance de la classe Personne.

        Paramètres :
        ------------
        num : str
            Le numéro d'identification de la personne.
        perm : str
            Les permissions de la personne (ex : admin, user).
        nom : str
            Le nom de famille de la personne.
        prenom : str
            Le prénom de la personne.
        login : str
            Le login utilisé pour l'authentification.
        password : str
            Le mot de passe utilisé pour l'authentification.
        """
        self.num: str = num
        self.perm: str = perm
        self.nom: str = nom
        self.prenom: str = prenom
        self.login: str = login
        self.password: str = password

    def connection(self, login: str, password: str) -> bool:
        """
        Vérifie si les identifiants fournis (login et mot de passe) correspondent à ceux de la personne.

        Paramètres :
        ------------
        login : str
            Le login donné pour la tentative de connexion.
        password : str
            Le mot de passe donné pour la tentative de connexion.

        Retourne :
        ----------
        bool
            True si les identifiants correspondent, False sinon.
        """
        return self.login == login and self.password == password

    def export_dict(self) -> dict:
        return {
            "num": self.num,
            "perm": self.perm,
            "prenom": self.prenom,
            "nom": self.nom,
            "login": self.login
        }


if __name__ == "__main__":
    # Création d'une personne
    personne1 = Personne("001", "admin", "Dupont", "Jean", "jean.dupont", "mdp123")

    # Tentative de connexion réussie
    if personne1.connection("jean.dupont", "mdp123"):
        print("Connexion réussie")
    else:
        print("Échec de la connexion")

    # Tentative de connexion échouée
    if personne1.connection("jean.dupont", "mauvaismdp"):
        print("Connexion réussie")
    else:
        print("Échec de la connexion")
