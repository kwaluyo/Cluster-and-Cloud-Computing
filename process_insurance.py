import json
from collections import defaultdict

cities = ['Sydney', 'Melbourne', 'Brisbane', 'Adelaide']

data = json.load(open('./rawdata/insurance.json'))['features']

result = defaultdict(list)

# to store the data into the format {city1: [insurance_region1, insurance_region2],
#                                    city2: [insurance_region1],...}
for city in cities:
    for obj in data:
        if city in obj['properties']['phn_name']:
            result[city].append(obj['properties']['est_ppl_18yrs_plus_priv_hlth_insur_2014_15_asr_100'])

# take average value
for key in result:
    result[key] = round(sum(result[key])/len(result[key]), 2)

with open('./processed_data/insurance.json', 'w') as f:
    json.dump(result, f)
    f.close()
