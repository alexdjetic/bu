from document import Document


class Dvd(Document):
    """
    Classe représentant un DVD dans une bibliothèque.

    Attributs :
    ----------
    _title : str
        Le titre du DVD.
    _auteur : str
        Le nom de l'auteur du DVD.

    Méthodes :
    ---------
    __init__(self, code: str, salle: str, titre: str, auteur: str):
        Initialise un nouvel objet DVD.

    Exemple d'utilisation :
    >>> dvd = Dvd("DVD123", "Salle multimedia", "Film d'action", "John Doe")
    >>> print(f"Code: {dvd._code}")
    Code: DVD123
    >>> print(f"Salle: {dvd._salle}")
    Salle: Salle multimedia
    >>> print(f"Titre: {dvd._title}")
    Titre: Film d'action
    >>> print(f"Auteur: {dvd._auteur}")
    Auteur: John Doe
    """

    def __init__(self, code: str, salle: str, titre: str, auteur: str, sur_place: bool = False, est_reserver: bool = False,
                 online: bool = False):
        """
        Initialise un nouvel objet DVD.

        Paramètres :
        ------------
        code : str
            Le code du DVD.
        salle : str
            La salle où se trouve le DVD.
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
        super().__init__(code, salle, sur_place, est_reserver, online)
        self._title: str = titre
        self._auteur: str = auteur

# Section de test
if __name__ == "__main__":
    # Création d'un DVD
    dvd = Dvd("DVD123", "Salle multimedia", "Film d'action", "John Doe")

    # Affichage des informations du DVD
    print(f"Code: {dvd.code}")
    print(f"Salle: {dvd._salle}")
    print(f"Titre: {dvd._title}")
    print(f"Auteur: {dvd._auteur}")
