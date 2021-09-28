from pydantic import BaseModel
from typing import Optional


class FirebaseConfiguration(BaseModel):
    email: str
    password: str

    apiKey: str
    authDomain: str
    databaseURL: str
    storageBucket: str
    serviceAccount: Optional[str]

    query: dict
