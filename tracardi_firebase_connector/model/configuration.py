from pydantic import BaseModel
from typing import Optional
from firebase import Firebase


class FirebaseAuthentication(BaseModel):
    email: str
    password: str

    async def authentication(self):
        auth = firebase.auth()
        return await auth.sign_in_with_email_and_password(email=self.email,
                                                          password=self.password)


class FirebaseConnection(BaseModel):
    apiKey: str
    authDomain: str
    databaseURL: str
    storageBucket: str
    serviceAccount: Optional[str]

    async def connect(self):
        return await Firebase.config(apiKey=self.apiKey,
                                     authDomain=self.authDomain,
                                     databaseURL=self.databaseURL,
                                     storageBucket=self.storageBucket,
                                     serviceAccount=self.serviceAccount)


class PluginConfiguration(BaseModel):
    query: str
