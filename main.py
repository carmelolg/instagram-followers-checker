import os
from service.Checker import get_mutual_followers, get_unfollowers

# Percorsi dei file
base_dir = os.path.join(os.path.dirname(__file__), 'metadata')
following_path = os.path.join(base_dir, 'following.json')
followers_path = os.path.join(base_dir, 'followers_1.json')

# Chiamata delle funzioni
mutual = get_mutual_followers(following_path, followers_path)
unfollowers = get_unfollowers(following_path, followers_path)

print("Mutual followers: ", len(mutual))
#for item in mutual:
#    print(item)

print("\nUnfollowers: ", len(unfollowers))
for item in unfollowers:
    print(item)