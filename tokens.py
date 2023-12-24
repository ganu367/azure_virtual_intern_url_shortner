from jose import JWTError, jwt
from datetime import datetime, timedelta
import schemas
import os
from dotenv import dotenv_values, load_dotenv

config = dotenv_values(".env")
connect = load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM_CODE = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = 1


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM_CODE)
    return encoded_jwt


def verify_token(data: str, credentials_exception):
    try:
        payload = jwt.decode(data, SECRET_KEY, algorithms=[ALGORITHM_CODE])
        user: dict = payload.get("user")

        if user["username"] is None:
            raise credentials_exception

        token_data = schemas.TokenData(user=user)
    except JWTError:
        raise credentials_exception

    return token_data
