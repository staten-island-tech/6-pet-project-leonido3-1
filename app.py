import random
class cat:
    def __init__(self, pname, hp, happy, smart, stamina):
        self.name = pname
        self.hp = hp
        self.happy = happy
        self.smart = smart
        self.stamina = stamina
    def study(self, happy, smart, stamina):
        self.smart += smart
        self.happy += happy
        self.stamina -= stamina
    def play(self, happy, stamina):
        if game == "poker":
            print(f"You play poker with {self.name}.")
            wager = int(input("Enter a wager: "))
            pwin = (100-self.smart)*0.01
            numpoker = random.random()
            if numpoker > pwin:
                print(f"You won! You got ${wager*2}, good job.")
                person.money += wager
                print(f"However, {self.name} is unhappy that he lost the game :( ")
                self.happy -= happy
                self.stamina -= stamina
            else:
                print(f"You lost! You gave up ${wager}... how do you even lose to a cat? Well, at least he's happy he won.")
                person.money -= wager
                self.happy += happy*2
                self.stamina -= stamina
        else:
            print(f"You play {game} with {self.name}. He got a little tired, but he is much happier now!")
            self.happy += happy
            self.stamina -= stamina
    def yummy(self, happy, stamina, hp):
        self.happy += happy
        self.stamina += stamina
        self.hp += hp
    def gaming(self, happy, stamina, smart):
        self.smart -= smart
        self.happy += happy
        self.stamina -= stamina
class player:
    def __init__(user, uname, money, inv):
        user.uname = uname
        user.money = money
        user.inv = inv
    def daytrade(user, money):
        gowork = input("Do you want to trade stocks? (y/n)")
        if gowork == "y":
            if pet.smart >= 100:
                user.money = money + 0.15*money*pet.smart
                print(f"Your cat uses its psychic powers to look into the future and tells you what stocks you should buy. You now have ${user.money}")
            elif pet.smart >= 75:
                user.money = money + 0.12*money*pet.smart
                print(f"Your cat bribes politicians to tell you the best insider information. You now have ${user.money}.")
            elif pet.smart >= 50:
                user.money = money + 0.10*money*pet.smart
                print(f"Your cat codes an algorithm to determine what you should buy. You now have ${user.money}.")
            elif pet.smart >= 25:
                user.money = money + 0.08*money*pet.smart
                print(f"Your cat is smart enough to look up a day trading guide on the internet and tell you what stocks you should buy. You now have ${money}.")
    def minimumwage(user, money):
        user.money = money + 7.25*6
        print(f"You go work at McDonalds for minimum wage for 6 hours. You now have ${user.money}.")
    def buyfood(user, inv):
        gostore = input("Do you want to go to the store? (y/n)")
        shopping = True
        while shopping:
            countfood = 0
            if gostore == "y":
                choosefood = int(input(
                     f"You have {inv[0]['count']} gourmet food, {inv[1]['count']} smartening food, and {inv[2]['count']} normal food."
                     " You can buy the following foods: Gourmet ($10/serving), "+
                     "Smartening ($15/serving), "+
                     "Normal ($5/serving), "+
                     "      Choose (1/2/3): "
                                    ))
                countfood = int(input(f"How much {inv[choosefood-1]['type']} food do you want to buy? "))
                total_cost = countfood * inv[choosefood-1]['price']
                if total_cost > user.money:
                        dontstop = input("You are broke and can't buy that! Try again? (y/n)")
                        if dontstop == "n":
                            shopping = False
                else:
                    inv[choosefood-1]['count'] += countfood
                    user.money -= total_cost
                    print(f"Good job. You aren't broke and can buy that. Your balance is ${user.money}.")
                    break
games = ["fortnite", "fetch", "among us", "tag", "poker", "hide and seek"]
stuff = [
    {
        "type": "gourmet",
        "count": 0,
        "price": 10,
    },
    {
        "type": "smartening",
        "count": 0,
        "price": 15,
    },
    {
        "type": "normal",
        "count": 2,
        "price": 5
    }
]
uname = input("What's your name? ")
pname = input("Name your pet. ")
pet = cat(pname, 100, 50, 0, 50)
person = player(uname, 100, stuff)
petnotonfarm = True
game = games[random.randint(0, 5)]
pet.play(pet.happy, pet.stamina)