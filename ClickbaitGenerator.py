import random

objectPronouns = ["Her", "Him", "Them"]  # Объектные местоимения
possesivePronouns = ["Her", "His", "Their"]  # Притяжательные местоимения
personalPronouns = ["She", "He", "They"]  # Личные местоимения
countries = ["Russia", "USA", "Germany", "Japan", "China", "England", "Korea"]  # Страна где что то произошло
persons = ["Clown", "Crazy scientist", "Student", "Serial maniac", "Mercenary", "Mom with child", "Doctor", "Parent",
           "Alcoholic", "Athlete", "Cat", "Dog", "Telephone Psychic"]  # Персона, которая выполняла определенные действия
things = ["Ancient ruins", "UFO ship", "USSR submarine", "Coin", "Legacy of China Emperor", "Nothing", "Bigfoot",
          "Nine-tail Fox", "Mummy", "Avocado", "Coffee", "Robot", "Leviathan", "Granddad pills"]
places = ["Bank", "Street", "Laboratory", "School", "Institute", "House", "Donuts shop", "Bunker", "Aqua park",
          "Park"]  # Место действия


# ГЕНЕРАЦИЯ ОБЪЕКТОВ
def returnRandomCountry(countriesObjects: [str]) -> str:
    return random.choice(countriesObjects)


def returnRandomPlace(placesObjects: [str]) -> str:
    return random.choice(placesObjects)


def returnRandomPerson(personsObjects: [str]) -> str:
    return random.choice(personsObjects)


def returnRandonThing(thingsObjects: [str]) -> str:
    return random.choice(thingsObjects)


# ГЕНЕРАЦИЯ ЗАГОЛОВКОВ
def generateGiftHeadline():
    randomNumber = random.randint(4, 15)

    return "{} best gift's ideas for {} from {}!".format(randomNumber, returnRandomPerson(persons), returnRandomPerson(persons))


def generateYouCantBelieveHeadline():
    randomInteger = random.randint(1, 2)
    if randomInteger == 1:
        randomPlace = returnRandomCountry(countries)
    else:
        randomPlace = returnRandomPlace(places)

    return "You won't to believe! {} was found by {} in {} area!".format(returnRandonThing(things), returnRandomPerson(persons), randomPlace)


def generateWhatDoYouWantToKnowHeadline():
    randomThing = ''
    randomNumber = random.randint(1, 2)

    if randomNumber == 1:
        randomThing = returnRandonThing(things)
    elif randomNumber == 2:
        randomThing = random.choice(persons)

    return "What {} don't won't to know about {}?!".format(returnRandomPerson(persons), randomThing)


def generateReasonsWhyInterestingHeadline():
    randomNumber = random.randint(4, 15)

    return "{} reasons why {} is more interesting than you think!".format(randomNumber, returnRandomPerson(persons))


def generateReasonsWhyYouNeverWantHeadline():
    return "What is the reason, why {} never want to hear about {}?!".format(returnRandomPerson(persons), returnRandomPerson(persons))


def generateBigCompaniesHateHeadline():
    return 'Big Companies Hate {}! See How This {} {} Invented a Cheaper {}'.format(returnRandonThing(things), returnRandomCountry(countries), returnRandomPerson(persons), returnRandonThing(things))


def headerGeneration():
    print('Clickbait Headline Generator')
    headline = ''
    while True:
        print('Enter the number of clickbait headlines to generate:')
        headersCount = input('> ')

        if not headersCount.isdigit():
            print('Please enter a number!')
        else:
            numberOfHeadline = int(headersCount)
            break

    for _ in range(numberOfHeadline):

        randonInteger = random.randint(1, 6)

        if randonInteger == 1:
            headline = generateGiftHeadline()
        elif randonInteger == 2:
            headline = generateYouCantBelieveHeadline()
        elif randonInteger == 3:
            headline = generateWhatDoYouWantToKnowHeadline()
        elif randonInteger == 4:
            headline = generateReasonsWhyInterestingHeadline()
        elif randonInteger == 5:
            headline = generateReasonsWhyYouNeverWantHeadline()
        elif randonInteger == 6:
            headline = generateBigCompaniesHateHeadline()

        print(headline)


headerGeneration()