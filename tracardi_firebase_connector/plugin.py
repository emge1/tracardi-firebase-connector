from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.result import Result
from tracardi_firebase_connector.model.configuration import FirebaseConnection, FirebaseAuthentication
from tracardi.service.storage.helpers.source_reader import read_source #
import firebase

class FirebaseConnectorAction(ActionRunner):

    @staticmethod
    async def build(**kwargs) -> 'FirebaseConnectorAction':
        plugin = FirebaseConnectorAction(**kwargs)
        plugin.client = FirebaseAuthentication(**kwargs)
        connection = FirebaseConnection(**kwargs)
        plugin.db = await connection.connect()

        return plugin

    def __init__(self, **kwargs):
        self.config = PluginConfiguration(**kwargs)
        self.client = None
        self.db = None
        if 'query' not in kwargs:
            raise ValueError("Define query, please.")

        self.query = kwargs['query']

    async def run(self, payload):
        result = await self.db.child(self.config.query).get()
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
            outputs=['result'],
            version='0.1.0',
            license="MIT",
            author="Marcin Gaca",
            init={
                "authentication": {
                  "email": None
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
        ),
        metadata=MetaData(
            name='Firebase connector',
            desc='Connects to Firebase and reads data.',
            type='flowNode',
            width=200,
            height=100,
            icon='firebase',
            group=["Connectors"]
        )
    )
