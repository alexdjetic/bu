from document import Document

class Livre(Document):
    """
    Classe représentant un livre dans une bibliothèque.

    Attributs :
    ----------
    _title : str
        Le titre du livre.
    _auteur : str
        Le nom de l'auteur du livre.

    Méthodes :
    ---------
    __init__(code: str, salle: str, titre: str, auteur: str, sur_place: bool = False, est_reserver: bool = False,
              online: bool = False):
        Initialise un nouvel objet Livre.

    Exemple d'utilisation :
    >>> livre = Livre("LIV123", "Salle de lecture", "Roman policier", "Jane Doe")
    >>> print(f"Code: {livre._code}")
    Code: LIV123
    >>> print(f"Salle: {livre._salle}")
    Salle: Salle de lecture
    >>> print(f"Titre: {livre._title}")
    Titre: Roman policier
    >>> print(f"Auteur: {livre._auteur}")
    Auteur: Jane Doe
    """

    def __init__(self, code: str, salle: str, titre: str, auteur: str, sur_place: bool = False, est_reserver: bool = False,
                 online: bool = False):
        """
        Initialise un nouvel objet Livre.

        Paramètres :
        ------------
        code : str
            Le code du livre.
        salle : str
            La salle où se trouve le livre.
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
        super().__init__(code, salle, sur_place, est_reserver, online)
        self._title: str = titre
        self._auteur: str = auteur

# Section de test
if __name__ == "__main__":
    # Création d'un livre
    livre = Livre("LIV123", "Salle de lecture", "Roman policier", "Jane Doe")

    # Affichage des informations du livre
    print(f"Code: {livre.code}")
    print(f"Salle: {livre._salle}")
    print(f"Titre: {livre._title}")
    print(f"Auteur: {livre._auteur}")
