import datetime


class Document:
    """
    Classe représentant un document dans une bibliothèque.

    Attributs:
        num_document (int): Le numéro global des documents créés.
        _code (str): Le code unique du document.
        _num (str): Le numéro de l'usager qui a réservé le document. "NA" si non réservé.
        _salle (str): La salle où se trouve le document dans la bibliothèque.
        _est_reserver (bool): Indique si le document est actuellement réservé (True) ou non (False).
        _sur_place (bool): Indique si le document peut être emprunté sur place (True) ou non (False).
        _online (bool): Indique si le document peut être réservé en ligne (True) ou non (False).
        _date_fin_emprunt (datetime.datetime): La date de fin de l'emprunt du document. Initialisée à une valeur par défaut.
        _date_debut_emprunt (datetime.datetime): La date de début de l'emprunt du document. Initialisée à une valeur par défaut.

    Méthodes:
        __init__(self, code: str, salle: str, sur_place: bool = False, est_reserver: bool = False, online: bool = False):
            Initialise un nouvel objet Document avec les informations fournies, y compris le code du document,
            la salle, et les options de réservation (sur place, en ligne).

        reserver_sur_place(self, num_usager: str) -> dict:
            Réserve un document pour un emprunt sur place par un usager spécifique. Renvoie un dictionnaire avec
            un message et un code de statut.

        reserver_online(self, num_usager: str) -> dict:
            Réserve un document pour un emprunt en ligne si le document peut être réservé en ligne. Renvoie un dictionnaire
            avec un message et un code de statut.

        reserver_emprunt(self, num_usager: str) -> dict:
            Réserve un document pour un emprunt, que ce soit sur place ou en ligne, pour un usager spécifique. Renvoie un
            dictionnaire avec un message et un code de statut.

        rendue(self, num_usager: str) -> dict:
            Marque un document comme rendu par un usager spécifique. Renvoie un dictionnaire avec un message et un code
            de statut.
    """

    num_document: int = 0

    def __init__(self, code: str, salle: str, sur_place: bool = False, est_reserver: bool = False,
                 online: bool = False):
        self.code: str = code
        self._num: str = "NA"
        self._salle: str = salle
        self._est_reserver: bool = est_reserver
        self._sur_place: bool = sur_place
        self._online: bool = online
        self._attente: bool = False
        self._date_fin_emprunt: datetime.datetime.date = datetime.datetime(1971, 1, 1).date()
        self._date_debut_emprunt: datetime.datetime.date = datetime.datetime(1971, 1, 1).date()
        Document.num_document += 1

    def reserver_sur_place(self, num_usager: str) -> dict:
        """
        Réserve un document pour être emprunté sur place.

        :param num_usager: Le numéro d'identification de l'usager qui réserve le document.
        :paramtype num_usager: str
        :return: Dictionnaire contenant un message et un statut.
        :rtype: dict
        """
        if self._est_reserver:
            return {"message": f"Le document dont le code est {self.code} est déjà réservé !", "status": 500}

        self._num: str = num_usager
        self._est_reserver: bool = True
        self._attente: bool = False
        self._date_debut_emprunt: datetime.datetime = datetime.datetime.now().date()
        self._date_fin_emprunt: datetime.datetime = datetime.datetime.now() + datetime.timedelta(weeks=2)

        return {"message": f"Le document dont le code est {self.code} est réservé avec succès !", "status": 200}

    def mise_en_attente(self, num_usager: str) -> dict:
        """
        Réserve un document pour être emprunté sur place.

        :param num_usager: Le numéro d'identification de l'usager qui réserve le document.
        :paramtype num_usager: str
        :return: Dictionnaire contenant un message et un statut.
        :rtype: dict
        """
        if self._est_reserver:
            return {"message": f"Le document dont le code est {self.code} est déjà réservé !", "status": 500}

        self._num: str = num_usager
        self._attente: bool = True
        self._date_debut_emprunt: datetime.datetime = datetime.datetime.now().date()
        self._date_fin_emprunt: datetime.datetime = datetime.datetime.now() + datetime.timedelta(weeks=2)

        return {"message": f"Le document dont le code est {self.code} est réservé avec succès !", "status": 200}

    def reserver_online(self, num_usager: str) -> dict:
        """
        Réserve un document pour être emprunté en ligne si cela est autorisé.

        :param num_usager: Le numéro d'identification de l'usager qui réserve le document.
        :paramtype num_usager: str
        :return: Dictionnaire contenant un message et un statut.
        :rtype: dict
        """
        if not self._online and self._est_reserver:
            return {"message": f"Le document dont le code est {self.code} ne peut pas être réservé en ligne !",
                    "status": 500}

        self._num: str = num_usager
        self._est_reserver: bool = True
        self._attente: bool = False
        self._date_debut_emprunt: datetime.datetime = datetime.datetime.now().date()
        self._date_fin_emprunt: datetime.datetime = datetime.datetime.now() + datetime.timedelta(weeks=2)

        return {"message": f"Le document dont le code est {self.code} est réservé en ligne avec succès !",
                "status": 200}

    def reserver_emprunt(self, num_usager: str) -> dict:
        """
        Réserve un document pour être emprunté, soit sur place, soit en ligne.

        :param num_usager: Le numéro d'identification de l'usager qui réserve le document.
        :paramtype num_usager: str
        :return: Dictionnaire contenant un message et un statut.
        :rtype: dict
        """
        if self._est_reserver:
            return {"message": f"Le document dont le code est {self.code} est déjà réservé !", "status": 500}

        self._num: str = num_usager
        self._est_reserver: bool = True
        self._attente: bool = False
        self._date_debut_emprunt: datetime.datetime.date = datetime.datetime.now().date()
        self._date_fin_emprunt: datetime.datetime.date = datetime.datetime.now().date() + datetime.timedelta(weeks=2)

        return {"message": f"Le document dont le code est {self.code} est réservé avec succès !", "status": 200}

    def rendue(self, num_usager: str) -> dict:
        """
        Marque le document comme étant rendu.

        :param num_usager: Le numéro d'identification de l'usager qui rend le document.
        :paramtype num_usager: str
        :return: Dictionnaire contenant un message et un statut.
        :rtype: dict
        """
        if not self._est_reserver:
            return {"message": f"Le document dont le code est {self.code} n'est pas réservé.", "status": 500}

        self._num: str = num_usager
        self._est_reserver: bool = False
        self._date_debut_emprunt: datetime.datetime = datetime.datetime(1971, 1, 1)
        self._date_fin_emprunt: datetime.datetime = datetime.datetime(1971, 1, 1)

        return {"message": f"Le document dont le code est {self.code} a bien été rendu !", "status": 200}


if __name__ == "__main__":
    # Création de deux documents
    doc1 = Document("ABC123", "Salle 1")
    doc2 = Document("DEF456", "Salle 2", online=True)

    # Essai de réserver les documents
    print(doc1.reserver_sur_place("123456"))  # Réservation sur place
    print(doc2.reserver_online("123456"))  # Réservation en ligne

    # Affichage de la liste des documents
    print(Document.num_document)

    # Essai de réserver un document déjà réservé
    print(doc1.reserver_sur_place("123456"))
