from databaseconnection import connect_to_mysql


class Personne:
    """
    Classe représentant une personne, avec des attributs tels que numéro, permissions, nom, prénom, login et mot de passe.

    Attributs :
    -----------
    num : str
        Le numéro d'identification unique de la personne.
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
    config_db : dict
        La configuration pour se connecter à la base de données.

    Méthodes :
    ----------
    __init__(self, num: str, perm: str, nom: str, prenom: str, login: str, password: str, config_db: dict):
        Initialise une instance de la classe Personne.

    get(self, login: str) -> list[tuple]:
        Récupère les informations d'une personne par son login.

    get_all(self) -> list[tuple]:
        Récupère toutes les personnes de la base de données.

    connection(self, login: str, password: str) -> bool:
        Vérifie si le login et le mot de passe donnés correspondent à ceux de la personne.

    create(self) -> bool:
        Crée un nouvel enregistrement de personne dans la base de données.

    update(self) -> bool:
        Met à jour les informations d'une personne dans la base de données.

    delete(self) -> bool:
        Supprime une personne de la base de données.

    Exemple d'utilisation :
    -----------------------
    >>> config = {"host": "127.0.0.1", "user": "root", "password": "passwd", "database": "people_db"}
    >>> personne1 = Personne("001", "admin", "Dupont", "Jean", "jean.dupont", "mdp123", config)
    >>> personne1.create()
    True
    >>> personne1.connection("jean.dupont", "mdp123")
    True
    """

    def __init__(self, num: str, perm: str, nom: str, prenom: str, login: str, password: str, config_db: dict):
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
        config_db : dict
            La configuration de la base de données.
        """
        self.num: str = num
        self.perm: str = perm
        self.nom: str = nom
        self.prenom: str = prenom
        self.login: str = login
        self.password: str = password
        self.config_db: dict = config_db

    def __eq__(self, other):
        return  self.__dict__ == other.__dict__

    @staticmethod
    def get(config_db: dict, login: str) -> list[tuple]:
        """
        Récupère les informations d'une personne à partir de son login.

        Paramètre :
        ------------
        login : str
            Le login de la personne à rechercher.

        Retourne :
        ----------
        list[tuple] : Les informations de la personne correspondante.
        """
        cnx = connect_to_mysql(config_db, attempts=3)

        if cnx and cnx.is_connected():
            with cnx.cursor() as cursor:
                cursor.execute(f"SELECT * FROM Personne WHERE login = '{login}'")
                rows = cursor.fetchall()
                return rows

    @staticmethod
    def get_all(config_db: dict) -> list[tuple]:
        """
        Récupère toutes les personnes de la base de données.

        Retourne :
        ----------
        list[tuple] : Une liste contenant toutes les personnes enregistrées.
        """
        cnx = connect_to_mysql(config_db, attempts=3)

        if cnx and cnx.is_connected():
            with cnx.cursor() as cursor:
                cursor.execute("SELECT * FROM Personne")
                rows = cursor.fetchall()
                return rows

    @staticmethod
    def connection(config_db: dict, login: str, password: str) -> bool:
        """
        Vérifie si les identifiants fournis (login et mot de passe) correspondent à ceux d'une personne.

        Paramètres :
        ------------
        login : str
            Le login fourni pour la tentative de connexion.
        password : str
            Le mot de passe fourni pour la tentative de connexion.

        Retourne :
        ----------
        bool : True si les identifiants correspondent, False sinon.
        """
        datas: list[tuple] = Personne.get_all(config_db)

        for data in datas:
            if data[4] == login and data[5] == password:
                return True

        return False

    def create(self) -> bool:
        """
        Crée un nouvel enregistrement de personne dans la base de données.

        Retourne :
        ----------
        bool : True si la création est réussie, False sinon.
        """
        cnx = connect_to_mysql(self.config_db, attempts=3)

        if cnx and cnx.is_connected():
            try:
                with cnx.cursor() as cursor:
                    query = """
                    INSERT INTO Personne (num, perm, nom, prenom, login, password)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """
                    params = (self.num, self.perm, self.nom, self.prenom, self.login, self.password)
                    cursor.execute(query, params)
                    cnx.commit()
                    return True
            except Exception as e:
                print(f"An error occurred: {e}")
                return False
        return False

    def update(self) -> bool:
        """
        Met à jour les informations de la personne dans la base de données.

        Retourne :
        ----------
        bool : True si la mise à jour est réussie, False sinon.
        """
        cnx = connect_to_mysql(self.config_db, attempts=3)

        if cnx and cnx.is_connected():
            with cnx.cursor() as cursor:
                sql = """
                UPDATE Personne
                SET perm = %s, nom = %s, prenom = %s
                WHERE num = %s
                """
                params = (self.perm, self.nom, self.prenom, self.num)
                cursor.execute(sql, params)
                cnx.commit()
                return True

        return False

    def delete(self) -> bool:
        """
        Supprime l'enregistrement d'une personne de la base de données.

        Retourne :
        ----------
        bool : True si la suppression est réussie, False sinon.
        """
        cnx = connect_to_mysql(self.config_db, attempts=3)

        if cnx and cnx.is_connected():
            with cnx.cursor() as cursor:
                sql = """DELETE FROM Personne WHERE num = %s"""
                params = (self.num,)
                cursor.execute(sql, params)
                cnx.commit()
                return True

        return False
