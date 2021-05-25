'''
COMP90024
Team 17
Jeanelle Abanto: 1133815
Kartika Waluyo: 1000555
Radhimas Djan: 1146240
Zi Jin: 987771  
'''

import json
import connect

cities = ['Sydney', 'Melbourne', 'Brisbane', 'Adelaide']

# export income to db
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
                connect.dbIncome.save(result)

# export support to db
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

# export unemployment to db
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