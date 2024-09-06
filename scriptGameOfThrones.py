from random import choice, random


class Character:
    def __init__(self, name, hair, region):
        self.name = name
        self.hair = hair
        self.region = region

# // Targeryans -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
class Targeryan(Character):
    dragons = ['Drogon', 'Rhaegal', 'Viserion', 'Balerion', 'Vermithor', 'Caraxes',
               'Meraxes', 'Syrax', 'Meleys', 'Sunfyre', 'Silverwing', 'Dreamfyre',
               'Tessarion', 'Vhagar']

    def __init__(self, name, hair, region, dragon=None):
        super().__init__(name.title(), hair.title(), region.title())
        self.house = 'Targeryan'
        self.last_n = self.house
        self.dragon = dragon if dragon else choice(Targeryan.dragons)
        if self.name == 'Daenerys' or 'Dany':
            self.dragon = Targeryan.dragons[:3]

        self.insanity = 'Insane' if random() > 0.5 else 'Good'

    def quotes(self):
        pass

# // Bastards -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

class Bastard(Character):
    last_names = {
        'North': 'Snow',
        'Dorne': 'Sand',
        'Riverlands': 'Rivers',
        'Vale': 'Stone',
        'Westerlands': 'Hill',
        'Reach': 'Flowers',
        'Stormlands': 'Storm'
    }
    quotes = {
        'Tyrion': ['cockJoke', 'somethingSmart'],
        'Jon': ['You know nothing, Jon Snow', 'urMahQueen'],
        'Ramsay': 'You’re no longer a Snow. You’re a Bolton',
        'Joffrey': 'Fucking Bastard'
    }

    def __init__(self, name, hair, region):
        super().__init__(name.title(), hair.title(), region.title())
        self.last_n = Bastard.last_names.get(str(self.region.title()))
        if self.name == 'Ramsay':
            self.last_n = 'Bolton'

    def say_quote(self):
        return Bastard.quotes.get(self.name)


# \\ Tests -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

name1 = 'Dany'
hair1 = 'White'
region1 = 'South'

character1 = Character(name1, hair1, region1)
if character1.hair.title() == 'White':
    character1 = Targeryan(character1.name, character1.hair, character1.region)
print(type(character1))

for x in character1.__dict__:
    print(f'{x.title()}: {character1.__dict__[x]}')

print('=*=' * 20)

bastard1 = Bastard('Ramsay', 'black', 'north')
for x in bastard1.__dict__:
    print(f'{x.title()}: {bastard1.__dict__[x]}')

print(bastard1.say_quote())
