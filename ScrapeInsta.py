import instaloader

# GET BASIC INFO:

bot = instaloader.Instaloader()

profile = instaloader.Profile.from_username(bot.context, '')

print(type(profile))

print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers: ", profile.followers)
print("Followees: ", profile.followees)
print("Bio: ", profile.biography,profile.external_url)


# DOWNLOAD ALL POSTS:

profile = instaloader.Profile.from_username(bot.context, '')
posts = profile.get_posts()
for index, post in enumerate(posts, 1):
    bot.download_post(post, target=f"{profile.username}_{index}")