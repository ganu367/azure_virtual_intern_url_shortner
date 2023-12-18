const form = document.getElementById('contact-form');
var successMessage = document.getElementById('success-message');
var errorMessage = document.getElementById('error-message');

const name_field = document.getElementById('name-fields');
const mobile_field = document.getElementById('mobile-fields');
const email_field = document.getElementById('email-fields');
const messages_field = document.getElementById('messages-fields');

form.addEventListener('submit', (event) => {
  event.preventDefault();
  if( !validateName()||!validateMobile()||!validateEmail()||!validateMassage()){
    return;
  }else{
    const name = document.getElementById('name-fields').value;
    const mobile = document.getElementById('mobile-fields').value;
    const email = document.getElementById('email-fields').value;
    const messages = document.getElementById('messages-fields').value;

    const data = {name:name, email:email, mobile_number:mobile, messages:messages};
    // console.log(data)
  
    fetch('http://127.0.0.1:8000/api/contact-us', {
      method: 'POST',
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => response.json())
    .then((response) => {
      console.log(response)
      if (response.status === 200){
        var successMessage = document.getElementById('success-message');
        successMessage.classList.add("show-message");
        successMessage.style.display = "block";
        successMessage.innerHTML = response.detail;
    
        //clear the text fields after successfully submited the form
        document.getElementById('name-fields').value = '';
        document.getElementById('mobile-fields').value = '';
        document.getElementById('email-fields').value = '';
        document.getElementById('messages-fields').value = '';
    }})
    .catch((error) => {
      var errorMessage = document.getElementById('error-message');
      errorMessage.classList.add("show-message");
      errorMessage.style.display = "block";
      errorMessage.innerHTML = error.message;
  
       //clear the text fields after successfully submited the form
      document.getElementById('name-fields').value = '';
      document.getElementById('mobile-fields').value = '';
      document.getElementById('email-fields').value = '';
      document.getElementById('messages-fields').value = '';
    })

  setTimeout(() => {
    var successMessage = document.getElementById('success-message');
    var errorMessage = document.getElementById('error-message');
    successMessage.style.display = "none";
    errorMessage.style.display = "none";
  }, 5000);
  }
});


function validateName(){
  const nameValue = name_field.value.trim();
  if(nameValue === '') {
      setError('Name field is required');
      return false;
    }
    return true;
}

function validateMobile(){
  const mobileValue = mobile_field.value.trim();
  if(mobileValue === '') {
      setError('Mobile number field is required');
      return false;
    }else if(!isValidMobileRe(mobileValue)){
      setError('Mobile number must have 10 didgits');
      return false;
    }
    return true;
}

function isValidMobileRe(mobileValue){
  // const mobileValue = mobile_field.value.trim();
  const mobilePattern = /^[0-9]{10}$/;
  return mobilePattern.test(mobileValue);
}

function validateEmail(){
  const emailValue = email_field.value.trim();
  if(emailValue==='') {  
    setError('Email fields is required');
    return false;          
    } else if (!isValidEmailPattern(emailValue)) {
      setError('Provide a valid email address');
      return false;
     }
  return true;
}

function isValidEmailPattern(emailValue){
  // const emailValue = email_field.value.trim();
  const emailPattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return emailPattern.test(String(emailValue).toLowerCase());
}

function validateMassage(){
 const messageValue = messages_field.value.trim();
 if(messageValue===''){
  setError('Messages fields is required');
  return false;
 } 
 return true;
}

const setError = (message) => {
  errorMessage.classList.add("show-message");
  errorMessage.style.display = "block";
  errorMessage.innerText = message;
}