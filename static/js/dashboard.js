let sidebar = document.querySelector(".sidebar");
let sidebarBtn = document.querySelector(".sidebarBtn");
sidebarBtn.onclick = function() {
  sidebar.classList.toggle("active");
  if(sidebar.classList.contains("active")){
  sidebarBtn.classList.replace("bx-menu" ,"bx-menu-alt-right");
}else
  sidebarBtn.classList.replace("bx-menu-alt-right", "bx-menu");
}

// create-link
var create_form = document.getElementById('create-form-api');
var successMessage = document.getElementById('success-message');
var errorMessage = document.getElementById('error-message');

var title_field = document.getElementById('url-title');
var original_url_field = document.getElementById('long-url');

create_form.addEventListener('submit', (event) => {
  event.preventDefault();

  const titleValue = title_field.value.trim();
  const original_urlValue = original_url_field.value.trim();

  const data = {
    title: titleValue,
    original_url: original_urlValue,
  };
  console.log(data)
  fetch('https://brandly.azurewebsites.net/api/create-url-short', {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(response => response.json())
  .then((response) => {
    const successMessage = document.getElementById('success-message');
    const errorMessage = document.getElementById('error-message');

    if (response.status === 200) {
      successMessage.innerHTML = 'Created!';
      successMessage.classList.add("show-message");
      window.location.href = '/dashboard';

    } else {
      errorMessage.innerHTML = response.detail;
      errorMessage.classList.add("show-message");
    }

    //clear the text fields after creating a new link
    title_field.value = '';
    long_url_field.value = '';

    // Hide messages after 5 seconds
    setTimeout(() => {
      successMessage.style.display = "none";
      errorMessage.style.display = "none";
    }, 1500);
  })
  .catch((error) => {
    const errorMessage = document.getElementById('error-message');
    errorMessage.innerHTML = error.message;
    errorMessage.classList.add("show-message");
  
    //clear the text fields after successfully submitting the form
    title_field.value = '';
    long_url_field.value = '';

    // Hide messages after 5 seconds
    setTimeout(() => {
      errorMessage.style.display = "none";
    }, 1500);
  });
});


const setError = (message) => {
    errorMessage.classList.add("show-message");
    errorMessage.style.display = "block";
    errorMessage.innerText = message;
  }

 

