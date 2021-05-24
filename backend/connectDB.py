import couchdb
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
couchserver = couchdb.Server(os.getenv('DB_URL'))
# Set credentials if necessary
couchserver.resource.credentials = (os.getenv('DB_USER'), os.getenv('DB_PASS'))

dbsentiment = "sentiments"
dbincome = "income_aurin"
dbsatisfaction = "satisfaction_aurin"
dbsupport = "support_aurin"
dbunemployment = "employment_aurin"
dbraw = "rawdata"

if dbsentiment in couchserver:
    dbSentiment = couchserver[dbsentiment]
else:
    dbSentiment = couchserver.create(dbsentiment)

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

if dbraw in couchserver:
    dbRaw = couchserver[dbraw]
else:
    dbRaw = couchserver.create(dbraw)