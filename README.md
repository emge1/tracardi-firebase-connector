# Tracardi plugin

This code can be run within Tracardi workflow.

# Firebase connector actione

The purpose of this plugin is to connect with Firebase and get data from
this database.

# Configuration

This node requires configuration. 

To authenticate, you should write your email and password.

Your Google's Firebase configuration data can be found on 
[Firebase](https://console.firebase.google.com/) > Settings > Project Settings (here scroll to bottom) > 
Add to web app > config. Optionally, you can add a service
account credential (serviceAccount) to authenticate with Firebase as an admin.

Query is a path to data you want to get.

Example of the configuration:

```json
{
  "authentication": {
    "email": "your@email.com",
    "password": "your_password"
  },
  "connection": {
    "apiKey": "your_api_key",
    "authDomain": "yourprojectid.firebaseapp.com",
    "databaseURL": "https://yourdatabaseName.firebaseio.com",
    "storageBucket": "yourprojectId.appspot.com",
    "serviceAccount": "path/to/serviceAccountCredentials.json",
    "query": "your/query/path"
  }
}
```

# Input payload

This node does not process input payload.

# Output

Returns data from a path.
