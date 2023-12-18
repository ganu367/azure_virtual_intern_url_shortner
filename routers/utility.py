from fastapi import APIRouter, Depends, status, HTTPException, Response, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
import database
import schemas
import models
# import requests

router = APIRouter(tags=["URL"])

get_db = database.get_db


def updateCount(url_key: str, click_count_update: schemas.UrlUpdateCount, db: Session = Depends(get_db)):
    try:
        click_count_update.click_count += 1

        count_visit = db.query(models.URL).filter(
            models.URL.key == url_key).update({"click_count": click_count_update.click_count})

        print("Total_visit_count", click_count_update.click_count)

        db.commit()
        return count_visit

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"{e.orig}")


@router.get("/{url_key}")
def forwadToRedirect(url_key: str, request: Request, db: Session = Depends(get_db)):
    get_url = db.query(models.URL).filter(
        models.URL.key == url_key)

    if not get_url.first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"http://127.0.0.1:8000/{url_key} not found")

    else:
        if click_count_update := get_url.filter(models.URL.is_active == True).first():
            try:
                updateCount(url_key, click_count_update, db)
                return RedirectResponse(get_url.first().target_url)

            except Exception as e:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, detail=f"{e.orig}")
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=f"http://127.0.0.1:8000/{url_key} not found")
