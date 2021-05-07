import couchdb

# CouchDB environment variables
host = "172.26.130.64"
port = "5984"
username = "admin"
password = "admin"
db_name = "tweets"

# can change to the unimelb and it will connect
couchserver = couchdb.Server("http://" + username + ':' + password + '@' + host + ':' + port)
# Set credentials if necessary
couchserver.resource.credentials = (username, password)


def connect_to_couchdb_server(username, password, host, port):
    couchdb_server = couchdb.Server('http://' + username + ':' + password + '@' + host + ':' + port)
    return couchdb_server


def connect_to_db(server, db_name):
    try:
        return server[db_name]
    except:
        return server.create(db_name)


# Establish connection to couchDB server and database
server = connect_to_couchdb_server(username, password, host, port)
database = connect_to_db(server, db_name)


def save_to_db(tweet, db=database):
    # check for duplication first
    if str(tweet["id"]) not in db:
        # set tweet id as the document id for duplication removal
        tweet["_id"] = "%s" % tweet["id"]

        if not tweet is None:
            try:
                db.save(tweet)
            except:
                pass