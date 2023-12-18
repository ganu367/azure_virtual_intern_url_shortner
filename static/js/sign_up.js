var sign_up_form = document.getElementById('sign-up-form');
var successMessage = document.getElementById('success-message');
var errorMessage = document.getElementById('error-message');

var name_field = document.getElementById('name');
var username_field = document.getElementById('username');
var password_field = document.getElementById('pass');
var confirm_password_field = document.getElementById('re-pass');

sign_up_form.addEventListener('submit', (event) => {
  event.preventDefault();
  if(!validateName()|| !validateUsername()||!validatePassword()||!validateConfrimPassword()){
    return;
  }else{
    const nameValue = name_field.value.trim();
    const usernameValue = username_field.value.trim();
    const passwordValue = password_field.value.trim();
    const conPassValue = confirm_password_field.value.trim();

    const data = {
      name: nameValue,
      username: usernameValue,
      password: passwordValue,
      confirm_password: conPassValue,
    };

    console.log(data)

    fetch('http://127.0.0.1:8000/auth/register', {
      method: 'POST',
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => response.json())
    .then((response) => {
      if (response.status === 200)
      {
        var successMessage = document.getElementById('success-message');
        successMessage.classList.add("show-message");
        successMessage.style.display = "block";
        successMessage.innerHTML = 'Successfully! Your account has been created. Please Login';
    
        //clear the text fields after successfully submited the signup form
        document.getElementById('name').value = '';
        document.getElementById('username').value = '';
        document.getElementById('pass').value = '';
        document.getElementById('re-pass').value = '';

      }else{
        var errorMessage = document.getElementById('error-message');
        errorMessage.classList.add("show-message");
        errorMessage.style.display = "block";
        errorMessage.innerHTML = response.detail;
    
        //clear the text fields after successfully submited the signup form
        document.getElementById('name').value = nameValue;
        document.getElementById('username').value = usernameValue;
        document.getElementById('pass').value = passwordValue;
        document.getElementById('re-pass').value = conPassValue;
      }
    })
    .catch((error) => {
      var errorMessage = document.getElementById('error-message');
      errorMessage.classList.add("show-message");
      errorMessage.style.display = "block";
      errorMessage.innerHTML = error.message;
  
       //clear the text fields after successfully submited the form
       document.getElementById('name').value = '';
       document.getElementById('username').value = '';
       document.getElementById('pass').value = '';
       document.getElementById('re-pass').value = '';
    })
    setTimeout(() => {
      var successMessage = document.getElementById('success-message');
      var errorMessage = document.getElementById('error-message');
      successMessage.style.display = "none";
      errorMessage.style.display = "none";
    }, 5000);
  }
});

const setError = (message) => {
    errorMessage.classList.add("show-message");
    errorMessage.style.display = "block";
    errorMessage.innerText = message;
  }

function validateName(){
  const nameValue = name_field.value.trim();
  if(nameValue==='') {  
    setError('Name fields is required');
    return false;          
    }
  return true;
}
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
//  const confirmPassValue = confirm_password_field.value.trim();
 if(passwordValue===''){
  setError('password fields is required');
  return false;
 }else if(passwordValue.length<6){
    setError('password must be atleast 6 characters');
    return false;
 }
 return true;
}

function validateConfrimPassword(){
 const confirmPassValue = confirm_password_field.value.trim();
 if(confirmPassValue===''){
  setError('confirm password fields is required');
  return false;
 }else if(confirmPassValue.length<6){
    setError('password must be atleast 6 characters');
    return false;
 }
 return true;
}

//pasword toggel function
function createPassowrd() {
  var passHideIcon = document.getElementById("hide-pass-icon");
  var passShowIcon = document.getElementById("show-pass-icon");
  var passInput = document.getElementById("pass");

  if (passInput.type === "password") {
     passInput.type = "text";
     passShowIcon.style.display = "block"
     passHideIcon.style.display = "none"

  } else {
     passInput.type = "password";
     passShowIcon.style.display = "none"
     passHideIcon.style.display = "block"
  }
  }
function rePassowrd() {
    var rePassHideIcon = document.getElementById("hide-re-pass-icon");
    var rePassShowIcon = document.getElementById("show-re-pass-icon");
    var rePassInput = document.getElementById("re-pass");

    if (rePassInput.type === "password") {
        rePassInput.type = "text";
        rePassShowIcon.style.display = "none"
        rePassHideIcon.style.display = "block"

    } else {
        rePassInput.type = "password";
       
        rePassShowIcon.style.display = "block"
        rePassHideIcon.style.display = "none"
    }
  }