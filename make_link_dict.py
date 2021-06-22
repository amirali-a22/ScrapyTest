import json

link_list = []
with open('drug_link.json', 'r', encoding='utf-8') as file:
    for drug in file:
        test = drug.split('\n')
        link_list.append(test[0].replace(',', ''))

for i, link in enumerate(link_list):
    # print(link)
    try:
        link_list[i] = json.loads(link)
    except:
        pass

print(link_list)