var signForm = document.getElementById('login-form');
var successMessage = document.getElementById('success-message');
var errorMessage = document.getElementById('error-message'); 

var username_field = document.getElementById('username');
var password_field = document.getElementById('pass'); 

signForm.addEventListener('submit', (event) => {
  event.preventDefault();
  if (!validateUsername() || !validatePassword()) {
    return;
  } else {
    const usernameValue = document.getElementById('username').value.trim();
    const passwordValue = document.getElementById('pass').value.trim();
    
    const data = new URLSearchParams({
      'username': usernameValue,
      'password': passwordValue,
    });

    fetch('https://brandly.azurewebsites.net/auth/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'accept': 'application/json'
      },
      body: data
    })
    .then(response => {
      if (!response.ok) {
        throw new Error(response.statusText);
      }
      return response.json();
    })
    .then(response => {
      if (response.status === 200) {
        successMessage.classList.add("show-message");
        successMessage.style.display = "block";
        successMessage.innerHTML = 'Successfully login';

        window.location.href = '/dashboard';
       
        //clear the text fields after successfully submitted the login form
        document.getElementById('username').value = '';
        document.getElementById('pass').value = '';
      } else {
        errorMessage.classList.add("show-message");
        errorMessage.style.display = "block";
        errorMessage.innerHTML = response.detail;
    
        //clear the text fields after successfully submitted the login form
        document.getElementById('username').value = usernameValue;
        document.getElementById('pass').value = passwordValue;
      }
    })
    .catch(error => {
      errorMessage.classList.add("show-message");
      errorMessage.style.display = "block";
      errorMessage.innerHTML = error.message;
      console.log(error.message);
  
       //clear the text fields after successfully submitted the form
       document.getElementById('username').value = '';
       document.getElementById('pass').value = '';
    })
    .finally(() => {
      setTimeout(() => {
        successMessage.style.display = "none";
        errorMessage.style.display = "none";
      }, 1500);
    });
  }
});

function validateUsername() {
  const usernameValue = username_field.value.trim();
  if (usernameValue === '') {  
    setError('Username field is required');
    return false;          
  } else if (!isValidEmailPattern(usernameValue)) {
    setError('Provide a valid username address');
    return false;
  }
  return true;
}

function isValidEmailPattern(usernameValue) {
  const emailPattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return emailPattern.test(String(usernameValue).toLowerCase());
}

function validatePassword() {
  const passwordValue = password_field.value.trim();
  if (passwordValue === '') {
    setError('Password field is required');
    return false;
  }
  return true;
}

const setError = (message) => {
  errorMessage.classList.add("show-message");
  errorMessage.style.display = "block";
  errorMessage.innerText = message;
}

// Password toggle function
function myPassword() {
  var passwordHideIcon = document.getElementById("hide-password-icon");
  var passwordShowIcon = document.getElementById("show-password-icon");
  var passwordInput = document.getElementById("pass");

  if (passwordInput.type === "password") {
    passwordInput.type = "text";
    passwordShowIcon.style.display = "none";
    passwordHideIcon.style.display = "block";
  } else { 
    passwordInput.type = "password";
    passwordShowIcon.style.display = "block";
    passwordHideIcon.style.display = "none";
  }
}
