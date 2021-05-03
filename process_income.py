import json
from collections import defaultdict

cities = ['Sydney', 'Melbourne', 'Brisbane', 'Adelaide']

data = json.load(open('./rawdata/income.json'))['features']

result = defaultdict(dict)

# each city would have median income, mean income, total earner count, median age of earners
for city in cities:
    for obj in data:
        regiron_name = obj['properties']['lga_name16']
        if city in regiron_name and len(regiron_name.split()) == 2:
            result[city]['median_aud'] = obj['properties']['median_aud']
            result[city]['mean_aud'] = obj['properties']['mean_aud']
            result[city]['earner_count'] = obj['properties']['earners_persons']
            result[city]['median_age_of_earners_years'] = obj['properties']['median_age_of_earners_years']

with open('./processed_data/income.json', 'w') as file:
    json.dump(result, file)
    file.close()
