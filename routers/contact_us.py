from fastapi import APIRouter, Depends, status, HTTPException, Response, Request, Form
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
import oauth2


router = APIRouter(prefix="/api", tags=["Contact"])
router.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


get_db = database.get_db


@router.post("/contact-us", status_code=200)
def contactUs(request: Request, contacts_fields: schemas.contactUsCreate, db: Session = Depends(get_db)):
    get_user = db.query(models.User).filter(
        models.User.username == contacts_fields.email)

    if not get_user.first():
        user_id = None
    else:
        user_id = get_user.first().id

    # try:
    new_message = models.CONTACTUS(
        name=contacts_fields.name, email=contacts_fields.email, mobile_number=contacts_fields.mobile_number, messages=contacts_fields.messages, user_id=user_id)

    db.add(new_message)
    db.commit()
    db.refresh(new_message)

    return {"detail": "Thank You for contact us.", "status": 200}

    # except Exception as e:
    #     db.rollback()
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST, detail=f"{e.orig}")
