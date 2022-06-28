import json, requests
from datetime import datetime
import pandas as pd


def saved_to_html(adr, fname=None):
    
    if fname is None:
        fname = adr + 'saved.html'
    
    adr = adr + 'saved/'

    with open(adr+'saved_posts.json', 'r') as f:
        content = f.read()
        
    dc = json.loads(content)


    ls = [i['string_map_data']['Shared By'] for i in dc['saved_saved_media']]

    href = [i['href'] for i in ls]
    user = [i['value'] for i in ls]
    time = [datetime.fromtimestamp(i['timestamp']) for i in ls]

    sv = pd.DataFrame({'href':href, 'user':user, 'time':time})
    sv.sort_values('time', inplace=True)

    cnt = sv['user'].value_counts().to_frame().reset_index()
    cnt.columns = ['user', 'count']

    df = pd.merge(sv, cnt, how='left', on='user')

    df = df[['time', 'user', 'count', 'href']]

    df.to_html(fname, render_links=True)

    
def search_user(username):
    url = f'https://www.instagram.com/web/search/topsearch/?query={username}'
    r = requests.get(url).text
    dc = json.loads(r)
    ls = []
    new_dc = {}
    for i in dc['users']:
        new_dc['username'] = i['user']['username']
        new_dc['pk'] = i['user']['pk']
        new_dc['is_private'] = i['user']['is_private']
        ls.append(new_dc)
    return ls


def user_to_id(username):
    ls = search_user(username)
    if len(ls)>0:
        the_id = ls[0]['pk']
    else:
        the_id = None
    return the_id
