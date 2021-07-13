
var listePDS
var idPDS

//Recupere la liste des PDS
function listePDS(){
    var url = '../../base_pds/api'
    $.ajax({
      type: "GET",
      url: url,
      dataType: "json",
      success: function(data,status){
      //Récupère la liste des PDS dans une variable globale
        listePDS = data;
        //vide le tableau pour le remplir a nouveau
        var table = document.getElementById('tableContents');
        table.innerHTML = ""
        data.forEach(function(item){
            table.innerHTML += '<tr><td>'+item.id+'</td><td>'+item.prenom+'</td><td>'+item.nom+'</td><td>'+item.mail+'</td><td>'+item.adresse+'</td><td><button type="button" class="btn btn-primary" onclick="editPds('+item.id+');">Editer</button></td></tr>';
        })
      },
      error: function(data){
        console.log(data);
      }
    });
}
listePDS()
setInterval(listePDS, 1000);

//Sauvegarder un nouveau PDS
function savePds(){
    var prenom = document.getElementById('prenom').value
    var nom = document.getElementById('nom').value
    var mail = document.getElementById('mail').value
    var adresse = document.getElementById('adresse').value

    data = {
    "prenom": prenom,
    "nom": nom,
    "mail": mail,
    "adresse": adresse,
    }
    data = JSON.stringify(data);
    var url = '../../base_pds/api/'
    $.ajax({
      type: "POST",
      url: url,
      headers: {
        "Content-Type": "application/json"
      },
      data: data,
      success: function(data,status){
      //Si data (mail unique) est rempli ont affiche le message d'erreur
        if(data.id){
            document.getElementById('prenom').value = ""
            document.getElementById('nom').value = ""
            document.getElementById('mail').value = ""
            document.getElementById('adresse').value = ""
            $('#modalCreationPDS').modal('hide');
        }
        // Sinon on affiche le message d'erreur
        else{
            alert(data);
        }

      },
      error: function(data){
        console.log(data);
      }
    });
}


//Récupère les informations pour éditer un PDS
function editPds(id){
    //Récupère l'ID du PDS editer dans une variable globale
    idPDS = id
    //Affiche la modale et les informations liés au PDS
    $('#modalEditPDS').modal('show');
    listePDS.forEach(function(item){
        if(id == item.id){
            document.getElementById('editPrenom').value = item.prenom
            document.getElementById('editNom').value = item.nom
            document.getElementById('editMail').value = item.mail
            document.getElementById('editAdresse').value = item.adresse
        }
    })
}

//Editer un PDS
function saveEditPds(action){
    if(action == "delete"){
        data = {
        "supprimer": "True"
        }
        data = JSON.stringify(data);
        var url = '../../fiche_profil/'+idPDS+'/'
        $.ajax({
          type: "PATCH",
          url: url,
          timeout: 0,
          headers: {
            "Content-Type": "application/json"
          },
          data: data,
          success: function(data,status){
            $('#modalEditPDS').modal('hide');
          },
          error: function(data){
            console.log(data);
          }
         });
    }
    else{
        //Récupère les informations liés au PDS editer
        var prenom = document.getElementById('editPrenom').value
        var nom = document.getElementById('editNom').value
        var mail = document.getElementById('editMail').value
        var adresse = document.getElementById('editAdresse').value

        data = {
        "prenom": prenom,
        "nom": nom,
        "mail": mail,
        "adresse": adresse
        }
        data = JSON.stringify(data);
        var url = '../../fiche_profil/'+idPDS+'/'
        $.ajax({
          type: "PATCH",
          url: url,
          timeout: 0,
          headers: {
            "Content-Type": "application/json"
          },
          data: data,
          success: function(data,status){
            // Si l'adresse mail n'existe pas
            if(data.id){
                $('#modalEditPDS').modal('hide');
            }
            // Sinon on affiche le message d'erreur
            else{
                alert(data)
            }
          },
          error: function(data){
            console.log(data);
          }

        });
   }
}