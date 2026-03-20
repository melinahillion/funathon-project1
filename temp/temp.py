# %%
dict_fr_en = {
  'idmutation':['trans_id', 'Unique identifier code of the transaction'],
  'datemut':['trans_date', 'Date of the official certified transaction'],
  'anneemut':['trans_year', 'Year of the official certified transaction'],
  'moismut':['trans_month','Month of the official certified transaction'], # Notaries
  'idnatmut':['trans_type_code','Type of transaction'], # Different types of transactions
  'libnatmut':['trans_type_label','Type of transaction'],
  'valeurfonc':['price','Price of the transaction'],  
  'dteloc':['prop_type','Type of property : a flat or a house'],
  'jannath':['prop_year','Year of contruction of the property'],
  'ccodep':['prop_loc_dep','Department code where the property is located'],  # list of departments in France  - overseas yes but Alsace Moselle nope
  'depcom':['prop_loc_',"Official city's code where the property is located"],  # COG : official geographical code https://www.insee.fr/en/metadonnees/source/serie/s2084
  'x':['prop_loc_x','Longitude where the property is located'],  # Type of projection ?
  'y':['prop_loc_y','Latitude where the property is located'],  # Type of projection ?
  'distance_ltm':['dist_tosea','Distance of the property to the nearest seashore - capped at 10km'],
  'distance_ltm_corr':['dist_tosea_corr','Corrected distance of the property to the nearest seashore - capped at 10km'],
  'dnbniv':['n_floors','Number of floor in the property (either if a building or a house)'], # 0 to 90
  'dnbbai':['n_bath','Number of bathrooms reported in the property'],  # 0 to 41
  'dnbdou':['n_show','Number of showers reported in the property'],  # 0 to 44
  'dnblav':['n_sink','Number of sinks reported in the property'],  # 0 to 90
  'dnbwc':['n_wc','Number of toilets reported in the property'], # 0 to 51
  'dnbppr':['n_room','Number of mains rooms reported in the property'], # 0 to 99 - loi carrez - no kitchen and bathroom ? 
  'dnbsam':['n_eatr','Number of eating rooms reported in the property'], # 0 to 99
  'dnbcha':['n_slr','Number of sleeping rooms reported in the property'], # 0 to 99
  'dnbcu8':['n_kit8','Number of kitchens reported in the property with an area of less than 8 square meters'],  # 0 to 90
  'dnbcu9':['n_kit9','Number of kitchens reported in the property with an area of larger than 9 square meters'],# 0 to 90
  'dnbsea':['n_washr','Number of washing rooms reported in the property'],  # 0 to 99
  'dnbann':['n_annex','Number of annexes reported in the property'], # 0 to 99
  'dnbpdc':['n_rooms','Number of rooms reported in the property '], # 0 to 99
  'dsupdc':['farea','Reported floor area of the property'], # 15 to 1915
  'geaulc':['water',''], # 0 to 2 ## 2 and more ?  pas une indicatrice ?
  'gelelc':['elec',''], # 0 to 2 ## 2 and more ?  pas une indicatrice ?
  'gesclc':['stair',''], # 0 to 2 ## 2 and more ?  
  'ggazlc':['gas',''], # 0 to 2 ## 2 and more ?  pas une indicatrice ?
  'gasclc':['elevator',''], # 0 to 2 ## 2 and more ? 
  'gchclc':['gteglc',''], # 0 to 2 ## 2 and more ? 
  'gvorlc':['gteglc',''], # 0 to 2 ## 2 and more ? 
  'gteglc':['gteglc',''], # 0 to 2 ## 2 and more ? 
  'dniv':['nth_floor','Reported floor of the property'], # 0 to 99 ## 99 and more ? 
  'dcntsol':['s_field',''], # 0 to 1684404  
  'dcntagri':['s_field',''], # 0 to 4486113  
  'dcntnat':['s_nat',''], # 0 to 4894480 
  'nb_garages':['n_garage','Number of garages reported in the property'], # 0 to 215
  'nb_piscines':['n_pool','Number of pools reported in the property'], # 0 to 3 ## 3 and more ? 
  'nb_terrasses':['n_terrace','Number of terraces reported in the property'], # 0 to 5 ## 5 and more ? 
  'nb_greniers':['n_attic','Number of attics reported in the property'], # 0 to 13 ## 13 and more ? 
  'nb_caves':['n_basmt','Number of basements reported in the property'], # 0 to 22 ## 22 and more ? 
  'nb_autresdep':['n_otherannex','Number of other annexes reported in the property'],  # 0 to 91 ## 91 and more ? 
  'price_sqm':['price_sqm','Price per square meter of the transaction'],
  'dnivrel':['nth_floor_rel', 'Relative floor of the property (from 0, ground floor, to 1, last floor)']
 }
# %%
res = pd.DataFrame.from_dict(dict_fr_en, orient="index", columns=["name_en", "explanation"]
    ).reset_index(names='name_fr').sort("name_en")

res[' '] = range(1, res.shape[0]+1)

with open('temp.txt', 'w') as f: 
    f.write(res[[" ", "name_en", "explanation"]].to_markdown(index=False))

# %%
