import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("VkOPxi5RoGq16dJG5CtqDXJKM",
    "Gngak0iL5AToolVKFuWAspWgCsRAyXDBXFNtFyCymC3zms53qf")
auth.set_access_token("573833945-OA00farFXda3Lf1fbzMiOUsfzLkaagekDLvl6xnp",
    "yCetWSP35wPjKbb4FM92iPHGOVN6QbFPUnQEv56a7RVZ3")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")

    # api.update_status("Test tweet from Tweepy Python")

    # user = api.get_user("sleepyadamm")
    # print("User details:")
    # print(user.name)
    # print(user.description)
    # print(user.location)

    # ?? print(api.home_timeline("sleepyadamm"))

except:
    print("Error during authentication")