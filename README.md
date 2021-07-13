# Test mockup Ennov Event
pds_api

* **CONTEXTE**
  * En utilisant Django & Django Rest Framework, donnez-nous votre avis et la façon dont vous développeriez un petit serveur d'applications qui expose une API REST. Cette API offrira la possibilité de créer, récupérer, mettre à jour et supprimer des objets professionnels de santé dans la base de données. Un objet professionnel de santé doit être composé d'un prénom, d'un nom, d'une adresse email (doit être unique) et d'une adresse postale.
De plus, pour des raisons pratiques, nous ne devons jamais vraiment supprimer un objet de la base de données. Lorsqu’on effectue une opération de « suppression », les objets des professionnels de la santé doivent être « signalés » comme supprimés. <br />
Ensuite, comme s’il a été réellement supprimé de la base de données, il ne devrait pas être possible de récupérer un soin « supprimé » professionnel utilisant l'API.


* **URL**
  * http://127.0.0.1:8000/base_pds/api/
   * `GET` Affiche la liste des PDS
   * `POST` Créer un nouveau PDS
  * http://127.0.0.1:8000/fiche_profil/{id}/
   * `GET` Affiche le détails d'un PDS
   * `PATCH` Met à jour un PDS
  * http://127.0.0.1:8000/schemaApi/
   * `GET` Affiche la documentation API

* **Method:**
  
  <_The request type_>

  `GET` | `POST` | `PATCH`
  
*  **URL Params**

   **Required:**
 
   `id`

* **Data Params**

  {
  "prenom": "string",
  "nom": "string",
  "mail": "string",
  "adresse": "string",
  "supprimer": "string"
}

* **Success Response:**
  
  * **Code:** 200
 
* **Error Response:**


  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{ error : "Adresse mail déjà utilisé" }`
