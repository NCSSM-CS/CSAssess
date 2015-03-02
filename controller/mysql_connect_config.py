def getConfig(dbName):
    config = {
        'user': 'root',
        'password': '',
        'host': '127.0.0.1',
        'database': dbName,
        'raise_on_warnings': True,
    }
    return config
