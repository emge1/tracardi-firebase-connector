from tracardi.domain.context import Context
from tracardi.domain.entity import Entity
from tracardi.domain.event import Event
from tracardi.domain.profile import Profile
from tracardi.domain.session import Session
from tracardi_plugin_sdk.service.plugin_runner import run_plugin

from tracardi_firebase_connector.plugin import FirebaseConnectorAction

init={
            "email": "emygeq@gmail.com",
            "password": "1111",  #przy podaniu złego hasła jest błąd 400 - INVALID_PASSWORD
            "apiKey": "AIzaSyBRjfXq5Au22x63hoW95-4mnvFdKPileRQ",
            "authDomain": "test-9267b.firebaseapp.com",
            "databaseURL": "https://console.firebase.google.com/project/test-9267b",
            "storageBucket": "test-9267b.appspot.com",
            "serviceAccount": None,
            "query": {
                'some': 'data'
            }
    }

payload = {}

result = run_plugin(FirebaseConnectorAction, init, payload)
print(result)
