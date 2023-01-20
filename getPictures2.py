# pip install instaloader

######### PROFILE PHOTO ONLY
# import instaloader
 
# ig = instaloader.Instaloader()
# dp = input("Enter Insta username : ")
 
# ig.download_profile(dp , profile_pic_only=True)

######## ALL VIDEOS AND PHOTOS
from instaloader import Instaloader, Profile

L = Instaloader()
PROFILE = "cervezacamus"
profile = Profile.from_username(L.context, PROFILE)

posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda post: post.likes,reverse=True)

for post in posts_sorted_by_likes:
    L.download_post(post, PROFILE)

