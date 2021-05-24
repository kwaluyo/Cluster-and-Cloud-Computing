import flask
from flask import jsonify, request,current_app
from flask_cors import cross_origin
import connectDB

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>api</h1>"

# A route to return all of the available entries in our catalog.
@app.route('/api/data/all', methods=['GET'])
@cross_origin()
def api_all():
    rows = connectDB.dbIncome.view('_all_docs', include_docs=True)
    data = [row['doc'] for row in rows]
    # df = connectDB.pd.DataFrame(data)
    # print(df.head(10))
    response = jsonify(data)

    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/api/income', methods=['GET'])
@cross_origin()
def api_city():
    if 'city' in request.args:
        city = str(request.args['city'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []
    result = []
    sentiment = []
    
    #adding sentiments
    for row in connectDB.dbSentiment.view('_design/data/_view/alldata',group=True):
        keys = row['key']
        if keys[0] == city.upper():
            row['value']['year'] = keys[1]
            sentiment.append(row['value'])

    for row in connectDB.dbIncome.view('_design/views/_view/income', key=city):
        # row['value']['years'] = {'year':row['value']['year']}
        for line in sentiment:
            if line['year'] == row['value']['year']:
                row['value']['years'] = {'sentiment':line}
        result.append(row['value'])

    results.append({'docs':result})
    # results.append({'sentiment':sentiment)
    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    response = jsonify(results)

    # Enable Access-Control-Allow-Origin
    # response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/api/unemployment', methods=['GET'])
@cross_origin()
def api_cityUnemp():
    if 'city' in request.args:
        city = str(request.args['city'])
    else:
        return "Error: No City field provided. Please specify an City."

    # Create an empty list for our results
    results = []
    result = []
    sentiment = []
    #adding sentiments
    for row in connectDB.dbSentiment.view('_design/data/_view/alldata',group=True):
        keys = row['key']
        if keys[0] == city.upper():
            row['value']['year'] = keys[1]
            sentiment.append(row['value'])

    for row in connectDB.dbUnemployment.view('_design/views/_view/data', key=city):
        # row['value']['years'] = {'year':row['value']['year']}
        for line in sentiment:
            if line['year'] == row['value']['year']:
                row['value']['years'] = {'sentiment':line}
        result.append(row['value'])

    results.append({'docs':result})
    # for doc in connectDB.dbUnemployment.find({'selector': {'city': city}}):
    #     results.append(doc)
    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    response = jsonify(results)

    # Enable Access-Control-Allow-Origin
    # response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/api/support', methods=['GET'])
@cross_origin()
def api_citySupport():
    if 'city' in request.args:
        city = str(request.args['city'])
    else:
        return "Error: No City field provided. Please specify an City."

    # Create an empty list for our results
    results = []
    result = []
    sentiment = []
    #adding sentiments
    for row in connectDB.dbSentiment.view('_design/data/_view/alldata',group=True):
        keys = row['key']
        if keys[0] == city.upper():
            row['value']['year'] = keys[1]
            sentiment.append(row['value'])
    
    for row in connectDB.dbSupport.find({'selector': {'city': city}}):
        # results.append(row)
        for line in sentiment:
            if line['year'] == row['year']:
                row['years'] = {'sentiment':line}
        result.append(row)

    results.append({'docs':result})
    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    response = jsonify(results)

    # Enable Access-Control-Allow-Origin
    # response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/api/realtime', methods=['GET'])
@cross_origin()
def api_citySatisfaction():
    if 'city' in request.args:
        city = str(request.args['city'])
    else:
        return "Error: No City field provided. Please specify an City."

    # Create an empty list for our results
    results = []
    result = []
    sentiment = []
    #adding sentiments
    for row in connectDB.dbRealTimeData.view('_design/data/_view/realtime', group=True,key=city.upper()):
        # keys = row['key']
        # if keys[0] == city.upper():
        row['value']['city'] =  row['key']
        result.append(row['value'])

    # for row in connectDB.dbSatisfaction.find({'selector': {'city': city}}):
    #     # results.append(row)
    #     for line in sentiment:
    #         row['years'] = {'sentiment':line}
    #     result.append(row)
    
    results.append({'docs':result})
    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    response = jsonify(results)

    # Enable Access-Control-Allow-Origin
    # response.headers.add("Access-Control-Allow-Origin", "*")
    return response

app.run()