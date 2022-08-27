import json
import pandas as pd
from datetime import datetime


def saved_posts(adr):
    with open(adr+'saved/saved_posts.json', 'r') as f:
        content = f.read()
    dc = json.loads(content)
    ls = dc['saved_saved_media']
    data = [i['string_map_data']['Shared By'] for i in ls]
    df = pd.DataFrame(data)
    df.columns = ['href', 'user', 'time']
    df['href'] = df['href'].str[26:]
    df['time'] = df['time'].apply(lambda x: datetime.fromtimestamp(x))
    df = df.sort_values('time')
    df.set_index('time', inplace=True)
    return df


def login_activity(adr):
    with open(adr+'login_and_account_creation/login_activity.json', 'r') as f:
        content = f.read()
    ls = json.loads(content)['account_history_login_history']
    ip = [i['string_map_data']['IP Address']['value'] for i in ls]
    user_agent = [i['string_map_data']['User Agent']['value'] for i in ls]
    timestamp = [i['string_map_data']['Time']['timestamp'] for i in ls]
    t = [datetime.fromtimestamp(i) for i in timestamp]
    df = pd.DataFrame({'time':t, 'ip':ip, 'user_agent':user_agent})
    df = df.sort_values('time')
    df.set_index('time', inplace=True)
    return df


def account_privacy_changes(adr):
    with open(adr+'login_and_account_creation/account_privacy_changes.json', 'r') as f:
        content = f.read()
    ls = json.loads(content)['account_history_account_privacy_history']
    title = [i['title'] for i in ls]
    timestamp = [i['string_map_data']['Time']['timestamp'] for i in ls]
    time = [datetime.fromtimestamp(i) for i in timestamp]
    df = pd.DataFrame({'time':time, 'title':title})
    df = df.sort_values('time')
    df.set_index('time', inplace=True)
    return df


def comments(adr):
    with open(adr+'comments/post_comments.json', 'r') as f:
        content = f.read()
    ls = json.loads(content)['comments_media_comments']   
    text = [i['string_map_data']['Comment']['value'] for i in ls]
    text = [i.encode('raw_unicode_escape').decode('utf-8') for i in text]
    timestamp = [i['string_map_data']['Comment creation time']['timestamp'] for i in ls]
    is_deleted = [i['string_map_data']['Deletion status']['value'] for i in ls]
    del_time = [i['string_map_data']['Deletion status']['timestamp'] for i in ls]
    user = [i['string_map_data']['Media owner']['value'] for i in ls]
    time = [datetime.fromtimestamp(i) for i in timestamp]
    df = pd.DataFrame({'time':time, 'user':user, 'text':text,
                       'is_deleted':is_deleted, 'del_time':del_time})
    if (df['is_deleted']=='False').sum()==len(df):
        del df['is_deleted']
        del df['del_time']
    df = df.sort_values('time')
    df.set_index('time', inplace=True)
    return df
