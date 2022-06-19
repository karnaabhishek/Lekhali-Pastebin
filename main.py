import requests
import json
import os

def parser():
    title = 'कोरोना'
    encoded_title = title.encode('utf-8')
    # print('encoded title >>', encoded_title)
    params = {
    'page': 1,
    'title': encoded_title
    }

    is_empty = os.stat("annapurna_news.json").st_size == 0
    if(is_empty):
        page = 1
        params["page"]=page
    else:
        with open('annapurna_news.json') as f:
            data = json.load(f)
            # get the keys from dictionary
            data_keys_last = int(list(data.keys())[-1])
            page = data_keys_last + 1
            params['page'] = page
            results = data


    results = {}

    temp_page = page
    while(page<=temp_page+2):
        count=0
        try:
            res = requests.get('https://bg.annapurnapost.com/api/search', params=params)
            data = res.json()

            if (res.status_code == 200 and data['status'] == 'success'):
                results[page] = data['data']['items']
                page = page + 1
                params['page'] = page
                json.dump(results, open('annapurna_news.json', 'w'), indent=4)
            print("Fetching page:", page - 1, 'successfully')
        except Exception as e:
            print(e)


parser()
print("Scraping complete")
