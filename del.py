# if (db.query(models.User).count() == 0):
# if (request.password == "Pass@1234"):

#     admin_user = models.User(username=request.username, created_by=request.username,
#                              password=hashing.Hash.bcrypt(request.password), is_admin=True)
#     db.add(admin_user)
#     db.commit()
#     db.refresh(admin_user)
#     access_token = tokens.create_access_token(data={"user": {
#         "username": request.username,"isAdmin": True}})

#     return {"access_token": access_token, "token_type": "bearer"}

# else:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                         detail="Incorrect Passwords")

# else:


# delete html code goes below
# <section class="footer">
#       <div class="col footer-about">
#         <a href="" class="brand-lg"> brands<span>U</span>rl </a>
#         <p>
#           BrandURL is a short URL service that offers custom domain branding,
#           password protection, link expiration, and tracking features. BrandURL
#           provides detailed analytics to track clicks, location, and device
#           type.
#         </p>
#       </div>

#       <div class="col footer-company">
#         <h4>Company</h4>
#         <ul>
#           <li>
#             <a href="http://" target="_blank" rel="noopener noreferrer">
#               Teams
#             </a>
#           </li>
#           <li>
#             <a href="http://" target="_blank" rel="noopener noreferrer">
#               Supports</a
#             >
#           </li>
#           <li>
#             <a href="http://" target="_blank" rel="noopener noreferrer"> FAQ</a>
#           </li>
#           <li>
#             <a href="http://" target="_blank" rel="noopener noreferrer"
#               >Customer Testimonial</a
#             >
#           </li>
#         </ul>
#       </div>
#       <div class="col footer-resources">
#         <h4>Usefull Links</h4>
#         <ul>
#           <li>
#             <a href="http://" target="_blank" rel="noopener noreferrer">
#               Privacy Policy</a
#             >
#           </li>
#           <li>
#             <a href="http://" target="_blank" rel="noopener noreferrer">
#               Terms & Conditions</a
#             >
#           </li>
#           <li>
#             <a href="http://" target="_blank" rel="noopener noreferrer">
#               Refunds</a
#             >
#           </li>
#         </ul>
#       </div>
#     </section>

# if not len(request.username) >= 8:
#     raise HTTPException(status_code=status.HTTP_302_FOUND,
#                         detail=f"{request.username} length must be gretter than 8 character.")
# else:
# else:
#     raise HTTPException(status_code=status.HTTP_302_FOUND,
#                         detail=f"{request.username} already exists.")
# if val_user.count() == 0:
#     new_user = models.User(fullname="Shreeganesh", email_address=request.email_address, created_by=request.email_address,
#                             password=hashing.Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     access_token = tokens.create_access_token(data={"user": {
#         "username": request.username, "email_address": request.email_address, "isAdmin": True}})

#     return {"access_token": access_token, "token_type": "bearer"}

# else:


# @router.get('/verifyemail/{verification_code}')
# def VerifyEmail(verification_code: str, db: Session = Depends(get_db)):
#     result = db.query(models.User).filter(
#         models.User.verification_code == verification_code)

#     if not result:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN, detail='Invalid verification code')
#     else:
#         result.update({"is_active": True, "verification_code": None})
#         db.commit()

#     return {"Account verified successfully!"}


######################################JS################################################################################
# const form = document.getElementById('contact-form');

# form.addEventListener('submit', (event) => {
#   event.preventDefault();
#   const name = document.getElementById('name-input').value;
#   const mobile = document.getElementById('mobile-input').value;
#   const email = document.getElementById('email-input').value;
#   const messages = document.getElementById('messages-input').value;
#   // const data = {name:name, mobile_number:mobile, email:email, messages:messages};

#   fetch('http://127.0.0.1:8000/api/contact-us', {
#     method: 'POST',
#     body: JSON.stringify({name:name, email:email, mobile_number:mobile, messages:messages}),
#     headers: {
#       'Content-Type': 'application/json'
#     }
#   })
#   .then(response => response.json())
#   .then((response) => {
#     if (response.status === 200) {
#     var successMessage = document.getElementById('success-message');
#     successMessage.classList.add("show-message");
#     successMessage.style.display = "block";
#     successMessage.innerHTML = "Thank You for contact us. Our team will reach you as soon as possible.";
#     console.log(successMessage)
#   }else {
#     var errorMessage = document.getElementById('error-message');
#     errorMessage.classList.add("show-message");
#     errorMessage.style.display = "block";
#     errorMessage.innerHTML = response.detail;
#     console.log(errorMessage)
#   }
#   setTimeout(() => {
#     var successMessage = document.getElementById('success-message');
#     var errorMessage = document.getElementById('error-message');
#     successMessage.style.display = "none";
#     errorMessage.style.display = "none";
#   }, 5000);})

#   .then(data => {
#     console.log(data);
#   })

#   .catch(error => {
#     var errorMessage = document.getElementById('error-message');
#     console.error('Error:', error);
#     errorMessage.style.display = "block";
#     errorMessage.innerHTML =error.messages;
#   });

# });


# async function shortItClick() {
#     const response = await fetch("/api/home/app", {
#       method: "post",
#       headers: {
#         'Content-Type': 'application/json'
#       },
#     //   body: JSON.stringify(data)
#     });
#     if (!response.ok) {
#       throw new Error(`HTTP error! Status: ${response.status}`);
#     }
#     const responseData = await response.json();
#     console.log(responseData)
#     return responseData;
#   }

#  document.addEventListener('DOMContentLoaded', (event) => {
#     document.getElementById("myForm").addEventListener("submit", function (e) {
#        e.preventDefault() // Cancel the default action
#        var catName = document.getElementById('catName').value;
#        fetch('/disable/' + catName, {
#              method: 'POST',
#           })
#           .then(resp => resp.text()) // or, resp.json(), etc.
#           .then(data => {
#              document.getElementById("response").innerHTML = data;
#           })
#           .catch(error => {
#              console.error(error);
#           });
#     });
#  });


# const form = document.getElementById('contact-form');
# const successMessage = document.getElementById('success-message');
# const errorMessage = document.getElementById('error-message');

# form.addEventListener('submit', (event) => {
#   event.preventDefault();

#   const name = document.getElementById('name-input').value;
#   const mobile = document.getElementById('mobile-input').value;
#   const email = document.getElementById('email-input').value;
#   const messages = document.getElementById('messages-input').value;
#   // const data = {name:name, mobile_number:mobile, email:email, messages:messages};

#   fetch('http://127.0.0.1:8000/api/contact-us', {
#     method: 'POST',
#     body: JSON.stringify({name:name, email:email, mobile_number:mobile, messages:messages}),
#     headers: {
#       'Content-Type': 'application/json'
#     }
#   })
#   .then(response => response.json())
#   .then(data => {
#     console.log(data);
#     if (data.success) {
#       successMessage.style.display = "block";
#       console.log(successMessage)
#     } else {
#       errorMessage.style.display = "block";
#       console.log(errorMessage)
#     }
#     setTimeout(() => {
#       successMessage.style.display = "none";
#       errorMessage.style.display = "none";
#     }, 10000);
#   })

#   .catch(error => {
#     console.error('Error:', error);
#   });

# });


# const form = document.getElementById('contact-form');

# form.addEventListener('submit', (event) => {
#   event.preventDefault();

#   const name = document.getElementById('name-input').value;
#   const mobile = document.getElementById('mobile-input').value;
#   const email = document.getElementById('email-input').value;
#   const messages = document.getElementById('messages-input').value;
#   const data = {name:name, email:email, mobile_number:mobile, messages:messages};

#   fetch('http://127.0.0.1:8000/api/contact-us', {
#     method: 'POST',
#     body: JSON.stringify(data),
#     headers: {
#       'Content-Type': 'application/json'
#     }
#   })
#   // .then(response => response.json())
#   .then((response) => {
#     if (response.status === 200) {
#     var successMessage = document.getElementById('success-message');
#     successMessage.classList.add("show-message");
#     successMessage.style.display = "block";
#     successMessage.innerHTML = response.detail;
#     console.log(successMessage)
#   }else {
#     var errorMessage = document.getElementById('error-message');
#     errorMessage.classList.add("show-message");
#     errorMessage.style.display = "block";
#     errorMessage.innerHTML = response.detail;
#     console.log(errorMessage)
#   }
#   setTimeout(() => {
#     var successMessage = document.getElementById('success-message');
#     var errorMessage = document.getElementById('error-message');
#     successMessage.style.display = "none";
#     errorMessage.style.display = "none";
#   }, 5000);})
#   .then(data => {
#     console.log(data);
#   })

#   .catch(error => {
#     var errorMessage = document.getElementById('error-message');
#     console.error('Error:', error);
#     errorMessage.style.display = "block";
#     errorMessage.innerHTML =error.messages;
#   });

# });

# perfect code
# const form = document.getElementById('contact-form');

# form.addEventListener('submit', (event) => {
#   event.preventDefault();

#   const name = document.getElementById('name-input').value;
#   const mobile = document.getElementById('mobile-input').value;
#   const email = document.getElementById('email-input').value;
#   const messages = document.getElementById('messages-input').value;
#   const data = {name:name, email:email, mobile_number:mobile, messages:messages};
#   console.log(data)

#   const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
#   const mobilePattern = /^[0-9]{10}$/;

#   if (!emailPattern.test(email)) {
#     var errorMessage = document.getElementById('error-message');
#     errorMessage.classList.add("show-message");
#     errorMessage.style.display = "block";
#     document.getElementById('email-input').focus();
#     errorMessage.innerHTML = "Please enter a valid email address.";
#     return;
#   }
#   if (!mobilePattern.test(mobile)){
#     var errorMessage = document.getElementById('error-message');
#     errorMessage.classList.add("show-message");
#     errorMessage.style.display = "block";
#     document.getElementById('mobile-input').focus();
#     errorMessage.innerHTML = "Please enter a valid 10-digit mobile number.";
#     return;
#   }


#   fetch('http://127.0.0.1:8000/api/contact-us', {
#     method: 'POST',
#     body: JSON.stringify(data),
#     headers: {
#       'Content-Type': 'application/json'
#     }
#   })
#   .then(response => response.json())
#   .then((response) => {
#     if (response.status === 200) {
#     var successMessage = document.getElementById('success-message');
#     successMessage.classList.add("show-message");
#     successMessage.style.display = "block";
#     successMessage.innerHTML = response.detail;

#     //clear the text fields after successfully submited the form
#     document.getElementById('name-input').value = '';
#     document.getElementById('mobile-input').value = '';
#     document.getElementById('email-input').value = '';
#     document.getElementById('messages-input').value = '';
#   }else {
#     var errorMessage = document.getElementById('error-message');
#     errorMessage.classList.add("show-message");
#     errorMessage.style.display = "block";
#     errorMessage.innerHTML = response.detail;

#      //clear the text fields after successfully submited the form
#      document.getElementById('name-input').value = '';
#      document.getElementById('mobile-input').value = '';
#      document.getElementById('email-input').value = '';
#      document.getElementById('messages-input').value = '';
#   }
#   setTimeout(() => {
#     var successMessage = document.getElementById('success-message');
#     var errorMessage = document.getElementById('error-message');
#     successMessage.style.display = "none";
#     errorMessage.style.display = "none";
#   }, 5000);
#   console.log(response);
# })
#   .catch(error => {
#     var errorMessage = document.getElementById('error-message');
#     // console.error('Error:', error);
#     errorMessage.style.display = "block";
#     errorMessage.innerHTML =error.messages;
#   });

# });


#   const name = document.getElementById('name-fields').value;
#   const mobile = document.getElementById('mobile-fields').value;
#   const email = document.getElementById('email-fields').value;
#   const messages = document.getElementById('messages-fields').value;
#   const data = {name:name, email:email, mobile_number:mobile, messages:messages};
#   console.log(data)

#   fetch('http://127.0.0.1:8000/api/contact-us', {
#     method: 'POST',
#     body: JSON.stringify(data),
#     headers: {
#       'Content-Type': 'application/json'
#     }
#   })

#   .then(response => response.json())

#   .then((response) => {
#     if (response.status === 200) {
#     var successMessage = document.getElementById('success-message');
#     successMessage.classList.add("show-message");
#     successMessage.style.display = "block";
#     successMessage.innerHTML = response.detail;

#     //clear the text fields after successfully submited the form
#     document.getElementById('name-fields').value = '';
#     document.getElementById('mobile-fields').value = '';
#     document.getElementById('email-fields').value = '';
#     document.getElementById('messages-fields').value = '';
#   }else {
#     var errorMessage = document.getElementById('error-message');
#     errorMessage.classList.add("show-message");
#     errorMessage.style.display = "block";
#     errorMessage.innerHTML = response.detail

#     //clear the text fields after successfully submited the form
#     document.getElementById('name-fields').value = '';
#     document.getElementById('mobile-fields').value = '';
#     document.getElementById('email-fields').value = '';
#     document.getElementById('messages-fields').value = '';
#   }

#   setTimeout(() => {
#     var successMessage = document.getElementById('success-message');
#     var errorMessage = document.getElementById('error-message');
#     successMessage.style.display = "none";
#     errorMessage.style.display = "none";
#   }, 5000);
#   console.log(response);
#   })

#   .catch(error => {
#     var errorMessage = document.getElementById('error-message');
#     errorMessage.style.display = "block";
#     errorMessage.innerHTML =error.messages;
#   });

# ###########
# const form = document.getElementById('contact-form');
# var successMessage = document.getElementById('success-message');
# var errorMessage = document.getElementById('error-message');

# const name_field = document.getElementById('name-fields');
# const mobile_field = document.getElementById('mobile-fields');
# const email_field = document.getElementById('email-fields');
# const messages_field = document.getElementById('messages-fields');

# form.addEventListener('submit', (event) => {
#   event.preventDefault();
#   if( !validateName()||!validateMobile()||!validateEmail()||!validateMobile()||!validateMassage()){
#     return;
#   }else{
#     const name = document.getElementById('name-fields').value;
#     const mobile = document.getElementById('mobile-fields').value;
#     const email = document.getElementById('email-fields').value;
#     const messages = document.getElementById('messages-fields').value;

#     const data = {name:name, email:email, mobile_number:mobile, messages:messages};
#     console.log(data)

#     fetch('http://127.0.0.1:8000/api/contact-us', {
#       method: 'POST',
#       body: JSON.stringify(data),
#       headers: {
#         'Content-Type': 'application/json'
#       }
#     })
#     .then(response => response.json())
#     .then((response) => {
#       if (response.status === 200){
#       var successMessage = document.getElementById('success-message');
#       successMessage.classList.add("show-message");
#       successMessage.style.display = "block";
#       successMessage.innerHTML = response.detail;

#       //clear the text fields after successfully submited the form
#       document.getElementById('name-fields').value = '';
#       document.getElementById('mobile-fields').value = '';
#       document.getElementById('email-fields').value = '';
#       document.getElementById('messages-fields').value = '';
#     }else {
#       var errorMessage = document.getElementById('error-message');
#       errorMessage.classList.add("show-message");
#       errorMessage.style.display = "block";
#       errorMessage.innerHTML = response.detail;

#        //clear the text fields after successfully submited the form
#       document.getElementById('name-fields').value = '';
#       document.getElementById('mobile-fields').value = '';
#       document.getElementById('email-fields').value = '';
#       document.getElementById('messages-fields').value = '';
#     }
#     setTimeout(() => {
#       var successMessage = document.getElementById('success-message');
#       var errorMessage = document.getElementById('error-message');
#       successMessage.style.display = "none";
#       errorMessage.style.display = "none";
#     }, 5000);
#     console.log(response);
#   })
#     // .catch(error => {
#     //   var errorMessage = document.getElementById('error-message');
#     //   // console.error('Error:', error);
#     //   errorMessage.style.display = "block";
#     //   errorMessage.innerHTML = error.messages;
#     // });
#   }
# });


# function validateName(){
#   const nameValue = name_field.value.trim();
#   if(nameValue === '') {
#       setError('Name field is required');
#       return false;
#     }
#     setError();
#     return true;
# }

# function validateMobile(){
#   const mobileValue = mobile_field.value.trim();
#   if(mobileValue === '') {
#       setError('Mobile number field is required');
#       return false;
#     }else if(!isValidMobileRe(mobileValue)){
#       setError('Mobile number must have 10 didgits');
#       return false;
#     }
#     setError();
#     return true;
# }

# function isValidMobileRe(mobileValue){
#   // const mobileValue = mobile_field.value.trim();
#   const mobilePattern = /^[0-9]{10}$/;
#   return mobilePattern.test(mobileValue);
# }

# function validateEmail(){
#   const emailValue = email_field.value.trim();
#   if(emailValue==='') {
#     setError('Email fields is required');
#     return false;
#     } else if (!isValidEmailPattern(emailValue)) {
#       setError('Provide a valid email address');
#       return false;
#      }
#   setError();
#   return true;
# }

# function isValidEmailPattern(emailValue){
#   // const emailValue = email_field.value.trim();
#   const emailPattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
#   return emailPattern.test(String(emailValue).toLowerCase());
# }

# function validateMassage(){
#  const messageValue = messages_field.value.trim();
#  if(messageValue===''){
#   setError('Messages fields is required');
#   return false;
#  }
#  setError()
#  return true;
# }

# const setError = (message) => {
#   errorMessage.classList.add("show-message");
#   errorMessage.style.display = "block";
#   errorMessage.innerText = message;
# }
# const setSuccess = () => {
#   successMessage.classList.add("show-message");
#   successMessage.style.display = "block";
#   successMessage.innerText = "form submitted succesfully";
#   errorMessage.classList.remove('show-message');
# }


# @router.post("/login", status_code=status.HTTP_200_OK)
# def login(request: Request, request_pass: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     # def login(request: Request, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
#     val_user = db.query(models.User).filter(
#         models.User.username == request_pass.username)
#     print(request_pass.username)
#     print(request_pass.password)

#     errors = []
#     if not val_user.first():
#         # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#         # detail="User does not exists")
#         errors.append("User does not exists")
#         return templates.TemplateResponse("signin.html", {"request": request, "errors": errors})
#     else:
#         # verify password between requesting by a user & database password
#         if not hashing.Hash.verify(val_user.first().password, request_pass.password):
#             # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#             #                     detail="Incorrect Passwords")

#             errors.append("Incorrect Passwords")
#             return templates.TemplateResponse("signin.html", {"request": request, "errors": errors})
#         else:
#             access_token = tokens.create_access_token(data={"user": {
#                 "username": val_user.first().username, "isAdmin": val_user.first().is_admin}})

#             # return {"access_token": access_token, "token_type": "bearer"}
#             return templates.TemplateResponse("sigin.html", {"request": request, "access_token": access_token, "token_type": "bearer"})
#             # return RedirectResponse("/", status_code=303)

 # return {"access_token": access_token, "token_type": "bearer", "status": 200}

            # response = templates.TemplateResponse(
            #     "/dashboard.html", {"request": request, "status": 200})
            # response = RedirectResponse(url="/dashboard.html")
            # print(response)
            # response.set_cookie(key="access_token",
            #                     value=f"Bearer {jwt_token}", httponly=True)
            # # return {"access_token": access_token, "token_type": "bearer", "status": 200}
            # return response
# from fastapi import APIRouter, Depends, status, HTTPException, Response, Request
# from fastapi.responses import JSONResponse
# from botbuilder.core import BotFrameworkAdapter, TurnContext, MessageFactory,BotFrameworkAdapterSettings
# from botbuilder.schema import Activity, ActivityTypes
# import os
# from dotenv import dotenv_values, load_dotenv

# config = dotenv_values(".env")
# connect = load_dotenv()

# router = APIRouter(tags=["ChatBot"])

# # adapter = BotFrameworkAdapter({
# #     "app_id":  os.getenv('AZURE_APP_ID'),
# #     "app_password":  os.getenv('AZURE_APP_PASSWORD'),
# # })

# app_settings = BotFrameworkAdapterSettings(
#     app_id=os.getenv('AZURE_APP_ID'),
#     app_password= os.getenv('AZURE_APP_PASSWORD')
# )

# adapter = BotFrameworkAdapter(app_settings)
# # Your Bot logic
# class MyBot:
#     async def on_turn(self, turn_context: TurnContext):
#         if turn_context.activity.type == ActivityTypes.message:
#             await turn_context.send_activity(MessageFactory.text(f"You said: {turn_context.activity.text}"))

# # Instantiate the Bot
# bot = MyBot()

# # Handle incoming messages
# async def handle_activity(request: Request, adapter: BotFrameworkAdapter):
#     body = await request.body()
#     try:
#         await adapter.process_activity(body, request.headers["Authorization"], bot.on_turn)
#         return JSONResponse(content={}, status_code=200)
#     except Exception as e:
#         return JSONResponse(content={"error": str(e)}, status_code=500)

# # Define the endpoint for receiving messages
# @router.post("/api/messages")
# async def messages_endpoint(request: Request, adapter: BotFrameworkAdapter = Depends()):
#     return await handle_activity(request, adapter)

#  <script>
#       document.addEventListener('DOMContentLoaded', function () {
#           const chatButton = document.getElementById('chatButton');
#           const webchatContainer = document.getElementById('webchatContainer');
#           const closeButton = document.getElementById('closeButton');
  
#           chatButton.addEventListener('click', async function () {
              
#               const res = await fetch('https://directline.botframework.com/v3/directline/tokens/generate', {
#                   method: 'POST',
#                   headers: { 'Authorization': 'Bearer JS8B8oqLjfw.GY2L8zoJTmwammep5oPep9D9OOiIaRlMY35IhSlG1pI' }
#               });
#               const { token } = await res.json();
  
#               const styleSet = window.WebChat.createStyleSet({
                 
#               });
  
#               window.WebChat.renderWebChat(
#                   {
#                       directLine: window.WebChat.createDirectLine({ token }),
#                       userID: 'WebChat_UserId',  
#                       username: 'Web Chat User',  
#                       locale: 'en-US',
#                       styleSet
#                   },
#                   document.getElementById('webchatContainer')
#               );
  
              
#               webchatContainer.style.display = 'block';
#               closeButton.style.display = 'block';
#               chatButton.style.display = 'none';
#           });

#           closeButton.addEventListener('click', function () {
#             webchatContainer.style.display = 'none';
#             closeButton.style.display = 'none';
#             chatButton.style.display = 'block';
#         });
#       });


#   </script> 

# anyio==3.6.2
# bcrypt==4.0.1
# click==8.1.3
# colorama==0.4.6
# ecdsa==0.18.0
# fastapi==0.89.1
# greenlet==2.0.2
# h11==0.14.0
# idna==3.4
# passlib==1.7.4
# psycopg2==2.9.5
# pyasn1==0.4.8
# pydantic==1.10.4
# python-dotenv==0.21.1
# python-jose==3.3.0
# python-multipart==0.0.5
# rsa==4.9
# six==1.16.0
# sniffio==1.3.0
# SQLAlchemy==2.0.2
# starlette==0.22.0
# typing_extensions==4.4.0
# uvicorn==0.20.0
