import requests
import json
import os
from collections import OrderedDict

def json_dumper():
    is_empty = os.stat("annapurna_news.json").st_size == 0
    if(is_empty==True):
        with open('annapurna_news.json', 'w') as json_file:
            json.dump(results, json_file, indent=4)

    else:
        with open('annapurna_news.json') as f:
            dict1 = json.load(f)

        dict3 = dict1.copy()
        for key, value in results.items():
            dict3[key] = value
        with open('annapurna_news.json', 'w') as json_file:
            json.dump(dict3, json_file, indent=4)
data = OrderedDict()

page = 0

title = 'कोरोना'
encoded_title = title.encode('utf-8')
# print('encoded title >>', encoded_title)
params = {
  'page': page,
  'title': encoded_title
}
is_empty = os.stat("annapurna_news.json").st_size == 0
if(is_empty==True):
    page = 1
    params["page"]=page
else:
    with open('annapurna_news.json') as f:
        data = json.load(f)
        data_keys_last = list(data.keys())[-1]
        a = int(data_keys_last.split("_")[0])
        page = a+1
        params['page'] = page
print(page)

results = {}
temp_page = page
while(page<=temp_page+2):
    count=0
    try:
        res = requests.get('https://bg.annapurnapost.com/api/search', params=params)
        data = res.json()

        if (res.status_code == 200 and data['status'] == 'success'):
            for d in data['data']['items']:
                count+=1
                results[str(page)+'_'+str(count)]=d
            page = page + 1
            params['page'] = page
            json_dumper()
    except:
        page = page + 1
        params['page'] = page



