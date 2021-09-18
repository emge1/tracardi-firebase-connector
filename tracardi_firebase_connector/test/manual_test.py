from tracardi_plugin_sdk.service.plugin_runner import run_plugin

from tracardi_firebase_connector.plugin import FirebaseConnectorAction

init = {
    "authentication": {
        "email": None,
        "password": None
    },
    "connection": {
        "apiKey": None,
        "authDomain": None,
        "databaseURL": None,
        "storageBucket": None,
        "serviceAccount": None,
        "query": None
    }
}

payload = {

}

result = run_plugin(FirebaseConnectorAction, init, payload)
