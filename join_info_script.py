import json
import re

drug_list = []
with open('scrapyTest/drugs_info.json', 'r', encoding='utf-8') as file:
    for drug in file:
        test = drug.split('\n')
        drug_list.append(test[0][:-1])

for i, link in enumerate(drug_list):
    # print(link)
    try:
        drug_list[i] = json.loads(link)
    except:
        pass
drug_list.pop(0)
drug_list.pop(len(drug_list) - 1)

tamin_data_list = []
with open('insurances/tamin.json', 'r', encoding='utf-8') as file:
    file = file.read()[1:-1].replace('},', '},\n').split('\n')
    for drug in file:
        try:
            tamin_data_list.append(json.loads(drug[:-1]))
        except:
            pass

# print(tamin_data_list[0]['GeneralCode'])
# print(tamin_data_list[0]['MinPrice'])
# print(tamin_data_list[0]['MaxPrice'])

salamat_data_list = []
with open('insurances/salamat.json', 'r', encoding='utf-8') as file:
    file = file.read()[1:-1].replace('},', '},\n').split('\n')
    for drug in file:
        try:
            salamat_data_list.append(json.loads(drug[:-1]))
        except:
            pass

# print(salamat_data_list[0]['GeneralCode'])
# print(salamat_data_list[0]['MinPrice'])
# print(salamat_data_list[0]['MaxPrice'])

niro_mosalah_data_list = []
with open('insurances/niro_mosalah.json', 'r', encoding='utf-8') as file:
    file = file.read()[1:-1].replace('},', '},\n').split('\n')
    for drug in file:
        try:
            niro_mosalah_data_list.append(json.loads(drug[:-1]))
        except:
            pass

# print(niro_mosalah_data_list[0]['GeneralCode'])
# print(niro_mosalah_data_list[0]['MinPrice'])
# print(niro_mosalah_data_list[0]['MaxPrice'])

for i, drug in enumerate(drug_list):
    try:
        temp = drug_list[i]['price']
        drug_list[i]['price'] = []
        # print(tamin_data_list[i]['GeneralCode'])
        # print(drug_list[i]['generic_code'])

        for j, tamin_drug in enumerate(tamin_data_list):
            if tamin_data_list[j]['GeneralCode'] == drug_list[i]['generic_code']:
                # print(tamin_data_list[i]['MinPrice'])
                temp_dict = {
                    'insurance': 'tamin',
                    'MinPrice': tamin_data_list[i]['MinPrice'],
                    'MaxPrice': tamin_data_list[i]['MaxPrice']
                }
                # temp_dict = {'test': 'test'}
                drug_list[i]['price'].append(temp_dict)

        for z, salamat_drug in enumerate(salamat_data_list):
            if salamat_data_list[z]['GeneralCode'] == drug_list[i]['generic_code']:
                temp_dict = [{
                    'insurance': 'salamat',
                    'MinPrice': salamat_data_list[i]['MinPrice'],
                    'MaxPrice': salamat_data_list[i]['MaxPrice']
                }]
                drug_list[i]['price'].append(temp_dict)

        for y, niro_mosalah_drug in enumerate(niro_mosalah_data_list):
            if niro_mosalah_data_list[y]['GeneralCode'] == drug_list[i]['generic_code']:
                temp_dict = {
                    'insurance': 'niro_mosalah',
                    'MinPrice': salamat_data_list[i]['MinPrice'],
                    'MaxPrice': salamat_data_list[i]['MaxPrice']
                }
                drug_list[i]['price'].append(temp_dict)

        if len(drug_list[i]['price']) == 0:
            drug_list[i]['price'].append(int(temp))
        # print(drug_list[i]['price'])
        # print(drug_list[i]['generic_code'])
    except:
        pass

with open('drug_complete_data.json', 'a') as file:
    file.write('[')
for n, drug in enumerate(drug_list):
    # try:
    #     with open('drug_complete_data.json') as file:
    #         file.write(drug_list[n])
    with open('drug_complete_data.json', 'a') as file:
        file.write(str(drug_list[n]))
    # except:
    #     pass

with open('drug_complete_data.json', 'a') as file:
    file.write(']')
