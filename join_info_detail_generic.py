import json

start_urls = []

link_list = []
with open('scrapyTest/drugs_info.json', 'r', encoding='utf-8') as file:
    drugs_info = json.loads(file.read())

# print(drugs_info)

    for drug in drugs_info:
        drug_url = drug['drug_link']
        link_list.append(drug_url)

# for i, link in enumerate(link_list):
#     # print(link)
#     try:
#         link_list[i] = json.loads(link)
#         start_urls.append(str(link_list[i]['drug_link']))
#         # print(link_list[i]['drug_link'])
#     except:
#         pass