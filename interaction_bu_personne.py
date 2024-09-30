from personne import Personne
from bibiotheques import Bibliotheques
from document import Document
from livre import Livre
from journal import Journal
from dvd import Dvd
from statuemprunt import StatuEmprunt
from databaseconnection import connect_to_mysql


def mise_attente_document(bibi: Bibliotheques, document: Document | Livre | Journal | Dvd, employer: Personne, num_usager: str) -> dict:
    """
    Met un document en attente pour un usager si celui-ci est déjà emprunté ou réservé.

    Paramètres:
    -----------
    bibi : Bibliotheques
        L'objet de la bibliothèque où le document est géré.
    document : Document | Livre | Journal | Dvd
        Le document à mettre en attente.
    employer : Personne
        L'employé qui effectue l'action.
    num_usager : str
        Le numéro de l'usager souhaitant réserver le document.

    Retourne:
    ---------
    dict
        Un message indiquant si le document a été mis en attente ou s'il y a eu une erreur.
    """
    if not bibi.check_exist(document):
        return {
            "message": f"Le document dont le code est {document.code} n'existe pas.",
            "status": 500
        }

    if bibi.livres.get(document) == StatuEmprunt.Libre:
        return {
            "message": f"Le document {document.code} est disponible, il n'est pas nécessaire de le mettre en attente.",
            "status": 200
        }

    if employer.perm != "employer":
        bibi.ajout_emprunt(num_usager, document)
        return {
            "message": f"Réservation du document dont la cote est {document.code} par une employer !",
            "status": 200
        }

    # Ajout en attente pour le document
    return bibi.ajout_en_attente_verif(num_usager, document)


def valider_reservation_document(bibi: Bibliotheques, document: Document | Livre | Journal | Dvd, employer: Personne, num_usager: str) -> dict:
    """
    Valide la réservation d'un document pour un usager.

    Paramètres:
    -----------
    bibi : Bibliotheques
        L'objet de la bibliothèque où le document est géré.
    document : Document | Livre | Journal | Dvd
        Le document à réserver.
    employer : Personne
        L'employé qui effectue l'action.
    num_usager : str
        Le numéro de l'usager souhaitant réserver le document.

    Retourne:
    ---------
    dict
        Un message indiquant si la réservation a été validée ou s'il y a eu une erreur.
    """
    if employer.perm != "employer":
        return {
            "message": f"Les permissions ne sont pas assez pour grande pour réaliser la réservation !",
            "status": 500
        }

    if not bibi.check_exist(document):
        return {
            "message": f"Le document dont le code est {document.code} n'existe pas.",
            "status": 500
        }

    if bibi.livres.get(document) != StatuEmprunt.Libre:
        return {
            "message": f"Le document {document.code} est déjà emprunté ou réservé.",
            "status": 500
        }

    # Ajout du document à la bibliothèque
    return bibi.ajout_emprunt(num_usager, document)


def enregistrer_retour_document(bibi: Bibliotheques, document: Document | Livre | Journal | Dvd, employer: Personne, num_usager: str) -> dict:
    """
    Enregistre le retour d'un document emprunté par un usager.

    Paramètres:
    -----------
    bibi : Bibliotheques
        L'objet de la bibliothèque où le document est géré.
    document : Document | Livre | Journal | Dvd
        Le document à retourner.
    employer : Personne
        L'employé qui effectue l'action.
    num_usager : str
        Le numéro de l'usager ayant emprunté le document.

    Retourne:
    ---------
    dict
        Un message indiquant si le retour a été enregistré ou s'il y a eu une erreur.
    """
    if employer.perm != "employer":
        return {
            "message": f"Les permissions ne sont pas assez pour grande pour enregistrer un retour de document !",
            "status": 500
        }

    if not bibi.check_exist(document):
        return {
            "message": f"Le document dont le code est {document.code} n'existe pas.",
            "status": 500
        }

    if bibi.livres.get(document) != StatuEmprunt.Non_Rendue:
        return {
            "message": f"Le document {document.code} n'est pas actuellement emprunté.",
            "status": 500
        }

    return bibi.fin_emprunt(num_usager, document)
