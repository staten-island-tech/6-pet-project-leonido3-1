import random
class cat:
    def __init__(self, pname, hp, happy, smart, stamina):
        self.name = pname
        self.hp = hp
        self.happy = happy
        self.smart = smart
        self.stamina = stamina
    def study(self, happy, smart, stamina):
        print(f"{pname} hits the books. He gets pretty tired!")
        self.smart += smart
        self.happy -= happy
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
                print(f"However, {self.name} is unhappy that he lost the game. {self.name}'s happieness level is now {self.happy}.")
                self.happy -= happy
                self.stamina -= stamina
            else:
                print(f"You lost! You gave up ${wager}... how do you even lose to a cat? Well, " +
                      f"at least he's happy he won. {self.name}'s happieness level is now {self.happy}.")
                person.money -= wager
                self.happy += happy*2
                self.stamina -= stamina
        else:
            print(f"You play {game} with {self.name}. He got a little tired, but he is much happier now!")
            self.happy += happy
            self.stamina -= stamina
    def yummy(self, happy, stamina, hp, smart):
        loop = True
        if person.inv[0]["count"] != 0 or person.inv[1]["count"] != 0 or person.inv[2]["count"] != 0:
            while loop:
                givefood = input(f"What do you want to feed {self.name}? " +
                                f"You have {person.inv[0]["count"]} gourmet food, {person.inv[1]["count"]} smartening food, and " +
                                f"{person.inv[2]["count"]} normal food. ")
                if givefood == "gourmet" and person.inv[0]["count"] != 0:
                    person.inv[0]["count"] -= 1
                    print(f"You give {self.name} some food. You now have {person.inv[0]["count"]} gourmet food. "+
                          f"He enjoyed it and became much happier. {pet.name}'s stamina level increased to {pet.stamina}. His happieness increased to {pet.happy}.")
                    loop = False
                    self.happy += happy*2
                    self.stamina += stamina
                    self.hp += hp*2
                elif person.inv[0]["count"] == 0:
                    feedloop = input(f"You don't have enough food! Do you want to feed {pname} some other food? (y/n)")
                    if feedloop == "n":
                        loop = False
                if givefood == "smartening" and person.inv[1]["count"] != 0:
                    person.inv[1]["count"] -= 1
                    print(f"You give {self.name} some food. The food tastes horrible, but at least he's smarter now. You now have {person.inv[1]["count"]} smartening food. " +
                          f"{pet.name}'s stamina level increased to {pet.stamina}. His happieness increased to {pet.happy}. His intellect increased to {pet.smart}.")
                    loop = False
                    self.happy -= happy*2
                    self.stamina += stamina
                    self.hp += hp
                    self.smart += smart*2
                elif person.inv[1]["count"] == 0:
                    feedloop = input(f"You don't have enough food! Do you want to feed {pname} some other food? (y/n)")
                    if feedloop == "n":
                        loop = False
                if givefood == "normal" and person.inv[2]["count"] != 0:
                    person.inv[2]["count"] -= 1
                    print(f"You give {self.name} some food. You now have {person.inv[2]["count"]} normal food." 
                          f"{pet.name}'s stamina level increased to {pet.stamina}. His happieness increased to {pet.happy}")
                    loop = False
                    self.happy += happy
                    self.stamina += stamina
                    self.hp += hp
                elif person.inv[2]["count"] == 0:
                    feedloop = input(f"You don't have enough food! Do you want to feed {pname} some other food? (y/n)") 
                    if feedloop == "n":
                        loop = False    
        else:
            gotostore = input(f"You don't have enough food to feed {self.name}. Would you like to go to the store? ")
            if gotostore == "y":
                person.buyfood(person.inv)                
    def ignore(self, happy, stamina):
        print(f"You ignore {self.name}, causing his stamina to go down to {self.stamina}, and his happieness to go down to {self.happy}!")
        self.happy -= happy
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
                     f"You have {inv[0]["count"]} gourmet food, {inv[1]["count"]} smartening food, and {inv[2]["count"]} normal food."
                     " You can buy the following foods: gourmet ($10/serving), "+
                     "smartening ($15/serving), "+
                     "normal ($5/serving), "+
                     "      Choose: "
                                    ))
                if choosefood == "gourmet":
                    choosefood = 1
                elif choosefood == "smartening":
                    choosefood = 2
                elif choosefood == "normal":
                    choosefood = 3
                countfood = int(input(f"How much {inv[choosefood-1]["type"]} food do you want to buy? "))
                total_cost = countfood * inv[choosefood-1]['price']
                if total_cost > user.money:
                        dontstop = input("You are broke and can't buy that! Try again? (y/n) ")
                        if dontstop == "n":
                            shopping = False
                else:
                    inv[choosefood-1]["count"] += countfood
                    user.money -= total_cost
                    print(f"Good job. You aren't broke and can buy that. Your balance is ${user.money}.")
                    break
games = ["fortnite", "fetch", "tag", "poker", "hide and seek"]
day = 0
stuff = [
    {
        "type": "gourmet",
        "count": 10,
        "price": 10,
    },
    {
        "type": "smartening",
        "count": 10,
        "price": 15,
    },
    {
        "type": "normal",
        "count": 10,
        "price": 5
    }
]
uname = input("What's your name? ")
pname = input("Name your pet. ")
pet = cat(pname, 100, 50, 0, 50)
person = player(uname, 100, stuff)
petalive = True
while petalive:
    game = games[random.randint(0, 4)]
    day += 1
    print(f"Today is day {day}. {pet.name}'s status is: HP: {pet.hp}, Stamina: {pet.stamina}, Happieness: {pet.happy}, Intellect: {pet.smart}.")
    action = input(f"What would you like to do with {pet.name}? (feed/play/study/ignore) ")
    if action == "feed":
        pet.yummy(15, 10, 5, 5)
    elif action == "play":
        pet.play(10, 15)
    elif action == "study":
        pet.study(10, 5, 15)
    elif action == "ignore":
        pet.study(10, 5, 15)
    workaction = input(f"Do you want to go to work or interact more with {pet.name}? (work/interact) ") 
    if workaction == "work":
        if pet.smart >= 25:
            person.daytrade(person.money)
        else:
            person.minimumwage(person.money)