import couchdb
# can change to the unimelb and it will connect
couchserver = couchdb.Server("http://127.0.0.1:5984")
# Set credentials if necessary
couchserver.resource.credentials = ("admin", "admin")

dbname = "test2"
dbresult = 'result5'
if dbname in couchserver:
    db = couchserver[dbname]
else:
    db = couchserver.create(dbname)

if dbresult in couchserver:
    dbres = couchserver[dbresult]
else:
    dbres = couchserver.create(dbresult)
# import json
# data = []
#
# # need to be changed to loop based on the folder
# with open("data.jsonl", 'r', encoding='utf-8') as f:
#     for line in f:
#         data.extend(json.loads(line))
#
# #need to preprocess data which is tweet_id as key
# # will need to be changed based on the folder
# city = "ADELAIDE"
#
# # # should be based on the name of the folder
# for each in data:
#     each["city"]="ADELAIDE"
#
#
# for each in data:
#     db.save(each)