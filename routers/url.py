from fastapi import APIRouter, Depends, status, HTTPException, Response, Request,Cookie
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import database
import schemas
import models
import string
import random
import secrets
import validators
from typing import Optional
import oauth2
import os
from jose import jwt
from dotenv import dotenv_values, load_dotenv
config = dotenv_values(".env")
connect = load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM_CODE = os.getenv('ALGORITHM')


router = APIRouter(prefix="/api", tags=["URL"])

router.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

get_db = database.get_db


@router.post("/home/app", status_code=200)
def createUShort(url_fields: schemas.UrlCreate, db: Session = Depends(get_db)):
    get_url = db.query(models.URL).filter(
        models.URL.target_url == url_fields.original_url)

    if not validators.url(url_fields.original_url):
        raise HTTPException(
            status_code=status.HTTP_303_SEE_OTHER, detail="Enter a valid url")
    else:
        # generate random string(8)
        key_string = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase +
                                            string.digits, k=7))

        url_random_key = "".join(secrets.choice(key_string) for _ in range(8))

        try:
            new_short_url = models.URL(
                target_url=url_fields.original_url,title =url_fields.title, key=url_random_key)

            db.add(new_short_url)
            db.commit()
            db.url = key_string
            db.refresh(new_short_url)
            return {"url_short": f"https://brandly.azurewebsites.net/{url_random_key}", "status": 200}
        except Exception as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=f"{e.orig}")


@router.post("/create-url-short")
def createUrlShort(url_fields: schemas.UrlCreate, db: Session = Depends(get_db),access_token: Optional[str] = Cookie(None)):
    
    if access_token is None:
        return RedirectResponse("/login")
    
    token_value = access_token.replace("Bearer ", "")
    user_info = jwt.decode(token_value, SECRET_KEY, algorithms=[ALGORITHM_CODE])

    username = user_info["user"]["username"]
    print(username)

    get_user = db.query(models.User).filter(
        models.User.username == username)
    
    if (get_user.first()):
            
            if not validators.url(url_fields.original_url):
                raise HTTPException(
                    status_code=status.HTTP_303_SEE_OTHER, detail="Enter a valid URL")
            else:
                    # generate random string(8)
                key_string = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase +
                                            string.digits, k=7))

                url_random_key = "".join(secrets.choice(key_string) for _ in range(8))

                try:
                    new_short_url = models.URL(
                        target_url=url_fields.original_url,title = url_fields.title, key=url_random_key, created_by=username, user_id=get_user.first().id)

                    db.add(new_short_url)
                    db.commit()
                    db.url = key_string
                    db.refresh(new_short_url)

                    return {"status": 200}

                except Exception as e:
                    db.rollback()
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST, detail=f"{e.orig}")
            
    else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User not found")

@router.get("/get-all-url")
def allUrl(db: Session = Depends(get_db),access_token: Optional[str] = Cookie(None)):
    if access_token is None:
        return RedirectResponse("/login")
    
    token_value = access_token.replace("Bearer ", "")
    user_info = jwt.decode(token_value, SECRET_KEY, algorithms=[ALGORITHM_CODE])

    username = user_info["user"]["username"]
    print(username)

    get_user = db.query(models.User).filter(
        models.User.username == username)

    if (get_user.first() and get_user.first().is_active == True):
        
        try:

            all_links = db.query(models.URL).filter(
                models.URL.user_id == get_user.first().id, models.URL.is_active == True).all()

            return all_links
        except Exception as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=f"{e.orig}")
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"User not found")


@router.put("/custom-url/{url_id}")
def customUrl(url_id: int, url_fields: schemas.UrlUpdate, db: Session = Depends(get_db),access_token: Optional[str] = Cookie(None)):
    if access_token is None:
        return RedirectResponse("/login")
    
    token_value = access_token.replace("Bearer ", "")
    user_info = jwt.decode(token_value, SECRET_KEY, algorithms=[ALGORITHM_CODE])

    username = user_info["user"]["username"]
    print(username)

    get_user = db.query(models.User).filter(
        models.User.username == username)

    get_url = db.query(models.URL).filter(
        models.URL.id == url_id, models.URL.user_id == get_user.first().id, models.URL.is_active == True)

    if not get_url.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="not found")

    else:
        if (get_user.first().is_active == True):

            try:

                get_url.update(
                    {"title":url_fields.title,"key": url_fields.key_url, "modified_by": username})

                db.commit()

                return {"status": 200}

            except Exception as e:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, detail=f"{e.orig}")

        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=f"User not found")

@router.put("/delete-url/{url_id}")
def deleteLinked(url_id: int, db: Session = Depends(get_db),access_token: Optional[str] = Cookie(None)):
    if access_token is None:
        return RedirectResponse("/login")
    
    token_value = access_token.replace("Bearer ", "")
    user_info = jwt.decode(token_value, SECRET_KEY, algorithms=[ALGORITHM_CODE])

    username = user_info["user"]["username"]
    print(username)

    get_user = db.query(models.User).filter(
        models.User.username == username)

    if (get_user.first().is_active == True):
        try:

            db.query(models.URL).filter(models.URL.id == url_id, models.URL.user_id == get_user.first(
            ).id, models.URL.is_active == True).update({"is_active": False, "modified_by": username})
            db.commit()

            return {"This link is deleted"}
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=f"{e.orig}")
