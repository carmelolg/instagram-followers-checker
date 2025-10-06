import json

def _get_mutual_followers(following_path, followers_path):
    # Carica i dati dei seguiti
    with open(following_path, 'r', encoding='utf-8') as f:
        following_data = json.load(f)
    following_usernames = {item['title'] for item in following_data['relationships_following']}

    # Carica i dati dei follower
    with open(followers_path, 'r', encoding='utf-8') as f:
        followers_data = json.load(f)
    followers_usernames = {entry['string_list_data'][0]['value'] for entry in followers_data if entry['string_list_data']}

    # Trova gli username presenti in entrambe le liste
    mutual = following_usernames & followers_usernames
    return list(mutual)

def _get_unfollowers(following_path, followers_path):
    # Carica i dati dei seguiti
    with open(following_path, 'r', encoding='utf-8') as f:
        following_data = json.load(f)
    following_usernames = {item['title'] for item in following_data['relationships_following']}

    # Carica i dati dei follower
    with open(followers_path, 'r', encoding='utf-8') as f:
        followers_data = json.load(f)
    followers_usernames = {entry['string_list_data'][0]['value'] for entry in followers_data if entry['string_list_data']}

    # Trova chi segui ma non ti segue
    unfollowers = following_usernames - followers_usernames
    return list(unfollowers)


def get_mutual_followers(following_path, followers_path):
    with open(following_path, 'r', encoding='utf-8') as f:
        following_data = json.load(f)
    following_map = {item['title']: item['string_list_data'][0]['href'] for item in following_data['relationships_following']}

    with open(followers_path, 'r', encoding='utf-8') as f:
        followers_data = json.load(f)
    followers_usernames = {entry['string_list_data'][0]['value'] for entry in followers_data if entry['string_list_data']}

    mutual = followers_usernames & set(following_map.keys())
    return [{'username': u, 'href': following_map[u]} for u in mutual]

def get_unfollowers(following_path, followers_path):
    with open(following_path, 'r', encoding='utf-8') as f:
        following_data = json.load(f)
    following_map = {item['title']: item['string_list_data'][0]['href'] for item in following_data['relationships_following']}

    with open(followers_path, 'r', encoding='utf-8') as f:
        followers_data = json.load(f)
    followers_usernames = {entry['string_list_data'][0]['value'] for entry in followers_data if entry['string_list_data']}

    unfollowers = set(following_map.keys()) - followers_usernames
    return [{'username': u, 'href': following_map[u]} for u in unfollowers]