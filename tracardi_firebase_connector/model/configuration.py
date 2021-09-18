from pydantic import BaseModel
from typing import Optional
from firebase import Firebase


class Connection(BaseModel):
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
