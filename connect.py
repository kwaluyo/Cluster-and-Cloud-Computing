import couchdb

couchserver = couchdb.Server("http://127.0.0.1:5984")
# Set credentials if necessary
couchserver.resource.credentials = ("admin", "admin")

dbincome = "income_aurin"
dbsatisfaction = "satisfaction_aurin"
dbsupport = "support_aurin"
dbunemployment = "employment_aurin"
if dbincome in couchserver:
    dbIncome = couchserver[dbincome]
else:
    dbIncome = couchserver.create(dbincome)

if dbsatisfaction in couchserver:
    dbSatisfaction = couchserver[dbsatisfaction]
else:
    dbSatisfaction = couchserver.create(dbsatisfaction)

if dbsupport in couchserver:
    dbSupport = couchserver[dbsupport]
else:
    dbSupport = couchserver.create(dbsupport)

if dbunemployment in couchserver:
    dbUnemployment = couchserver[dbunemployment]
else:
    dbUnemployment = couchserver.create(dbunemployment)
