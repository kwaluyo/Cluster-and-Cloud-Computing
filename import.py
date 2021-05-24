import json
from collections import defaultdict
import connect

cities = ['Sydney', 'Melbourne', 'Brisbane', 'Adelaide']
# import income to db
with open('./processed_data/income.json', 'r', encoding='utf-8') as file:
    for line in file:
        parsed_input = json.loads(line)
        for city in cities:
            for row in parsed_input[city]:
                result = {
                    'city': city,
                    'year': row
                }
                result.update(parsed_input[city][row])
                # print(parsed_input[city][row])
                # print(result)
                connect.dbIncome.save(result)
                # exit;

# import satisfaction to db
with open('./processed_data/satisfaction.json', 'r', encoding='utf-8') as file:
    for line in file:
        parsed_input = json.loads(line)
        for city in cities:
            result = {
                'city': city,
            }
            result.update(parsed_input[city])
            connect.dbSatisfaction.save(result)

# import support to db
with open('./processed_data/support.json', 'r', encoding='utf-8') as file:
    for line in file:
        parsed_input = json.loads(line)
        for city in cities:
            for row in parsed_input[city]:
                result = {
                    'city': city,
                    'year': row
                }
                result.update(parsed_input[city][row])
                connect.dbSupport.save(result)

# # import unemployment to db
with open('./processed_data/unemployment.json', 'r', encoding='utf-8') as file:
    for line in file:
        parsed_input = json.loads(line)
        for city in cities:
            for row in parsed_input[city]:
                result = {
                    'city': city,
                    'year': row
                }
                result.update(parsed_input[city][row])
                connect.dbUnemployment.save(result)