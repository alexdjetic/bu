from document import Document
from databaseconnection import connect_to_mysql


class Dvd(Document):
    """
    Classe représentant un DVD dans une bibliothèque.

    Attributs :
    -----------
    _code : str
        Le code unique du DVD.
    _salle : str
        La salle où se trouve le DVD.
    _title : str
        Le titre du DVD.
    _auteur : str
        Le nom de l'auteur du DVD.
    _sur_place : bool
        Indique si le DVD est destiné à être consulté sur place.
    _est_reserver : bool
        Indique si le DVD est réservé.
    _online : bool
        Indique si le DVD est disponible en ligne.
    _config_db : dict
        La configuration de la base de données.

    Méthodes :
    ----------
    __init__(self, code: str, salle: str, config_db: dict, titre: str, auteur: str, sur_place: bool = False, est_reserver: bool = False, online: bool = False):
        Initialise un nouvel objet DVD.

    get_all(self) -> list[tuple]:
        Récupère tous les enregistrements de la table Dvd.

    insert(self) -> bool:
        Insère un nouvel enregistrement de DVD dans la base de données.

    update(self) -> bool:
        Met à jour les informations d'un DVD dans la base de données.

    delete(self) -> bool:
        Supprime l'enregistrement d'un DVD de la base de données.

    Exemple d'utilisation :
    -----------------------
    >>> config = {"host": "127.0.0.1", "user": "root", "password": "wm7ze*2b", "database": "media_db"}
    >>> dvd = Dvd("DVD123", "Salle multimedia", config, "Film d'action", "John Doe")
    >>> dvd.insert()
    True
    >>> dvd.update()
    True
    >>> dvd.delete()
    True
    """

    def __init__(self, code: str, salle: str, config_db: dict, titre: str, auteur: str, sur_place: bool = False, est_reserver: bool = False, online: bool = False):
        """
        Initialise un nouvel objet DVD.

        Paramètres :
        ------------
        code : str
            Le code du DVD.
        salle : str
            La salle où se trouve le DVD.
        config_db : dict
            La configuration de connexion à la base de données.
        titre : str
            Le titre du DVD.
        auteur : str
            Le nom de l'auteur du DVD.
        sur_place : bool, optionnel
            Indique si le DVD est destiné à être consulté sur place (défaut: False).
        est_reserver : bool, optionnel
            Indique si le DVD est réservé (défaut: False).
        online : bool, optionnel
            Indique si le DVD est disponible en ligne (défaut: False).
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
                cursor.execute("SELECT * FROM Dvd WHERE code = %s", (code,))
                rows = cursor.fetchall()
                return rows

    @staticmethod
    def get_all(config_db: dict) -> list[tuple]:
        cnx = connect_to_mysql(config_db, attempts=3)

        if cnx and cnx.is_connected():
            with cnx.cursor() as cursor:
                cursor.execute("SELECT * FROM Dvd")
                rows = cursor.fetchall()
                return rows

    def insert(self) -> bool:
        """
        Insère un nouvel enregistrement de DVD dans la base de données.

        Retourne :
        ----------
        bool : True si l'insertion est réussie, False sinon.
        """
        cnx = connect_to_mysql(self.config_db, attempts=3)

        if cnx and cnx.is_connected():
            try:
                with cnx.cursor() as cursor:
                    query = """
                    INSERT INTO Dvd (code, salle, titre, auteur) 
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
        """
        Met à jour les informations d'un DVD dans la base de données.

        Retourne :
        ----------
        bool : True si la mise à jour est réussie, False sinon.
        """
        cnx = connect_to_mysql(self.config_db, attempts=3)

        if cnx and cnx.is_connected():
            with cnx.cursor() as cursor:
                sql = """
                UPDATE Dvd
                SET titre = %s, auteur = %s, sur_place = %s, online = %s 
                WHERE code = %s
                """
                params = (self.title, self.auteur, self.sur_place, self.online, self.code)
                cursor.execute(sql, params)
                cnx.commit()
                return True

        return False

    def delete(self) -> bool:
        """
        Supprime l'enregistrement d'un DVD de la base de données.

        Retourne :
        ----------
        bool : True si la suppression est réussie, False sinon.
        """
        cnx = connect_to_mysql(self.config_db, attempts=3)

        if cnx and cnx.is_connected():
            with cnx.cursor() as cursor:
                sql = """DELETE FROM Dvd WHERE code = %s"""
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

    # Création d'un DVD
    dvd = Dvd("DVD123", "Salle multimedia", config, "Film d'action", "John Doe")

    # Test d'insertion dans la base de données
    if dvd.insert():
        print("DVD inséré avec succès.")

    # Test de mise à jour dans la base de données
    dvd.title = "Nouveau Film d'action"
    if dvd.update():
        print("DVD mis à jour avec succès.")

    # Test de suppression dans la base de données
    if dvd.delete():
        print("DVD supprimé avec succès.")
