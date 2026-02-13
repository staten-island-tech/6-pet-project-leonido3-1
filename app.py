import random
uname = input("What's your name? ")
pname = input("Name your pet. ")
if uname == pname:
    print("OF COURSE. OF COURSE THEY ARE THE SAME.")
daysmissed = 0
petalive = True
items_brought = []
stuyboost = 1
basesmart = 5
games = ["fortnite", "fetch", "tag", "poker", "hide and seek"]
day = 0
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
class cat:
    def __init__(self, pname, hp, happy, smart, stamina, fat):
        self.name = pname
        self.hp = hp
        self.happy = happy
        self.smart = smart
        self.stamina = stamina
        self.fat = fat
    def study(self, happy, stamina):
        gain = (basesmart + self.smart*0.15) * stuyboost * (0.6 + self.happy/300 + self.stamina/300)
        self.smart += gain
        self.happy -= happy
        self.stamina -= stamina
        print(f"{self.name} hits the books. He gets pretty tired!")
        print(f"{self.name}'s stamina level decreased to {self.stamina}. His happieness decreased to {self.happy}. His intellect is now {self.smart}.")
    def play(self, happy, stamina, fat):
        if game == "poker":
            poker = True
            while poker:
                print(f"You play poker with {self.name}.")
                wager = int(input(f"Your balance is ${person.money}. Enter a wager: "))
                if wager > person.money:
                    print("Your cat notices you trying to cheat. He then takes half of your money. ")
                    person.money = person.money/2
                    poker = False
                pwin = min(0.75, 0.25 + self.smart*0.002)
                numpoker = random.random()
                if numpoker > pwin:
                    print(f"You won! You got ${wager*2}, good job.")
                    person.money += wager
                    self.happy -= happy
                    poker = False
                    print(f"However, {self.name} is unhappy that he lost the game. {self.name}'s happieness level is now {self.happy}.")
                else:
                    person.money -= wager
                    self.happy += happy*2
                    poker = False
                    print(f"You lost! You gave up ${wager}... how do you even lose to a cat? Well, " +
                        f"at least he's happy he won. {self.name}'s happieness level is now {self.happy}.")
        else:
            self.happy += happy
            self.stamina -= stamina
            self.fat -= fat
            print(f"You play {game} with {self.name}. He got a little tired, but he is much happier now! He also lost a little weight. "+
                  f"{self.name}'s stamina level decreased to {self.stamina}. His happieness increased to {self.happy}. His weight is {self.fat} lbs.")
    def yummy(self, happy, stamina, hp, smart, fat):
        global feedcode
        loop = True
        feedloop = "y"
        if person.inv[0]["count"] != 0 or person.inv[1]["count"] != 0 or person.inv[2]["count"] != 0:
            while loop:
                givefood = input(f"What do you want to feed {self.name}? " +
                                f"You have {person.inv[0]["count"]} gourmet food, {person.inv[1]["count"]} smartening food, and " +
                                f"{person.inv[2]["count"]} normal food. ")
                if givefood == "gourmet":
                    givefood = 1
                    if person.inv[0]["count"] == 0:
                        feedloop = input(f"You don't have enough food! Do you want to feed {self.name} some other food? (y/n)")
                        if feedloop == "n":
                            loop = False
                    else:
                        self.happy += happy*2
                        self.stamina += stamina
                        self.hp += hp*2
                        self.fat += fat*2
                        person.inv[0]["count"] -= 1
                        print(f"You give {self.name} A5 wagyu. You now have {person.inv[0]["count"]} gourmet food. "+
                            f"He enjoyed it and became much happier. {self.name}'s stamina level increased to {self.stamina}. "
                            f"His happieness increased to {self.happy}. His weight increased to {self.fat} lbs.")
                        loop = False
                elif givefood == "smartening":
                    givefood = 2
                    if person.inv[1]["count"] == 0:
                        feedloop = input(f"You don't have enough food! Do you want to feed {self.name} some other food? (y/n)")
                    if feedloop == "n":
                        loop = False
                    else:
                        person.inv[1]["count"] -= 1
                        self.happy -= happy*2
                        self.stamina += stamina
                        self.hp += hp
                        self.smart += smart*2
                        self.fat += fat
                        print(f"You give {self.name} some brain pellets." +
                            f"The food tastes horrible, but at least he's smarter now. You now have {person.inv[1]["count"]} smartening food. " +
                            f"{self.name}'s stamina level increased to {self.stamina}. "
                            f"His happieness decreased to {self.happy}. His intellect increased to {self.smart}. His weight increased to {self.fat} lbs.")
                        loop = False
                elif givefood == "normal":
                    givefood = 3
                    if person.inv[2]["count"] == 0:
                        feedloop = input(f"You don't have enough food! Do you want to feed {self.name} some other food? (y/n)")
                    if feedloop == "n":
                        loop = False
                    else:
                        person.inv[2]["count"] -= 1
                        self.happy += happy
                        self.stamina += stamina
                        self.hp += hp
                        self.fat += fat
                        print(f"You give {self.name} some kibble. You now have {person.inv[2]["count"]} normal food. " 
                            f"{self.name}'s stamina level increased to {self.stamina}. "
                            f"His happieness increased to {self.happy}. His weight is now {self.fat} lbs.")
                        loop = False
                else:
                    if stuff[givefood-1]["count"] == 0:
                        foodtrip = input(f"Would you like to go to the store to buy more food? (y/n) ")
                    if foodtrip == "y":
                        feedcode = True
                        person.buyfood(stuff)
                        feedcode = False
                    feedloop = input(f"You don't have enough food! Do you want to feed {self.name} some other food? (y/n) ") 
                    if feedloop == "n":
                        loop = False    
        else:
            gotostore = input(f"You don't have enough food to feed {self.name}. Would you like to go to the store to buy more? (y/n) ")
            if gotostore == "y":
                person.buyfood(person.inv)
            else:
                keepinter = input(f"Do you want to do something else with {self.name}? (y/n) ")
                if keepinter == "y":
                    petactions()   
                elif keepinter == "n":
                    workfunc()
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
        global basesmart
        if pet.smart >= 500:
            user.money = money + 0.15*money*pet.smart
            basesmart += 12
            pet.stamina -= 20
            print(f"Your cat uses its psychic powers to look into the future and tells you what stocks you should buy. "+
                  f"He got super tired from that, but gained great knowledge in the proccess! You now have ${user.money}. "+
                  f"{pet.name}'s stamina is now {pet.stamina}. ")
        elif pet.smart >= 400:
            user.money = money + 0.12*money*pet.smart
            basesmart += 7
            pet.stamina -= 15
            print(f"Your cat bribes politicians to tell you the best insider information. You now have ${user.money}. "+
                  "This drained his stamina by a lot but made him smarter. "+
                  f"{pet.name}'s stamina is now {pet.stamina}."
                  )
        elif pet.smart >= 250:
            user.money = money + 0.10*money*pet.smart
            basesmart += 3
            pet.stamina -= 10
            print(f"Your cat codes an algorithm to determine what you should buy. "+
                  f"You now have ${user.money}. He got very tired, but he's also a little smarter! "+
                  f"{pet.name}'s stamina is now {pet.stamina}. "
                  )
        elif pet.smart >= 100:
            user.money = money + 0.08*money*pet.smart
            basesmart += 3
            pet.stamina -= 5
            print(f"Your cat is smart enough to look up a day trading guide on the internet and tell you what stocks you should buy. " +
                  f"You now have ${user.money}. He got a little tired, but he's also a little smarter! "+
                  f"{pet.name}'s stamina is now {pet.stamina}. "
                  )
    def minimumwage(user, money):
        user.money = money + 7.25*6
        print(f"You go work at McDonalds for minimum wage for 6 hours. You now have ${user.money}.")
    def buyfood(user, inv):
        shopping = True
        while shopping:
            countfood = 0
            choosefood = input(
            f"You have {inv[0]["count"]} gourmet food, {inv[1]["count"]} smartening food, and {inv[2]["count"]} normal food."
            " You can buy the following foods: gourmet ($10/serving), "+
            "smartening ($15/serving), "+
            "normal ($5/serving), "+
            "Choose: ")
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
                inv[choosefood-1]["count"] = inv[choosefood-1]["count"] + countfood
                user.money -= total_cost
                print(f"Good job. You aren't broke and can buy that. Your balance is ${user.money}.")
                shopping = False
                if storecode == False and feedcode == True:
                    pet.yummy(15, 10, 5, 5, 0.25)
    def storefunc(user):
        global items_brought, stuyboost
        gostore = input(f"Do you want to buy something? Balance: ${person.money} (y/n) ")
        academic_items = [
                {"name": "high school textbooks", 
                "price": 50, 
                "boost": 0.3, 
                "req": 0
                },
                {"name": "college textbooks", 
                "price": 100, 
                "boost": 0.5, 
                "req": 0
                },
                {"name": "PhD dissertation", 
                "price": 1000, 
                "boost": 1.5, 
                "req": 100
                },
                {"name": "ancient tome of knowledge", 
                "price": 3000, 
                "boost": 2.5, 
                "req": 300
                },
        ]
        if gostore == "y":
            global storecode
            shopping = True
            while shopping:
                typestore = input("Would you like to go to the academic store or the food store? ")
                if typestore == "academic":
                    for i in range(4):
                        print(f"{i+1}) You can buy {academic_items[i]["name"]} for {academic_items[i]["price"]}.")
                        print(f"It will boost studying by {academic_items[i]["boost"]}, and requires {academic_items[i]["req"]} intellect.")
                    itemselect = int(input("What would you like to buy? (1/2/3/4) "))
                    if academic_items[itemselect]["price"] <= user.money and pet.smart > academic_items[i]["req"] and academic_items[i]["name"] not in items_brought:
                        user.money -= academic_items[i]["price"]
                        stuyboost += academic_items[i]["boost"]
                        items_brought.append(academic_items[i]["name"])
                        shopping = False
                        print(f"You brought the {academic_items[i]["name"]}. Your balance is now {user.money}.")
                    elif academic_items[i]["name"] in items_brought:
                        print("You already have that boost? ")
                        stop = input("Keep shopping? (y/n) ")
                        if stop == "n":
                            shopping = False
                    elif academic_items[itemselect]["price"] > user.money:
                        print("You're too broke to buy that. ")
                        stop = input("Keep shopping? (y/n) ")
                        if stop == "n":
                            shopping = False
                    elif pet.smart > academic_items[i]["req"]:
                        print(f"{pet.name} is not smart enough to buy that! ")
                        stop = input("Keep shopping? (y/n) ")
                        if stop == "n":
                            shopping = False
                elif typestore == "food":
                    storecode = True
                    user.buyfood(stuff)
                    shopping = False
                    storecode = False
def petactions():
    action = input(f"What would you like to do with {pet.name}? (feed/play/study/ignore) ")
    if action == "feed":
        pet.yummy(15, 10, 5, 5, 0.25)
    elif action == "play":
        pet.play(10, 15, 0.25)
    elif action == "study":
        pet.study(20, basesmart)
    elif action == "ignore":
        pet.ignore(10, 5)
allowwork = True
pet = cat(pname, 100, 30, 0, 30, 7.5)
person = player(uname, 10, stuff)
def workfunc():
    global daysmissed, allowwork
    workaction = input(f"Do you want to go to work or interact more with {pet.name}? (work/interact) ")
    if workaction == "work":
        if pet.smart > 25:
            print()
            worktype = input("Do you want to daytrade or go to work at McDonalds? (1/2) ")
            if worktype == "2":
                if allowwork:
                    person.minimumwage(person.money)
                    pet.happy -= 20
                    print(f"You ignored {pet.name} for your entire shift! YOU MONSTER!! Happieness decreased to {pet.happy}! "
                        f"(hint hint: maybe try increasing {pet.name}'s intelligence to earn more money with his help)")
                else: 
                    print("You can't work, your boss fired you.")
                    changemymindtrading = input("Do you want to go daytrading instead? (y/n)")
                    if changemymindtrading:
                        person.daytrade(person.money)
            elif worktype == "1":
                person.daytrade(person.money)
        elif pet.smart < 25:
            print()
            if allowwork:
                person.minimumwage(person.money)
                pet.happy -= 20
                print(f"You ignored {pet.name} for your entire shift! YOU MONSTER!! Happieness decreased to {pet.happy}! "
                      f"(hint hint: maybe try increasing {pet.name}'s intelligence to earn more money with his help)")
            else: 
                print("You can't work, your boss fired you. ")
    else:
        daysmissed += 1
        print(f"You decide to interact a little more with {pet.name}.")
        print()
        petactions()
        print()
        if daysmissed == 1:
            print(f"Your boss is calling you. He says that you have missed {daysmissed} days of work! "+
            "He says that you have to go to work every day, or you will be fired! (minimum wage option will be disabled)")
        elif daysmissed == 2:
            print(f"Your boss is calling you. He says that you have missed {daysmissed} days of work! "+
            "He says that he is furious and that he is getting close to wanting to fire you!")
        elif daysmissed == 3:
            print(f"Your boss is calling you. He says that you have missed {daysmissed} days of work! "+
            "He says that if you miss even ONE more day of work he will fire you. This is your last straw!")
        elif daysmissed == 4:
            allowwork = False
            print(f"Your boss is calling you. He says that you have missed {daysmissed} days of work! "+
            "Your boss is so mad at you that he has fired you! "+
            "(Minimum wage disabled)")
while petalive:
    game = games[random.randint(0, 4)]
    day += 1
    print()
    print(f"Today is day {day}. {pet.name}'s status is: HP: {pet.hp}, "
          f"Stamina: {pet.stamina}, Happieness: {pet.happy}, Intellect: {pet.smart}. Weight: {pet.fat} lbs.")
    petactions() 
    print()
    workfunc()
    print()
    person.storefunc()
    print()
    print("It's getting late. You should go to sleep.")
    print()
    if pet.happy > 150:
        print(f"GAME OVER! {pet.name} ran a way to a farm because he was too happy! He was in your care for {day} days.")
        break
    if pet.happy < 0:
        print(f"GAME OVER! {pet.name} ran a way to a farm because of your neglect! He was in your care for {day} days.")
        break
    if pet.stamina < 0:
        print(f"GAME OVER! {pet.name} ran a way to a farm because he was too tired! He was in your care for {day} days.")
        break
    if pet.smart < -10:
        print(f"GAME OVER! {pet.name} fell on his head and then ran away to a farm because he was too stupid! He was in your care for {day} days.")
        break
    if pet.hp < 0:
        print(f"GAME OVER! {pet.name} ran a way to a farm because he died (no cats were harmed in the making of this game))! He was in your care for {day} days.") 
        break
    if pet.fat < 5:
        print(f"GAME OVER! {pet.name} ran a way to a farm because he wasn't fed enough! He was in your care for {day} days.") 
        break
    if pet.fat > 15:
        print(f"GAME OVER! {pet.name} ran a way to a farm because he was too fat! He was in your care for {day} days.") 
        break
    if person.money > 100000:
        print(f"You finally won! You and {pet.name} will become billionares together!")
        break