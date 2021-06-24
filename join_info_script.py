import json

with open('scrapyTest/drugs_detail.json', 'r', encoding='utf-8') as drugs_file:
    drugs_file = json.loads(drugs_file.read())

# print(type(drugs_file[0]))

with open('insurances/tamin.json', 'r', encoding='utf-8') as tamin_file:
    tamin_file = json.loads(tamin_file.read())

# print(tamin_file[0]['GeneralCode'])
# print(tamin_file[0]['MinPrice'])
# print(tamin_file[0]['MaxPrice'])


with open('insurances/salamat.json', 'r', encoding='utf-8') as salamat_file:
    salamat_file = json.loads(salamat_file.read())

# print(salamat_file[0]['GeneralCode'])
# print(salamat_file[0]['MinPrice'])
# print(salamat_file[0]['MaxPrice'])

with open('insurances/niro_mosalah.json', 'r', encoding='utf-8') as niro_mosalah_file:
    niro_mosalah_file = json.loads(niro_mosalah_file.read())

# print(niro_mosalah_[0]['GeneralCode'])
# print(niro_mosalah_[0]['MinPrice'])
# print(niro_mosalah_[0]['MaxPrice'])

for i, drug in enumerate(drugs_file):
    try:
        temp = drugs_file[i]['price']
        if temp == '':
            temp = 0

        drugs_file[i]['price'] = []

        for j, tamin_drug in enumerate(tamin_file):
            if tamin_file[j]['GeneralCode'] == drugs_file[i]['generic_code']:
                # print(tamin_file[i]['MinPrice'])
                temp_dict = {
                    'insurance': 'tamin',
                    'MinPrice': tamin_file[i]['MinPrice'],
                    'MaxPrice': tamin_file[i]['MaxPrice']
                }
                # temp_dict = {'test': 'test'}
                drugs_file[i]['price'].append(temp_dict)
        for z, salamat_drug in enumerate(salamat_file):
            if salamat_file[z]['GeneralCode'] == drugs_file[i]['generic_code']:
                temp_dict = {
                    'insurance': 'salamat',
                    'MinPrice': salamat_file[i]['MinPrice'],
                    'MaxPrice': salamat_file[i]['MaxPrice']
                }
                drugs_file[i]['price'].append(temp_dict)

        for y, niro_mosalah_drug in enumerate(niro_mosalah_file):
            if niro_mosalah_file[y]['GeneralCode'] == drugs_file[i]['generic_code']:
                temp_dict = {
                    'insurance': 'niro_mosalah',
                    'MinPrice': niro_mosalah_file[i]['MinPrice'],
                    'MaxPrice': niro_mosalah_file[i]['MaxPrice']
                }
                drugs_file[i]['price'].append(temp_dict)

        if len(drugs_file[i]['price']) == 0:
            drugs_file[i]['price'].append(int(temp))

        # print(drugs_file[i]['price'])
        # print(drugs_file[i]['generic_code'])
    except:
        pass

# print(drugs_file[0])
with open(file='drug_complete_data.json', mode='w', encoding='utf-8') as file:
    file.write(json.dumps(drugs_file, ensure_ascii=False))
