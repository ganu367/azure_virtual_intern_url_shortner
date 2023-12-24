from fastapi import FastAPI, Request, status,Depends,HTTPException,Cookie
from fastapi.responses import RedirectResponse, HTMLResponse,JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from database import engine
import models
from internal import authentication, registration
from routers import url, contact_us, utility
import oauth2
import schemas
from jose import JWTError, jwt
from sqlalchemy.orm import Session
import database
from typing import Optional
import os
from dotenv import dotenv_values, load_dotenv

config = dotenv_values(".env")
connect = load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
get_db = database.get_db

models.Base.metadata.create_all(engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Brandly | URL Shortnal-Shorten your links with ease using our free URL shortener"})


@app.get("/login", response_class=HTMLResponse)
def loginUser(request: Request):
    return templates.TemplateResponse("signin.html", {"request": request, "title": "Login"})


@app.get("/register", response_class=HTMLResponse)
def loginUser(request: Request):
    return templates.TemplateResponse("sign_up.html", {"request": request, "title": " Sign Up"})


@app.get("/services", response_class=HTMLResponse)
def services(request: Request):
    return templates.TemplateResponse("services.html", {"request": request, "title": "Our Services"})

@app.get("/about-us", response_class=HTMLResponse)
def about_us(request: Request):
    return templates.TemplateResponse("about_us.html", {"request": request, "title": "Brandly |Who we are"})

@app.get("/contact_us", response_class=HTMLResponse)
def contactUs(request: Request):
    return templates.TemplateResponse("contact_us.html", {"request": request, "title": "Contact Us"})


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request,db: Session = Depends(get_db),access_token: Optional[str] = Cookie(None),):

    if access_token is None:
        return RedirectResponse("/login")
    
    token_value = access_token.replace("Bearer ", "")
    user_info = jwt.decode(token_value, SECRET_KEY, algorithms=[ALGORITHM])

    username = user_info["user"]["username"]
   
    user = db.query(models.User).filter(models.User.username==username).first()
    get_url = db.query(models.URL).filter(models.URL.user_id ==user.id).all()

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "name": user.name,
            "url_data":get_url,
            "title": "Dashboard - Manage Your Links",
        },
    )

@app.get("/create", response_class=HTMLResponse)
def create(request: Request,db: Session = Depends(get_db),access_token: Optional[str] = Cookie(None),):

    if access_token is None:
        return RedirectResponse("/login")
    
    token_value = access_token.replace("Bearer ", "")
    user_info = jwt.decode(token_value, SECRET_KEY, algorithms=[ALGORITHM])

    username = user_info["user"]["username"]
   
    user = db.query(models.User).filter(models.User.username==username).first()

    return templates.TemplateResponse("create.html", {"request": request, "name": user.name, "title": "Create Your Links"})


@app.get("/custom/{id}", response_class=HTMLResponse)
def custom(id:int,request: Request,db: Session = Depends(get_db),access_token: Optional[str] = Cookie(None),):

    if access_token is None:
        return RedirectResponse("/login")
    
    token_value = access_token.replace("Bearer ", "")
    user_info = jwt.decode(token_value, SECRET_KEY, algorithms=[ALGORITHM])

    username = user_info["user"]["username"]
   
    user = db.query(models.User).filter(models.User.username==username).first()
    get_url = db.query(models.URL).filter(models.URL.id==id).first()

    return templates.TemplateResponse("custom.html", {"request": request, "title": "Update Your Links", "name": user.name,"url_id":get_url})




app.include_router(authentication.router)
app.include_router(registration.router)
app.include_router(url.router)
app.include_router(contact_us.router)
app.include_router(utility.router)
