from jose import jwt 
from jose import JWTError
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.core.config import settings
from app.core.database import get_db
from app.models.user import User


security = HTTPBearer()

def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(security),
        db: Session = Depends(get_db)
):
    token = credentials.credentials


    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        user_id = payload.get("user_id")
        if user_id is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid Token"
            )
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )
    
    user = db.query(User).filter(
        User.id == user_id
    ).first()
    if not user:
        raise HTTPException(
            status_code=401,
            detail="User Not Found"
        )
    return user