import couchdb

# CouchDB environment variables
host = "172.26.130.64"
# host = "127.0.0.1"
port = "5984"
username = "admin"
password = "admin"

def connect_to_couchdb_server(username, password, host, port):
    """
    Establish connection to couchdb server.
    """
    couchdb_server = couchdb.Server('http://' + username + ':' + password + '@' + host + ':' + port)
    return couchdb_server


def connect_to_db(server, db_name):
    """
    Connect to or create a database with db_name.
    """
    try:
        return server[db_name]
    except:
        return server.create(db_name)


# Establish connection to couchDB server and database
server = connect_to_couchdb_server(username, password, host, port)
dbSentiment = connect_to_db(server, "old_tweets")
dbIncome = connect_to_db(server, "income_aurin")
dbSatisfaction = connect_to_db(server, "satisfaction_aurin")
dbSupport = connect_to_db(server, "support_aurin")
dbUnemployment = connect_to_db(server, "employment_aurin")
dbRaw = connect_to_db(server, "rawdata")
dbRealTimeData = connect_to_db(server, "tweets")