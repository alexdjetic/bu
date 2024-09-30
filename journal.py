from document import Document
import datetime
from databaseconnection import connect_to_mysql


class Journal(Document):
    """
    Classe représentant un journal dans une bibliothèque.

    Attributs :
    ----------
    _code : str
        Le code unique du journal.
    _salle : str
        La salle où se trouve le journal.
    _titre : str
        Le titre du journal.
    _date : datetime.date
        La date de parution du journal.
    _sur_place : bool
        Indique si le journal est consultable sur place uniquement.
    _est_reserver : bool
        Indique si le journal est réservé.
    _online : bool
        Indique si le journal est disponible en ligne.
    _config_db : dict
        La configuration de la base de données.

    Méthodes :
    ---------
    __init__(self, code: str, salle: str, config_db: dict, titre: str, date_publication: datetime.date, sur_place: bool = False, est_reserver: bool = False, online: bool = False):
        Initialise un nouvel objet Journal.

    insert_livre(self) -> bool:
        Insère un nouvel enregistrement de journal dans la base de données.

    update_livre(self) -> bool:
        Met à jour les informations du journal dans la base de données.

    delete_livre(self) -> bool:
        Supprime l'enregistrement du journal de la base de données.

    Exemple d'utilisation :
    -----------------------
    >>> import datetime
    >>> config = {"host": "127.0.0.1", "user": "root", "password": "wm7ze*2b", "database": "bu"}
    >>> date = datetime.datetime.now().date()
    >>> journal = Journal("JOU123", "Salle de presse", config, "Journal quotidien", date)
    >>> journal.insert_livre()
    True
    >>> journal.update_livre()
    True
    >>> journal.delete_livre()
    True
    """

    def __init__(self, code: str, salle: str, config_db: dict, titre: str, date_publication: datetime.date, sur_place: bool = False, est_reserver: bool = False, online: bool = False):
        """
        Initialise un nouvel objet Journal.

        Paramètres :
        ------------
        code : str
            Le code du journal.
        salle : str
            La salle où se trouve le journal.
        config_db : dict
            La configuration de connexion à la base de données.
        titre : str
            Le titre du journal.
        date_publication : datetime.date
            La date de parution du journal.
        sur_place : bool, optionnel
            Indique si le journal est destiné à être consulté sur place (défaut: False).
        est_reserver : bool, optionnel
            Indique si le journal est réservé (défaut: False).
        online : bool, optionnel
            Indique si le journal est disponible en ligne (défaut: False).
        """
        super().__init__(code, salle, config_db, sur_place, est_reserver, online)
        self.titre: str = titre
        self.date: datetime.date = date_publication

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
                cursor.execute("SELECT * FROM Journal WHERE code = %s", (code,))
                rows = cursor.fetchall()
                return rows

    @staticmethod
    def get_all(config_db: dict) -> list[tuple]:
        cnx = connect_to_mysql(config_db, attempts=3)

        if cnx and cnx.is_connected():
            with cnx.cursor() as cursor:
                cursor.execute("SELECT * FROM Journal")
                rows = cursor.fetchall()
                return rows

    def insert(self) -> bool:
        cnx = connect_to_mysql(self.config_db, attempts=3)

        if cnx and cnx.is_connected():
            try:
                with cnx.cursor() as cursor:
                    query = """
                    INSERT INTO Journal (code, salle, titre, date_publication) 
                    VALUES (%s, %s, %s, %s)
                    """
                    params = (self.code, self.salle, self.titre, self.date)
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
                UPDATE Journal 
                SET titre = %s, date_publication = %s, sur_place = %s, online = %s 
                WHERE code = %s
                """
                params = (self.titre, self.date, self.sur_place, self.online, self.code)
                cursor.execute(sql, params)
                cnx.commit()
                return True

        return False

    def delete(self) -> bool:
        cnx = connect_to_mysql(self.config_db, attempts=3)

        if cnx and cnx.is_connected():
            with cnx.cursor() as cursor:
                sql = """DELETE FROM Journal WHERE code = %s"""
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

    # Création d'un journal
    date = datetime.datetime.now().date()
    journal = Journal("JOU123", "Salle de presse", config, "Journal quotidien", date)

    # Test d'insertion dans la base de données
    if journal.insert():
        print("Journal inséré avec succès.")

    # Test de mise à jour dans la base de données
    journal.titre = "Nouveau Journal Quotidien"
    if journal.update():
        print("Journal mis à jour avec succès.")

    # Test de suppression dans la base de données
    if journal.delete():
        print("Journal supprimé avec succès.")
