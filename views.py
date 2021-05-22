import couchdb
import connect
from couchdb import design

def create_income_view(db):
    view = design.ViewDefinition('views', 'income', """
        function (doc) {
            if (doc.city) {
                emit(doc.city, {city :doc.city,year:doc.year,mean:doc.mean_income_yr});
            }
        }
        """)
    if not view.get_doc(db):
        view.sync(db)

def create_sentiment_view(db):
    view = design.ViewDefinition('data', 'alldata', """
        function (doc) {
            emit([doc.location,doc.time.slice(doc.time.length-4)], {compound:doc.sentiment.compound,negative:doc.sentiment.neg,
                neutral:doc.sentiment.neu,positive:doc.sentiment.pos
            });
        }
        """)
    # if not view.get_doc(db):
    view.sync(db)

# create_income_view(connect.dbIncome)
create_sentiment_view(connect.dbSentiment)