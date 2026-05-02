from typing import Annotated
from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

security = HTTPBasic()

@app.get("/users/me")
def read_current_user(
    credential: Annotated[HTTPBasicCredentials, Depends(security)]
):
    return {"username": credential.username, "password": credential.password}
