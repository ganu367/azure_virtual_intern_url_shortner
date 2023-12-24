var update_form = document.getElementById('update-url-form');
// update_form.method = "PUT";

var title_field_update = document.getElementById('url-title-update');
var original_url_field_update = document.getElementById('long-url-update');
var url_id = original_url_field_update.dataset.urlId;

update_form.addEventListener('submit', (event) => {
  event.preventDefault();

  const titleUpdateValue = title_field_update.value.trim();
  const original_urlUpdateValue = original_url_field_update.value.trim();

  const data = {
    title: titleUpdateValue,
    key_url: original_urlUpdateValue,
  };
  

  fetch(`https://brandly.azurewebsites.net/api/custom-url/${url_id}`, {
    method: 'PUT',
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
      successMessage.innerHTML = 'updated!';
      successMessage.classList.add("show-message");
      window.location.href = '/dashboard';

    } else {
      errorMessage.innerHTML = response.detail;
      errorMessage.classList.add("show-message");
    }

    //clear the text fields after creating a new link
    title_field_update.value = '';
    original_url_field_update.value = '';

    // Hide messages after 5 seconds
    setTimeout(() => {
      successMessage.style.display = "none";
      errorMessage.style.display = "none";
    }, 5000);
  })
  .catch((error) => {
    const errorMessage = document.getElementById('error-message');
    errorMessage.innerHTML = error.message;
    errorMessage.classList.add("show-message");
  
    //clear the text fields after successfully submitting the form
    title_field_update.value = '';
    original_url_field_update.value = '';

    // Hide messages after 5 seconds
    setTimeout(() => {
      errorMessage.style.display = "none";
    }, 5000);
  });
});

const setError = (message) => {
    errorMessage.classList.add("show-message");
    errorMessage.style.display = "block";
    errorMessage.innerText = message;
  }

 
