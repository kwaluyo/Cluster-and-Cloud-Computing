import json
from collections import defaultdict

cities = ['Sydney', 'Melbourne', 'Brisbane', 'Adelaide']

result = defaultdict(lambda : defaultdict(dict))

data = json.load(open('./rawdata/death/death_2012_2019.json'))['features']

for year in ['2014', '2015', '2016', '2017', '2018', '2019']:
    for city in cities:
        for obj in data:
            # find all the regions in city
            if city in obj['properties']['gcc_name16']:
                # customise death rate by death number/population
                result[city][year]['std_death_rate'] = round(1000*obj['properties']['_'+year+'_deaths']/obj['properties']['_'+year+'_est_res_population'],3)
                result[city][year]['number_deaths'] = obj['properties']['_'+year+'_deaths']


with open('./processed_data/death.json', 'w') as file:
    json.dump(result, file)
    file.close()
