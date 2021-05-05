import couchdb
# can change to the unimelb and it will connect
couchserver = couchdb.Server("http://127.0.0.1:5984")
# Set credentials if necessary
couchserver.resource.credentials = ("admin", "admin")

dbresult = 'result5'
if dbresult in couchserver:
    dbres = couchserver[dbresult]
else:
    dbres = couchserver.create(dbresult)