import random
def whatIsLove(petals):
    ofLove = 0
    everythingNice = 0
    for petal in petals:
        sugarSpice = random.randint(0, len(petals) - 1)
        if ofLove % 2 == 1:
            print("He loves me")
            if ofLove == everythingNice:
                print("First Love Thyself")
                everythingNice += sugarSpice
            ofLove += 1
        elif ofLove % 2 == 0:
            print("He loves me not")
            if ofLove == everythingNice:
                print("First Love Thyself")
                everythingNice += sugarSpice
                print(everythingNice)
            ofLove += 1
whatIsLove("Learning to love thyself")
