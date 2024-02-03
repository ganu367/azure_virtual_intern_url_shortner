//btn
const shortLinkBtn = document.getElementById('shrt-lnk-btn');
const copyItBtn = document.getElementById('shrt-cpy-btn');


//text
const shortUrlDiv = document.getElementById('cpy-url-div');
const shortUrlText = document.getElementById('shrt-url-text');

shortLinkBtn.addEventListener('click', function() {
    const longUrlInput = document.getElementById('lng-url-text');
    const originalUrl = longUrlInput.value; 
  
    fetch('/api/home/app', {
      method: 'POST',
      body: JSON.stringify({ original_url: originalUrl }),
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => response.json())
    .then((response) => {
      console.log(response)
      if (response.status === 200){
        shortUrlDiv.style.display="block";
        shortUrlText.value = response.url_short;
        
        //input empty
        longUrlInput.value = '';
    }else{
      var errorMessage = document.getElementById('error-message');
        errorMessage.classList.add("show-message");
        errorMessage.style.display = "block";
        errorMessage.innerHTML = response.detail;
    }
    })
    .catch((error) => {
        var errorMessage = document.getElementById('error-message');
        errorMessage.classList.add("show-message");
        errorMessage.style.display = "block";
        errorMessage.innerHTML = error.message;
      })
    setTimeout(() => {
      var errorMessage = document.getElementById('error-message');
      errorMessage.style.display = "none";
    }, 1500);  
});


copyItBtn.addEventListener('click', function() {
  const shortUrlText = document.getElementById('shrt-url-text');
  shortUrlText.select();
  document.execCommand("copy");
  copyItBtn.innerText = "copied";
  copyItBtn.classList.add("green-copied");
  setTimeout(() => {
    copyItBtn.innerHTML = '<i class="bx bxs-copy-alt"></i>';
    copyItBtn.classList.remove("green-copied");
  }, 1500); 
});


// azure bot implement
document.addEventListener('DOMContentLoaded', function () {
  const chatButton = document.getElementById('chatButton');
  const webchatContainer = document.getElementById('webchatContainer');
  const closeButton = document.getElementById('closeButton');

  chatButton.addEventListener('click', async function () {
      
      const res = await fetch('https://directline.botframework.com/v3/directline/tokens/generate', {
          method: 'POST',
          headers: { 'Authorization': 'Bearer JS8B8oqLjfw.GY2L8zoJTmwammep5oPep9D9OOiIaRlMY35IhSlG1pI' }
      });
      const { token } = await res.json();

      const styleSet = window.WebChat.createStyleSet({
         
      });

      window.WebChat.renderWebChat(
          {
              directLine: window.WebChat.createDirectLine({ token }),
              userID: 'WebChat_UserId',  
              username: 'Web Chat User',  
              locale: 'en-US',
              styleSet
          },
          document.getElementById('webchatContainer')
      );

      
      webchatContainer.style.display = 'block';
      closeButton.style.display = 'block';
      chatButton.style.display = 'none';
  });

  closeButton.addEventListener('click', function () {
    webchatContainer.style.display = 'none';
    closeButton.style.display = 'none';
    chatButton.style.display = 'block';
});
});

// faq
const faqHeaders = document.querySelectorAll(".content-container .faq-header");

faqHeaders.forEach((header, i) => {
  header.addEventListener("click", () => {
    header.nextElementSibling.classList.toggle("active");

    const open = header.querySelector(".open");
    const close = header.querySelector(".close");
    if (header.nextElementSibling.classList.contains("active")) {
      open.classList.remove("active");
      close.classList.add("active");
      
    } else {
      open.classList.add("active");
      close.classList.remove("active");

    }
  });
});
