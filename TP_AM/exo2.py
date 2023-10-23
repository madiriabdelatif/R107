jour = int(input("Quel est le jour?"))
heure = int(input("Quel est l'heure?"))
munite = int(input("Quel est la munite?"))
result = (munite + heure * 60 + jour * 24 * 60)

print(result)
