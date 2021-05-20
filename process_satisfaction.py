import json
from collections import defaultdict

cities = ['Sydney', 'Melbourne', 'Brisbane', 'Adelaide']

data = json.load(open('./rawdata/satisfaction.json'))['features']

result = defaultdict(lambda : defaultdict(list))

for city in cities:
    for obj in data:
        # find all the regions in city
        if city in obj['properties']['sa2_name16']:
            # loop through satisfaction level 10 to 100
            for level in range(10,101,10):
                score_pc = obj['properties']['_life_satisfaction_pc_'+str(level)+'_synth']
                # filter the none and zeros -> missing values
                if score_pc:
                    result[city]['satisfaction_' + str(level) + '_pc'].append(score_pc)


finalresult = defaultdict(dict)

for city, feature in result.items():
    for k, v in feature.items():
        # take average values of all the region to represent the city
        finalresult[city][k] = round(sum(v)/len(v),4)

with open('./processed_data/statisfaction.json', 'w') as file:
    json.dump(finalresult, file)
    file.close()
