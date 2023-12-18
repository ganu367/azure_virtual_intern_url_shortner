var signForm = document.getElementById('login-form');
var successMessage = document.getElementById('success-message');
var errorMessage = document.getElementById('error-message');

var username_field = document.getElementById('username');
var password_field = document.getElementById('pass');

signForm.addEventListener('submit', (event) => {
  event.preventDefault();
  if( !validateUsername()||!validatePassword()){
    return;
  }else{
    const usernameValue = document.getElementById('username').value.trim();
    const passwordValue = document.getElementById('pass').value.trim();
    const data = {
      username: document.getElementById('username').value,
      password: document.getElementById('pass').value,
    };

    console.log(data)

    fetch('http://127.0.0.1:8000/auth/login', {
      method: 'POST',
      redirect: 'follow',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'accept': 'application/json'
      },
      body: new URLSearchParams({
        'grant_type': '',
        'username': usernameValue,
        'password': passwordValue,
        'scope': '',
        'client_id': '',
        'client_secret': ''
      })
    })
    .then(response => response.json())
    .then((response) => {
      if (response.status === 200)
      {
        var successMessage = document.getElementById('success-message');
        successMessage.classList.add("show-message");
        successMessage.style.display = "block";
        successMessage.innerHTML = 'Successfully login';

        window.location.href = '/dashboard';
       
        //clear the text fields after successfully submited the login form
        document.getElementById('username').value = '';
        document.getElementById('pass').value = '';
      }else{
        var errorMessage = document.getElementById('error-message');
        errorMessage.classList.add("show-message");
        errorMessage.style.display = "block";
        errorMessage.innerHTML = response.detail;
    
        //clear the text fields after successfully submited the login form
        document.getElementById('username').value = usernameValue;
        document.getElementById('pass').value = passwordValue;
      }
    })
    .catch((error) => {
      var errorMessage = document.getElementById('error-message');
      errorMessage.classList.add("show-message");
      errorMessage.style.display = "block";
      errorMessage.innerHTML = error.message;
      console.log(error.message)
  
       //clear the text fields after successfully submited the form
       document.getElementById('username').value = '';
       document.getElementById('pass').value = '';
    })
    setTimeout(() => {
      var successMessage = document.getElementById('success-message');
      var errorMessage = document.getElementById('error-message');
      successMessage.style.display = "none";
      errorMessage.style.display = "none";
    }, 5000);
  }
});

function validateUsername(){
  const usernameValue = username_field.value.trim();
  if(usernameValue==='') {  
    setError('Username fields is required');
    return false;          
    } else if (!isValidEmailPattern(usernameValue)) {
      setError('Provide a valid username address');
      return false;
     }
  return true;
}

function isValidEmailPattern(usernameValue){
  const emailPattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return emailPattern.test(String(usernameValue).toLowerCase());
}

function validatePassword(){
 const passwordValue = password_field.value.trim();
 if(passwordValue===''){
  setError('password fields is required');
  return false;
 }
 return true;
}

const setError = (message) => {
  errorMessage.classList.add("show-message");
  errorMessage.style.display = "block";
  errorMessage.innerText = message;
}


//pasword toggel function
function myPassowrd() {
    var passwordHideIcon = document.getElementById("hide-password-icon");
    var passwordShowIcon = document.getElementById("show-password-icon");
    var passwordInput = document.getElementById("pass");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        passwordShowIcon.style.display = "none"
        passwordHideIcon.style.display = "block"

    } else {
        passwordInput.type = "password";
        passwordShowIcon.style.display = "block"
        passwordHideIcon.style.display = "none"
    }
  }