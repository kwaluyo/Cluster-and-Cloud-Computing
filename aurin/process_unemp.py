import json
from collections import defaultdict

cities = ['Sydney', 'Melbourne', 'Brisbane', 'Adelaide']

result = defaultdict(lambda : defaultdict(dict))

unemp_num = json.load(open('./rawdata/unemployment/unemployment_num.json'))['features']

unemp_rate = json.load(open('./rawdata/unemployment/unemployment_rate.json'))['features']

result = defaultdict(lambda : defaultdict(lambda : defaultdict(list)))

for year in ['2014', '2015', '2016', '2017', '2018']:
    for city in cities:
        for obj in unemp_num:
            # find city
            if city+' (C)' in obj['properties']['lga_name18']:
                result[city][year]['unemp_num'].append(obj['properties']['mar_'+year])
                result[city][year]['unemp_num'].append(obj['properties']['jun_'+year])
                if year != '2018':
                    result[city][year]['unemp_num'].append(obj['properties']['sep_'+year])
                    result[city][year]['unemp_num'].append(obj['properties']['dec_'+year])
        for obj in unemp_rate:
            if city+' (C)' in obj['properties']['lga_name18']:
                result[city][year]['unemp_rate'].append(obj['properties']['mar_'+year])
                result[city][year]['unemp_rate'].append(obj['properties']['jun_'+year])
                if year != '2018':
                    result[city][year]['unemp_rate'].append(obj['properties']['sep_'+year])
                    result[city][year]['unemp_rate'].append(obj['properties']['dec_'+year])


final_result = defaultdict(lambda: defaultdict(dict))

for city, v in result.items():
    for year, v1 in v.items():
        # take average
        final_result[city][year]['avg_unemp_num'] = round(sum(v1['unemp_num']) / len(v1['unemp_num']), 2)
        final_result[city][year]['avg_unemp_rate'] = round(sum(v1['unemp_rate']) / len(v1['unemp_rate']), 2)


with open('./processed_data/unemployment.json', 'w') as file:
    json.dump(final_result, file)
    file.close()
