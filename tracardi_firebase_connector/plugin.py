from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.result import Result
from tracardi_firebase_connector.model.configuration import FirebaseConfiguration
from firebase import Firebase

class FirebaseConnectorAction(ActionRunner):

    def __init__(self, **kwargs):
        self.config = FirebaseConfiguration(**kwargs)

        # self.client = None

        if 'query' not in kwargs:
            raise ValueError("Define query, please.")

        self.query = kwargs["query"]

    async def run(self, payload):
        firebase = Firebase({"apiKey": self.config.apiKey,
                             "authDomain": self.config.authDomain,
                             "databaseURL": self.config.databaseURL,
                             "storageBucket": self.config.storageBucket,
                             "serviceAccount": self.config.serviceAccount})
        firebase_db = firebase.database()
        auth = firebase.auth()
        user = auth.sign_in_with_email_and_password(self.config.email, self.config.password)

        print(type(self.config.query))
        print(user['idToken'])
        result = firebase_db.push(self.config.query, user['idToken'])
        # result = await firebase_db.child(self.config.query).get()
        return Result(port="payload", value={"result": result})

'''    async def close(self):
        if self.db:
            await self.db.close()'''


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='tracardi_firebase_connector.plugin',
            className='FirebaseConnectorAction',
            inputs=["payload"],
            outputs=['payload'],
            version='0.1',
            license="MIT",
            author="Marcin Gaca",
            init={
                  "email": None,
                  "password": None,
                  "apiKey": None,
                  "authDomain": None,
                  "databaseURL": None,
                  "storageBucket": None,
                  "serviceAccount": None,
                  "query": None,
                }
        ),
        metadata=MetaData(
            name='tracardi-firebase-connector',
            desc='This plugin connects to Firebase and reads data from the database on given query.',
            type='flowNode',
            width=200,
            height=100,
            icon='icon',
            group=["General"]
        )
    )
