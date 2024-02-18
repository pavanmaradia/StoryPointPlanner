import fastapi
from fastapi.middleware.cors import CORSMiddleware
import fastapi.security as _security
import schemas
import sqlalchemy.orm as _orm
import servicer

app = fastapi.FastAPI()

ORIGINS = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/users")
async def create_user(user: schemas.UserCreate, db: _orm.Session = fastapi.Depends(servicer.get_db)):
    db_user = await servicer.get_user_by_email(email=user.email, db=db)

    if db_user:
        raise fastapi.HTTPException(status_code=400, detail="Email already Exists.")

    _user = await servicer.create_user(user, db)
    return await servicer.create_token(_user)


@app.post("/api/token/")
async def generate_token(
    from_data: _security.OAuth2PasswordRequestForm = fastapi.Depends(),
    db: _orm.Session = fastapi.Depends(servicer.get_db),
):
    user = await servicer.authenticate_user(email=from_data.username, password=from_data.password, db=db)

    if not user:
        raise fastapi.HTTPException(status_code=401, detail="Invalid Credentials")

    return await servicer.create_token(user)
