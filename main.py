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

    # print(api.friends_ids('sleepyadamm'))

    j = 1
    for i in api.friends_ids('sleepyadamm'):
        print(i)
        # print(j, "   ", i)
        # j+=1
        # api.destroy_frienship(i)


except:
    print("Error during authentication")