from document import Document
from databaseconnection import connect_to_mysql


class Livre(Document):
    """
    Classe représentant un livre dans une bibliothèque.

    Attributs :
    ----------
    _code : str
        Le code unique du livre.
    _salle : str
        La salle où se trouve le livre.
    _title : str
        Le titre du livre.
    _auteur : str
        Le nom de l'auteur du livre.
    _sur_place : bool
        Indique si le livre est destiné à être consulté sur place.
    _est_reserver : bool
        Indique si le livre est réservé.
    _online : bool
        Indique si le livre est disponible en ligne.
    _config_db : dict
        La configuration de la base de données.

    Méthodes :
    ----------
    __init__(self, code: str, salle: str, config_db: dict, titre: str, auteur: str, sur_place: bool = False, est_reserver: bool = False, online: bool = False):
        Initialise un nouvel objet Livre.

    get_all(self) -> list[tuple]:
        Récupère tous les enregistrements de la table Dvd (exemple générique, peut être adapté).

    insert_livre(self) -> bool:
        Insère un nouvel enregistrement de livre dans la base de données.

    update_livre(self) -> bool:
        Met à jour les informations d'un livre dans la base de données.

    delete_livre(self) -> bool:
        Supprime l'enregistrement d'un livre de la base de données.

    Exemple d'utilisation :
    -----------------------
    >>> config = {"host": "127.0.0.1", "user": "root", "password": "wm7ze*2b", "database": "bu"}
    >>> livre = Livre("LIV123", "Salle de lecture", config, "Roman policier", "Jane Doe")
    >>> livre.insert_livre()
    True
    >>> livre.update_livre()
    True
    >>> livre.delete_livre()
    True
    """

    def __init__(self, code: str, salle: str, config_db: dict, titre: str, auteur: str, sur_place: bool = False, est_reserver: bool = False, online: bool = False):
        """
        Initialise un nouvel objet Livre.

        Paramètres :
        ------------
        code : str
            Le code du livre.
        salle : str
            La salle où se trouve le livre.
        config_db : dict
            La configuration de connexion à la base de données.
        titre : str
            Le titre du livre.
        auteur : str
            Le nom de l'auteur du livre.
        sur_place : bool, optionnel
            Indique si le livre est destiné à être consulté sur place (défaut: False).
        est_reserver : bool, optionnel
            Indique si le livre est réservé (défaut: False).
        online : bool, optionnel
            Indique si le livre est disponible en ligne (défaut: False).
        """
        super().__init__(code, salle, config_db, sur_place, est_reserver, online)
        self.title: str = titre
        self.auteur: str = auteur

    @staticmethod
    def get(config_db: dict, code: str) -> list[tuple]:
        """
        Récupère tous les enregistrements de la table Dvd de la base de données.

        Retourne :
        ----------
        list[tuple] : Une liste de tuples contenant les enregistrements de DVD.
        """
        cnx = connect_to_mysql(config_db, attempts=3)

        if cnx and cnx.is_connected():
            with cnx.cursor() as cursor:
                cursor.execute("SELECT * FROM Livre WHERE code = %s", (code,))
                rows = cursor.fetchall()
                return rows

    @staticmethod
    def get_all(config_db: dict) -> list[tuple]:
        cnx = connect_to_mysql(config_db, attempts=3)

        if cnx and cnx.is_connected():
            with cnx.cursor() as cursor:
                cursor.execute("SELECT * FROM Livre")
                rows = cursor.fetchall()
                return rows

    def insert(self) -> bool:
        cnx = connect_to_mysql(self.config_db, attempts=3)

        if cnx and cnx.is_connected():
            try:
                with cnx.cursor() as cursor:
                    query = """
                    INSERT INTO Livre (code, salle, titre, auteur) 
                    VALUES (%s, %s, %s, %s)
                    """
                    params = (self.code, self.salle, self.title, self.auteur)
                    cursor.execute(query, params)
                    cnx.commit()
                    return True
            except Exception as e:
                print(f"An error occurred: {e}")
                return False
        return False

    def update(self) -> bool:
        cnx = connect_to_mysql(self.config_db, attempts=3)

        if cnx and cnx.is_connected():
            with cnx.cursor() as cursor:
                sql = """
                UPDATE Livre
                SET titre = %s, auteur = %s, sur_place = %s, online = %s 
                WHERE code = %s
                """
                params = (self.title, self.auteur, self.sur_place, self.online, self.code)
                cursor.execute(sql, params)
                cnx.commit()
                return True

        return False

    def delete(self) -> bool:
        cnx = connect_to_mysql(self.config_db, attempts=3)

        if cnx and cnx.is_connected():
            with cnx.cursor() as cursor:
                sql = """DELETE FROM Livre WHERE code = %s"""
                params = (self.code,)
                cursor.execute(sql, params)
                cnx.commit()
                return True

        return False

# Section de test
if __name__ == "__main__":
    config = {
        "host": "127.0.0.1",
        "user": "root",
        "password": "wm7ze*2b",
        "database": "bu",
    }

    # Création d'un livre
    livre = Livre("LIV123", "8d-121", config, "Roman policier", "Jane Doe")

    # Test d'insertion dans la base de données
    if livre.insert():
        print("Livre inséré avec succès.")

    # Test de mise à jour dans la base de données
    livre.title = "Nouveau Roman Policier"
    if livre.update():
        print("Livre mis à jour avec succès.")

    # Test de suppression dans la base de données
    if livre.delete():
        print("Livre supprimé avec succès.")
