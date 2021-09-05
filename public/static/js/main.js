


console.log("ss")
function login(){
    var username = document.getElementById('loginUsername').value
    var password = document.getElementById('loginPassword').value
    var csrf = document.getElementById('csrf').value

    if(username == '' && password == '' ){
        alert('You must enter both')
    }

    var data = {
        'username' : username,
        'password' : password
 
    }

    fetch('/api/login/' , {
        method : 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrf,
        },
       
        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {
        
        if(response.status == 200){
            window.location.href = '/'
            alert('You have loged in Successfully')

        }
        else{
            alert(response.message)
        }

    })

}


function register(){
    var username = document.getElementById('loginUsername').value
    var password = document.getElementById('loginPassword').value
	var password1 = document.getElementById('loginPassword1').value
    var csrf = document.getElementById('csrf').value

    if(username == '' && password == '' && password1 == ''){
        alert('You must enter Three field')
    }


    var data = {
        'username' : username,
        'password' : password,
		'password1': password1
    }

    fetch('/api/register/' , {
        method : 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrf,
        },
       
        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {
        console.log(response)
        if(response.status == 200){
            alert('You Registerd Successfully ')
          
        }
        else{
            alert(response.message)
        }

    })

}