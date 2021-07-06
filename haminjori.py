import json
import pandas as pd

with open('drug_complete_data_new.json', 'r', encoding='utf-8') as file:
    file = json.loads(file.read())

drug_list = []
counter = 0
for drug in file:
    try:
        if type(drug['price'][0]) == dict:
            print(drug['price'])
            drug_list.append(drug)
            counter += 1
    except:
        pass

print(counter)
print(file[0].keys())

# df = pd.DataFrame(file, columns=file[0].keys())
df = pd.DataFrame(drug_list, columns=file[0].keys())
df.to_csv('drugs_report.csv')
print('done')
