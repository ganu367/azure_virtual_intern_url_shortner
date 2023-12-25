from fastapi import APIRouter, Depends, status, HTTPException, Response, Request, Form, Body,Cookie
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import database
import models
import hashing
import tokens
import schemas
import oauth2
from fastapi.security import OAuth2PasswordRequestForm
import os
from typing import Optional

router = APIRouter(prefix="/auth", tags=["Authentication"])


router.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(
    directory=os.path.abspath(os.path.expanduser('templates')))

get_db = database.get_db


@router.post("/login")
def login(response: Response, request: Request, request_detail: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    val_user = db.query(models.User).filter(
        models.User.username == request_detail.username)

    if not val_user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User does not exists")

    else:
        # verify password between requesting by a user & database password
        if not hashing.Hash.verify(val_user.first().password, request_detail.password):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Incorrect Passwords")
        else:

            jwt_token = tokens.create_access_token(data={"user": {
                "username": val_user.first().username, "isAdmin": val_user.first().is_admin}})

            response = RedirectResponse(
                url='/dashboard', status_code=status.HTTP_302_FOUND)
            
           
            response.set_cookie(
            key="access_token",
            value=f"Bearer {jwt_token}",
            httponly=True,
            secure=True,
            samesite="none",
             )

            return {"response": response, "status": 200}


@router.put("/update-password", status_code=status.HTTP_202_ACCEPTED)
def updatePassword(request: schemas.UserPassword, db: Session = Depends(get_db), current_user: schemas.UserCreate = Depends(oauth2.get_current_user)):
    _username_ = current_user.user["username"]

    val_user = db.query(models.User).filter(
        models.User.username == _username_).first()

    if not val_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    else:
        if not hashing.Hash.verify(val_user.password, request.current_password):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Incorrect Passwords")

        elif (request.new_password != request.confirm_password):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Password not matched")
        else:
            db.query(models.User).filter(models.User.username == _username_).update(
                {"password": hashing.Hash.bcrypt(request.new_password)})
            db.commit()

            return {f"Password successfully updated"}


@router.put("/forget-password/{username}", status_code=status.HTTP_202_ACCEPTED)
def forgetPassword(username: str, request: schemas.ForgetPassword, db: Session = Depends(get_db)):
    val_user = db.query(models.User).filter(
        models.User.username == username).first()

    if not val_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    else:
        if (request.new_password != request.confirm_password):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Password not matched")
        else:
            db.query(models.User).filter(models.User.username == username).update(
                {"password": hashing.Hash.bcrypt(request.new_password)})
            db.commit()
            return {f"Password successfully updated"}
        
@router.get("/logout")
def logout(response: Response, request: Request):
    response = RedirectResponse("/login", status_code=302)
    response.delete_cookie(key='access_token')  # Corrected key
    return response        
