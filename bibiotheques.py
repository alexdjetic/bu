from document import Document
from livre import Livre
from dvd import Dvd
from journal import Journal
from statuemprunt import StatuEmprunt

class Bibliotheques:
    """
    Classe représentant une bibliothèque gérant différents types de documents
    tels que des livres, des DVD, et des journaux, ainsi que leur statut
    d'emprunt (libre, emprunté, réservé, non rendu).

    Attributs :
    ----------
    livres : dict
        Dictionnaire associant un document (Livre, Dvd, Journal) à son statut d'emprunt.

    Méthodes :
    ---------
    __init__() -> None:
        Initialise la bibliothèque avec un dictionnaire vide pour stocker les documents.

    check_exist(document: Document | Livre | Dvd | Journal) -> bool:
        Vérifie si un document existe déjà dans la bibliothèque.

    consulter() -> dict:
        Permet de consulter les documents présents dans la bibliothèque.

    ajout_livre(document: Document | Livre | Dvd | Journal = None) -> dict:
        Ajoute un document à la bibliothèque s'il n'existe pas déjà.

    supprimer_livre(document: Document | Livre | Dvd | Journal = None) -> dict:
        Supprime un document de la bibliothèque s'il existe.

    ajout_emprunt(num_usager: str, document: Document | Livre | Dvd | Journal = None) -> dict:
        Ajoute un emprunt pour un document s'il est disponible.

    ajout_non_rendue(document: Document | Livre | Dvd | Journal = None) -> dict:
        Enregistre un document comme non rendu.

    fin_emprunt(num_usager: str, document: Document | Livre | Dvd | Journal = None) -> dict:
        Marque la fin d'un emprunt et met à jour le statut du document.

    ajout_en_attente_verif(document: Document | Livre | Dvd | Journal = None) -> dict:
        Ajoute un document à la bibliothèque en attente de vérification.
    """

    def __init__(self) -> None:
        """
        Initialise la bibliothèque avec un dictionnaire vide pour stocker les documents.
        """
        self.livres: dict[Document | Livre | Dvd | Journal, StatuEmprunt] = {}

    def check_exist(self, document: Document | Livre | Dvd | Journal) -> bool:
        """
        Vérifie si un document existe déjà dans la bibliothèque.

        Paramètres:
        -----------
        document : Document | Livre | Dvd | Journal
            Le document à vérifier.

        Retourne:
        ---------
        bool
            True si le document existe, False sinon.
        """
        return self.livres.get(document, "NA") != "NA"

    def consulter(self) -> dict[Document | Livre | Dvd | Journal, StatuEmprunt]:
        """
        Consulte les documents dans la bibliothèque.

        Retourne:
        ---------
        dict
            Un dictionnaire des documents présents dans la bibliothèque et leurs statuts.
        """
        return self.livres

    def ajout_livre(self, document: Document | Livre | Dvd | Journal = None) -> dict:
        """
        Ajoute un document à la bibliothèque.

        Paramètres:
        -----------
        document : Document | Livre | Dvd | Journal, optionnel
            Le document à ajouter à la bibliothèque.

        Retourne:
        ---------
        dict
            Un message indiquant si le document a été ajouté ou s'il est déjà présent.
        """
        if document and self.check_exist(document):
            return {
                "message": f"Le document dont le code est {document.code} existe déjà dans la bibliothèque.",
                "status": 500
            }

        self.livres.setdefault(document, StatuEmprunt.Libre)

        return {
            "message": f"Le document dont le code est {document.code} a été ajouté à la bibliothèque.",
            "status": 200
        }

    def ajout_en_attente_verif(self, num_usager: str, document: Document | Livre | Dvd | Journal = None) -> dict:
        """
        Ajoute un document à la bibliothèque en attente de vérification.

        Cette méthode permet de signaler qu'un document doit être vérifié avant d'être ajouté
        à la collection de la bibliothèque. Elle vérifie d'abord si le document existe et s'il
        est disponible.

        Paramètres:
        -----------
        document : Document | Livre | Dvd | Journal, optionnel
            Le document à ajouter à la bibliothèque.

        Retourne:
        ---------
        dict
            Un dictionnaire contenant un message indiquant si le document a été ajouté à la liste
            d'attente pour vérification ou s'il est déjà présent dans un statut incompatible.
        """
        if document and not self.check_exist(document):
            return {
                "message": f"Le document dont le code est {document.code} n'existe pas dans la bibliothèque.",
                "status": 500
            }

        if self.livres.get(document) == StatuEmprunt.Libre:
            retour_document: dict = document.mise_en_attente(num_usager)

            if retour_document.get("status") == 200:
                self.livres.setdefault(document, StatuEmprunt.En_Attente)
                return {
                    "message": f"Le document {document.code} a été mis en attente de vérification.",
                    "status": 200
                }


        return {
            "message": f"Le document {document.code} n'a pas été mis en attente de vérification.",
            "status": 500
        }


    def supprimer_livre(self, document: Document | Livre | Dvd | Journal = None) -> dict:
        """
        Supprime un document de la bibliothèque.

        Paramètres:
        -----------
        document : Document | Livre | Dvd | Journal, optionnel
            Le document à supprimer de la bibliothèque.

        Retourne:
        ---------
        dict
            Un message indiquant si le document a été supprimé ou s'il est introuvable.
        """
        if document and not self.check_exist(document):
            return {
                "message": f"Le document dont le code est {document.code} n'existe pas dans la bibliothèque.",
                "status": 500
            }

        self.livres.pop(document)

        return {
            "message": f"Le document dont le code est {document.code} a été supprimé de la bibliothèque.",
            "status": 200
        }

    def ajout_emprunt(self, num_usager: str, document: Document | Livre | Dvd | Journal = None) -> dict:
        """
        Enregistre l'emprunt d'un document par un usager.

        Paramètres:
        -----------
        num_usager : str
            Le numéro de l'usager effectuant l'emprunt.
        document : Document | Livre | Dvd | Journal, optionnel
            Le document à emprunter.

        Retourne:
        ---------
        dict
            Un message indiquant si l'emprunt a été effectué ou s'il a échoué.
        """
        if document and not self.check_exist(document):
            return {
                "message": f"Le document dont le code est {document.code} n'existe pas dans la bibliothèque.",
                "status": 500
            }

        if self.livres.get(document) == StatuEmprunt.Libre:
            retour_document = document.reserver_emprunt(num_usager)
            if retour_document.get("status") == 200:
                self.livres[document] = StatuEmprunt.Non_Rendue
                return {
                    "message": f"Le document {document.code} a été emprunté.",
                    "status": 200
                }
            else:
                return {
                    "message": f"L'emprunt du document {document.code} a échoué.",
                    "status": 500
                }

        return {
            "message": f"Le document {document.code} est déjà réservé ou emprunté !",
            "status": 500
        }

    def ajout_non_rendue(self, document: Document | Livre | Dvd | Journal = None) -> dict:
        """
        Marque un document comme non rendu après un emprunt.

        Paramètres:
        -----------
        document : Document | Livre | Dvd | Journal, optionnel
            Le document à marquer comme non rendu.

        Retourne:
        ---------
        dict
            Un message indiquant si l'opération a réussi ou échoué.
        """
        if document and not self.check_exist(document):
            return {
                "message": f"Le document {document.code} n'existe pas dans la bibliothèque.",
                "status": 500
            }

        if self.livres.get(document) == StatuEmprunt.Reserver:
            return {
                "message": f"Le document {document.code} a été emprunté.",
                "status": 200
            }

        self.livres.setdefault(document, StatuEmprunt.Non_Rendue)

        return {
            "message": f"Le document {document.code} a été marqué comme non rendu.",
            "status": 200
        }

    def fin_emprunt(self, num_usager: str, document: Document | Livre | Dvd | Journal = None) -> dict:
        """
        Marque la fin d'un emprunt et met à jour le statut d'un document.

        Paramètres:
        -----------
        num_usager : str
            Le numéro de l'usager ayant emprunté le document.
        document : Document | Livre | Dvd | Journal, optionnel
            Le document à rendre.

        Retourne:
        ---------
        dict
            Un message indiquant si le document a été rendu ou s'il y a eu une erreur.
        """
        if self.livres.get(document) == StatuEmprunt.Reserver:
            retour_document = document.rendue(num_usager)

            if retour_document.get("status") == 200:
                self.livres[document] = StatuEmprunt.Libre
                return {
                    "message": f"Le document {document.code} a été rendu et est maintenant disponible.",
                    "status": 200
                }
            return {
                "message": f"La tentative de rendre le document {document.code} a échoué.",
                "status": 500
            }

        return {
            "message": f"Le document {document.code} n'a pas été emprunté.",
            "status": 500
        }


if __name__ == "__main__":
    # Création de la bibliothèque
    bibliotheque = Bibliotheques()

    # Ajout d'un document
    livre1 = Livre("22222", "8d-121", "Le Petit Prince", "Saint-Exupéry")
    livre2 = Livre("22534", "8d-121", "Starwars 2", "J.K. Rowling", online=True)
    resultat_ajout = bibliotheque.ajout_livre(livre1)
    resultat_ajout2 = bibliotheque.ajout_livre(livre2)
    print(resultat_ajout)
    print(resultat_ajout2)

    # Ajout d'un emprunt
    resultat_emprunt = bibliotheque.ajout_emprunt("usager123", livre1)
    print(resultat_emprunt)

    # Consultation des documents
    print(bibliotheque.consulter())

    # Fin d'emprunt
    resultat_fin_emprunt = bibliotheque.fin_emprunt("usager123", livre1)
    print(resultat_fin_emprunt)
