import json
from collections import defaultdict

cities = ['Sydney', 'Melbourne', 'Brisbane', 'Adelaide']

# read data
support2014 = json.load(open('./rawdata/support/support_2014.json'))['features']
support2016 = json.load(open('./rawdata/support/support_2016.json'))['features']
support2017 = json.load(open('./rawdata/support/support_2017.json'))['features']

result = defaultdict(lambda: defaultdict(dict))

for city in cities:
    for obj in support2014:
        # find all the regions in city
        if city + ' (C)' == obj['properties']['lga_name']:
            result[city]['2014']['age_pension_pc'] = obj['properties']['age_pens_3_percent']
            result[city]['2014']['senior_card'] = obj['properties']['snr_card_3_percent']
            result[city]['2014']['disable'] = obj['properties']['disab_pens_3_percent']
            result[city]['2014']['sole_fam'] = obj['properties']['sole_fem_par_3_percent']
            result[city]['2014']['unemployment'] = obj['properties']['unemply_ben_3_percent']

    for obj in support2016:
        if city + ' (C)' == obj['properties']['lga_name']:
            result[city]['2016']['age_pension_pc'] = obj['properties']['age_pnsr_jun_2016_pc_age_pnsr']
            result[city]['2016']['senior_card'] = obj['properties']['snrs_hlth_card_hldrs_jun_2016_pc_snrs_hlth_card_hldrs']
            result[city]['2016']['disable'] = obj['properties']['dsblty_supp_pnsr_jun_2016_pc_dsblty_supp_pnsr']
            result[city]['2016']['sole_fam'] = obj['properties']['f_sole_prnt_pnsr_jun_2016_pc_f_sole_prnt_pnsr']
            result[city]['2016']['unemployment'] = obj['properties']['ppl_rec_unp_bft_jun_2016_pc_ppl_rec_unp_bft']

    for obj in support2017:
        if city + ' (C)' == obj['properties']['lga_name16']:
            result[city]['2017']['age_pension_pc'] = obj['properties']['age_pnsr_jun_2017_pr100_age_pnsr']
            result[city]['2017']['senior_card'] = obj['properties'][
                'snrs_hlth_card_hldrs_jun_2017_pr100_snrs_hlth_card_hldrs']
            result[city]['2017']['disable'] = obj['properties']['dsblty_supp_pnsr_jun_2017_pr100_dsblty_supp_pnsr']
            result[city]['2017']['sole_fam'] = obj['properties']['f_sole_prnt_pnsr_jun_2017_pr100_f_sole_prnt_pnsr']
            result[city]['2017']['unemployment'] = obj['properties']['ppl_rec_unmbft_jun_2017_pr100_ppl_rec_unmbft']

with open('./processed_data/support.json', 'w') as file:
    json.dump(result, file)
    file.close()
