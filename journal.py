from document import Document
import datetime


class Journal(Document):
    """
    Classe représentant un journal dans une bibliothèque.

    Attributs :
    ----------
    _titre : str
        Le titre du journal.
    _date : datetime.datetime
        La date de parution du journal.

    Méthodes :
    ---------
    __init__(self, code: str, salle: str, titre: str, date: datetime.datetime):
        Initialise un nouvel objet Journal.

    Exemple d'utilisation :
    >>> import datetime
    >>> date = datetime.datetime.now()
    >>> journal = Journal("JOU123", "Salle de presse", "Journal quotidien", date)
    >>> print(f"Code: {journal._code}")
    Code: JOU123
    >>> print(f"Salle: {journal._salle}")
    Salle: Salle de presse
    >>> print(f"Titre: {journal._titre}")
    Titre: Journal quotidien
    >>> print(f"Date: {journal._date}")
    Date: 2024-09-24 14:30:15.123456
    """

    def __init__(self, code: str, salle: str, titre: str, date: datetime.datetime, sur_place: bool = False, est_reserver: bool = False,
                 online: bool = False):
        """
        Initialise un nouvel objet Journal.

        Paramètres :
        ------------
        code : str
            Le code du journal.
        salle : str
            La salle où se trouve le journal.
        titre : str
            Le titre du journal.
        date : datetime.datetime
            La date de parution du journal.
        sur_place : bool, optionnel
            Indique si le journal est destiné à être consulté sur place (défaut: False).
        est_reserver : bool, optionnel
            Indique si le journal est réservé (défaut: False).
        online : bool, optionnel
            Indique si le journal est disponible en ligne (défaut: False).
        """
        super().__init__(code, salle, sur_place, est_reserver, online)
        self._titre: str = titre
        self._date: datetime.datetime = date

# Section de test
if __name__ == "__main__":
    # Création d'un journal
    date = datetime.datetime.now()
    journal = Journal("JOU123", "Salle de presse", "Journal quotidien", date)

    # Affichage des informations du journal
    print(f"Code: {journal.code}")
    print(f"Salle: {journal._salle}")
    print(f"Titre: {journal._titre}")
    print(f"Date: {journal._date}")
