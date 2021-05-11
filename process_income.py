import json
from collections import defaultdict

cities = ['Sydney', 'Melbourne', 'Brisbane', 'Adelaide']

result = defaultdict(lambda : defaultdict(dict))

for year in ['2014', '2015', '2016', '2017']:
    data = json.load(open('./rawdata/income/income_'+year+'.json'))['features']
    for city in cities:
        for obj in data:
            # find all the regions in city
            if city in obj['properties']['gccsa_name_2016']:
                result[city][year]['mean_income_yr'] = obj['properties']['estimates_personal_income_year_ended_30_june_mean_employee']
                result[city][year]['median_income_yr'] = obj['properties']['estimates_personal_income_year_ended_30_june_median_employee']
                result[city][year]['earner_number'] = obj['properties']['estmts_prsnl_incme_yr_endd_30_jne_emplye_ernrs_nm']
                result[city][year]['earner_age_meadian'] = obj['properties']['estmts_prsnl_incme_yr_endd_30_jne_emplye_ernrs_mdn_age_yrs']

with open('./processed_data/income.json', 'w') as file:
    json.dump(result, file)
    file.close()
