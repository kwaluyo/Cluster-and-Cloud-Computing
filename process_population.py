import json
from collections import defaultdict

age_group = ['15_24', '25_34', '35_44', '45_54', '55_64', '65+']
cities = ['Sydney', 'Melbourne', 'Brisbane', 'Adelaide']

data = []
for group in age_group:
    data.append(json.load(open('./rawdata/population/population_' + group + '.json'))['features'])

result = defaultdict(dict)

for i in range(len(cities)):
    for j in range(len(age_group)):
        result[cities[i]][age_group[j]] = data[j][i]['properties']['pop_distribution']

# the result would have the format of {city1:{age_group1: pop_dist, age_group2:pop_dist},
#                                      city2:{age_group1: pop_dist, age_group2:pop_dist}...}

with open('./processed_data/population.json', 'w') as f:
    json.dump(result, f)
    f.close()
