# import time
# import random

# class Character():
#     def __init__(self, health, power):
#         self.health = health
#         self.power = power

#     def alive(self):
#         life = True
#         if self.health <= 0:
#             life = False
#         return life

# class Larry(Character):
#     def attack(self, alien1):
#         alien1.health -= self.power
#         print(f"You do {self.power} damage to the alien.")
#         if alien1.health <= 0:
#             print("The alien is dead.")

#     def print_status(self):
#         print(f"You have {self.health} health and {self.power} power.")

# class Dave(Character):
#     def attack(self, alien1):
#         alien1.health -= self.power
#         print(f"You do {self.power} damage to the alien1.")
#         if alien1.health <= 0:
#             print("The first alien is dead.")
#         # if alien2.health 

#     def print_status(self):
#         print(f"Dave has {self.health} health and {self.power} power.")

# class Alien1(Character):
#     def attack(self, larry):
#         larry.health -= self.power
#         print(f"The first alien does {self.power} damage to you.")
#         if larry.health <= 0:
#             print("You are dead.")

#     def print_status(self):
#         print(f"The first alien has {self.health} health and {self.power} power.")

# class Alien2(Character):
#     def attack(self, larry):
#         larry.health -= self.power
#         print(f"The second alien does {self.power} damage to you.")
#         if larry.health <= 0:
#             print("You are dead.")

#     def print_status(self):
#         print(f"The second alien has {self.health} health and {self.power} power.")

# class Alien3(Character):
#     def attack(self, larry):
#         larry.health -= self.power
#         print(f"The third alien does {self.power} damage to you.")
#         if larry.health <= 0:
#             print("You are dead.")

#     def print_status(self):
#         print(f"The third alien has {self.health} health and {self.power} power.")

# class Rusty(Character):
#     def attack(self, larry):
#         larry.health -= self.power
#         print(f"Rusty does {self.power} damage to you.")
#         if larry.health <= 0:
#             print("You are dead.")

#     def print_status(self):
#         print(f"Rusty has {self.health} health and {self.power} power.")

# def print_title1():
#     print('''

# It's time for...


#    ██╗      █████╗ ██████╗ ██████╗ ██╗   ██╗ ██████╗ ██╗   ██╗███████╗███████╗████████╗
#    ██║     ██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝
#    ██║     ███████║██████╔╝██████╔╝ ╚████╔╝ ██║   ██║██║   ██║█████╗  ███████╗   ██║   
#    ██║     ██╔══██║██╔══██╗██╔══██╗  ╚██╔╝  ██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║   
#    ███████╗██║  ██║██║  ██║██║  ██║   ██║   ╚██████╔╝╚██████╔╝███████╗███████║   ██║   
#    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   


#     Somewhere, in the outer reaches of deep space, a janitor named Larry could count down
# the days to retirement on one hand.

#     "It's hard to believe I've got less than a week left," Larry muttered to himself while
# finishing one last mop of the mess hall.
    
#     While he enjoyed having the base almost completely to himself, there was something
# about being this close to the end that made him wonder how things would've turned out if
# he'd made it all the way through The Academy. Still, he had a level of job security most
# folks this far out into space could only dream of. And only a few days of it left to boot.

#     He did have a bit of company though: His robot pal, Rusty. Larry had grown fond of his
# agency-appointed helper, so much so that he even named it. Rusty was definitely outdated,
# but that didn't matter to Larry. He enjoyed the familiarity of "Trusty Rusty" and the robot
# reminded him of a time when things seemed to move a little bit slower. Maintaining an older
# robot also helped pass the time and Larry figured that if his buddy had made it this far,
# he may very well be indestructable.

#     "Well, I guess that's it for the year, Rusty," said Larry.
    
#     "01010100 01101001 01101101 01100101 00100000 01100110 01101111 01110010 00100000 
# 01100001 00100000 01100011 01101111 01101100 01100100 00100000 01101111 01101110 01100101
# 00100001 00100001 00100001," Rusty beeped.
    
#     "Boy is it ever! I'll head over to the Officer's Quarters and see if they left any
# bottles of suds behind in the fridge. That sure was one hell of a party..."

# (Press "Enter" to walk to the Officer's Quarters.)

#     The best part about being the senior janitor was that Larry's keycard granted him full
# access to the entire base. (Another alien1 specimen exploded in the lab you say? "Someone go
# find Larry." Someone puked in the anti-gravity chamber again? "Say no more! Larry's on it!")
# The Officer's Quarters were all the way on the other side of the facility, so Larry headed
# over that way while Rusty stayed behind to straighten up their neck of the woods.

#     As he was making his way down one of the now-dimly-lit corridors, a dark figure in the
# distance startled Larry something fierce.

#     "Hey! Who's that?!?", shouted Larry.

#     "Huh? Oh... It's me, Dave!"

#     Dave was one of the medics at the base and a good friend of Larry's. A welcomed sight,
# for sure.

#     "Terribly sorry about that, bud," said Dave. "They must've turned the lights out to save
# power over the break. I guess I overslept and missed the shuttle. Damn... Well anyway, what
# are you doing all the way out here? I thought they closed this wing down before the party..."

#     "I'm headed over to the Officer's Quarters to see if they left any beers in that mini-
# fridge that they think is a secret."

#     "Yeah, they aren't foolin' anyone... But aren't you worried about them finding out? The
# security cameras are still on and that constitutes as stealing from an officer," Dave noted.

#     "What are they gonna do, fire me?"

#     "Good point, Larry. Let's go find some beers and drink to your retirement."

#     The old pals made their way up the hill and quipped back and forth about how much nicer
# the accomodations were on this side of the base (for agency standards, at least). The outer
# door of the Officer's Quarters proved to be no obstacle for Larry's keycard and the two
# friends paraded around feeling like kings, if only for a short while. The mini-fridge was
# "hidden" right where they knew it was and sure enough, the brewski gods shined bright on 
# Larry and Dave on this particular day.

# (Press "Enter" to take a sip.)

#     "Light beer sure hits differently when it isn't yours," posited Larry.

#     "You said it, man. The tastiest style of beer is free beer."

#     The two shared stories about their time working on moon base CRM-114, all the nonsense
# they both had to endure that simply didn't matter in the grand scheme of things, and then
# chatted about what Larry's life outside of the agency might look like. Larry wondered if
# they even made fishing rods anymore now that all meat back on Earth was lab grown, but
# before he could get that thought out, Dave noticed something through one of the large bay
# windows.

#     "Hold that thought, Larry. A ship just landed in the maintenance dock..."

#     "That's odd. No one's supposed to return until after the New Year. Let's go check and
# see who it is."

#     "Yeah. Let's bolt before anyone finds out what we're up to."

#     The two made haste back to Larry's side of the base, finishing their last sips of oat
# soda along the way. As they get closer to the airlock by the maintenance dock, Larry
# notices that his janitor cart hasn't been properly stowed back in the closet.

#     "Huh... Rusty didn't finish cleaning up for the day," said Larry.

#     "Yeah, that robot's probably nearing the end there. I honestly don't see why you never
# upgraded. But I guess it doesn't really matter now."

#     "This is different. He would never forget to do something this basic. Oh wait... Here
# he comes."

#     "01010000 01010010 01000101 01010000 01000001 01010010 01000101 00100000 01010100 
# 01001111 00100000 01000100 01001001 01000101 00101100 00100000 01001000 01010101 01001101
# 01000001 01001110 01010011 00100001 00100001 00100001," beeped Rusty, much louder than
# before.

#     "Oh, shit! Dave, RUN!!!" Larry yelled, grabbing Dave's arm.

#     "What'd he say?!?"

#     "Just find something to hide behind!"

#     Dave found a corner of the dock that would keep him safe for the moment and Larry dove
# behind the only thing he could find: his janitor cart. Go figure... The one thing that
# symbolized his feeling of being trapped in a dead end job for so many years may actually
# be what saves him after all. He had everything he needed: A broom to use as a weapon, some
# spray bottles of cleaner that might do something, and a mobile shield in the cart itself.

#     As he was taking stock of his surroundings, the real threat made itself known: Alien
# scouts. They must have known about the break and figured that it would be the perfect
# time to try and commandeer the base.

#     "Dave, can you hear me?"

#     "Yeah. What do we do?"

#     "I'm all set here with some weapons to fend them off for a bit. Are there any med
# stations close by?" asked Larry.

#     "Definitely. It'll take me a minute to run and get supplies, but I restocked all of
# them before everyone left. What happened with Rusty?"

#     "Those bastards must've hotwired him or something. I know his weak spots though, so
# I'll take care of things here ."

#     "Got it. I'll be back in a bit!"
# ''')

# def main():
#     larry = Larry(10, 5)
#     dave = Dave(10, 5)
#     alien1 = Alien1(6, 2)
#     alien2 = Alien2(6, 2)
#     alien3 = Alien3(6, 2)
#     rusty = Rusty(100, 1)

#     print_title1()

#     while (alien1.alive() or alien2.alive() or alien3.alive()) and larry.alive():
#         larry.print_status()
#         alien1.print_status()
#         alien2.print_status()
#         alien3.print_status()
#         print()
#         print("What do you want to do?")
#         print("1. Fight an alien")
#         print("2. Do nothing")
#         print("3. Flee")
#         user_input = input("Choice: ")
#         print()
#         if user_input == "1":
#             larry.attack(alien1)
#         elif user_input == "2":
#             pass
#         elif user_input == "3":
#             print("Goodbye.\n")
#             break
#         else:
#             print(f"Invalid input: {user_input}")
#             print()
#         if alien1.health > 0:
#             alien1.attack(larry)

# main()

import time
import random

class Character():
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def alive(self):
        life = True
        if self.health <= 0:
            life = False
        return life

class Larry(Character):
    def attack(self, alien1, alien2, alien3):
        hit = random.randint(1, 5)
        if hit == 1:
            alien_hit = "first"
            alien1.health -= self.power
            print(f"Larry does {self.power} damage to the {alien_hit} alien.")
        elif hit == 2:
            alien2.health -= self.power
            alien_hit = "second"
            print(f"Larry does {self.power} damage to the {alien_hit} alien.")
        elif hit == 3:
            alien3.health -= self.power
            alien_hit = "third"
            print(f"Larry does {self.power} damage to the {alien_hit} alien.")
        else:
            print("Larry missed.")
        if alien1.health <= 0:
            print("The alien is dead.")

    def print_status(self):
        print(f"Larry has {self.health} health and {self.power} power.")

class Dave(Character):
    def attack(self, alien1, alien2, alien3):
        alien1.health -= self.power
        alien2.health -= self.power
        alien3.health -= self.power
        print(f"You do {self.power} damage to the aliens.")
        if alien1.health <= 0:
            print("The first alien is dead.")
        if alien2.health <= 0:
            print("The second alien is dead.")
        if alien3.health <= 0:
            print("The third alien is dead.")

    def print_status(self):
        print(f"Dave has {self.health} health and {self.power} power.")

class Alien1(Character):
    def attack(self, larry):
        larry.health -= self.power
        print(f"The first alien does {self.power} damage to Larry.")
        if larry.health <= 0:
            print("Larry retired prematurely.")

    def print_status(self):
        print(f"The first alien has {self.health} health and {self.power} power.")

class Alien2(Character):
    def attack(self, larry):
        larry.health -= self.power
        print(f"The second alien does {self.power} damage to Larry.")
        if larry.health <= 0:
            print("Larry retired prematurely.")

    def print_status(self):
        print(f"The second alien has {self.health} health and {self.power} power.")

class Alien3(Character):
    def attack(self, larry):
        larry.health -= self.power
        print(f"The third alien does {self.power} damage to Larry.")
        if larry.health <= 0:
            print("Larry retired prematurely.")

    def print_status(self):
        print(f"The third alien has {self.health} health and {self.power} power.")

class Rusty(Character):
    def attack(self, larry):
        larry.health -= self.power
        print(f"Rusty does {self.power} damage to you.")
        if larry.health <= 0:
            print("You are dead.")

    def print_status(self):
        print(f"Rusty has {self.health} health and {self.power} power.")

def print_title1():
    print('''

It's time for...


   ██╗      █████╗ ██████╗ ██████╗ ██╗   ██╗ ██████╗ ██╗   ██╗███████╗███████╗████████╗
   ██║     ██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝
   ██║     ███████║██████╔╝██████╔╝ ╚████╔╝ ██║   ██║██║   ██║█████╗  ███████╗   ██║   
   ██║     ██╔══██║██╔══██╗██╔══██╗  ╚██╔╝  ██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║   
   ███████╗██║  ██║██║  ██║██║  ██║   ██║   ╚██████╔╝╚██████╔╝███████╗███████║   ██║   
   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   


    Somewhere, in the outer reaches of deep space, a janitor named Larry could count down
the days to retirement on one hand.

    "It's hard to believe I've got less than a week left," Larry muttered to himself while
finishing one last mop of the mess hall.
    
    While he enjoyed having the base almost completely to himself, there was something
about being this close to the end that made him wonder how things would've turned out if
he'd made it all the way through The Academy. Still, he had a level of job security most
folks this far out into space could only dream of. And only a few days of it left to boot.

    He did have a bit of company though: His robot pal, Rusty. Larry had grown fond of his
agency-appointed helper, so much so that he even named it. Rusty was definitely outdated,
but that didn't matter to Larry. He enjoyed the familiarity of "Trusty Rusty" and the robot
reminded him of a time when things seemed to move a little bit slower. Maintaining an older
robot also helped pass the time and Larry figured that if his buddy had made it this far,
he may very well be indestructable.

    "Well, I guess that's it for the year, Rusty," said Larry.
    
    "01010100 01101001 01101101 01100101 00100000 01100110 01101111 01110010 00100000 
01100001 00100000 01100011 01101111 01101100 01100100 00100000 01101111 01101110 01100101
00100001 00100001 00100001," Rusty beeped.
    
    "Boy is it ever! I'll head over to the Officer's Quarters and see if they left any
bottles of suds behind in the fridge. That sure was one hell of a party..."

(Press "Enter" to walk to the Officer's Quarters.)

    The best part about being the senior janitor was that Larry's keycard granted him full
access to the entire base. (Another alien specimen exploded in the lab you say? "Someone go
find Larry." Someone puked in the anti-gravity chamber again? "Say no more! Larry's on it!")
The Officer's Quarters were all the way on the other side of the facility, so Larry headed
over that way while Rusty stayed behind to straighten up their neck of the woods.

    As he was making his way down one of the now-dimly-lit corridors, a dark figure in the
distance startled Larry something fierce.

    "Hey! Who's that?!?", shouted Larry.

    "Huh? Oh... It's me, Dave!"

    Dave was one of the medics at the base and a good friend of Larry's. A welcomed sight,
for sure.

    "Terribly sorry about that, bud," said Dave. "They must've turned the lights out to save
power over the break. Damn... I guess I overslept and missed the shuttle. Well anyway, what
are you doing all the way out here? I thought they closed this wing down before the party..."

    "I'm headed over to the Officer's Quarters to see if they left any beers in that mini-
fridge that they think is a secret."

    "Yeah, they aren't foolin' anyone... But aren't you worried about them finding out? The
security cameras are still on and that constitutes as stealing from an officer," Dave noted.

    "What are they gonna do, fire me?"

    "Good point, Larry. Let's go find some beers and drink to your retirement."

    The old pals made their way up the hill and quipped back and forth about how much nicer
the accomodations were on this side of the base (for agency standards, at least). The outer
door of the Officer's Quarters proved to be no obstacle for Larry's keycard and the two
friends paraded around feeling like kings, if only for a short while. The mini-fridge was
"hidden" right where they knew it was and sure enough, the brewski gods shined bright upon 
Larry and Dave on this particular day.

(Press "Enter" to take a sip.)

    "Light beer sure hits differently when it isn't yours," posited Larry.

    "You said it, man. The tastiest style of beer is free beer."

    The two shared stories about their time working on moon base CRM-114, all the nonsense
they both had to endure that simply didn't matter in the grand scheme of things, and then
chatted about what Larry's life outside of the agency might look like. Larry wondered if
they even made fishing rods anymore now that all meat back on Earth was lab-grown, but
before he could get that thought out, Dave noticed something through one of the large bay
windows.

    "Hold that thought, Larry. A ship just landed in the maintenance dock..."

    "That's odd. No one's supposed to return until after the New Year. Let's go check and
see who it is."

    "Yeah. Let's bolt before anyone finds out what we're up to."

    The two made haste back to Larry's side of the base, finishing their last sips of oat
soda along the way. As they got closer to the airlock by the maintenance dock, Larry
noticed that his janitor cart wasn't properly stowed back in the closet.

    "Huh... Rusty didn't finish cleaning up for the day," said Larry.

    "Yeah, that robot's probably nearing the end there. I honestly don't see why you never
upgraded. But I guess it doesn't really matter now."

    "This is different. He would never forget to do something this basic. Oh wait... Here
he comes."

    "01010000 01010010 01000101 01010000 01000001 01010010 01000101 00100000 01010100 
01001111 00100000 01000100 01001001 01000101 00101100 00100000 01001000 01010101 01001101
01000001 01001110 01010011 00100001 00100001 00100001," beeped Rusty, much louder than
before.

    "Oh, shit! Dave, RUN!!!" Larry yelled, grabbing Dave's arm.

    "What'd he say?!?"

    "Just find something to hide behind!"

    Dave found a corner of the dock that would keep him safe for the moment and Larry dove
behind the only thing he could find: his janitor cart. Go figure... The one thing that
symbolized his feeling of being trapped in a dead end job for so many years may actually
be what saved him after all. He had everything he needed: A broom to use as a weapon, some
spray bottles of cleaner that might do something, and a mobile shield in the cart itself.

    As he was taking stock of his surroundings, the real threat made itself known: Alien
scouts. They must have intercepted transmissions talking about the break and figured that
it would be the perfect time to try and commandeer the base.

    "Dave, can you hear me?"

    "Yeah. What do we do?"

    "I'm all set here with some weapons to fend them off for a bit. Are there any med
stations close by?" asked Larry.

    "Definitely. It'll take me a minute to run and get supplies, but I restocked all of
them before everyone left. What happened with Rusty?"

    "Those bastards must've hotwired him or something. I know his weak spots though. Look,
I'll hold down the fort here. Just grab what you can and get back here ASAP!"

    "Got it. I'll be back in a bit!"

    Larry turned to fight, knowing that these three aliens and that old rust bucket were
the only things standing between him and a lifetime of sipping mojitos while lounging
poolside...
''')

larry = Larry(10, 2)
dave = Dave(10, 2)
alien1 = Alien1(6, 1)
alien2 = Alien2(6, 1)
alien3 = Alien3(6, 1)
rusty = Rusty(100, 1)

print_title1()

while (alien1.alive() or alien2.alive() or alien3.alive()) and larry.alive():
    larry.print_status()
    alien1.print_status()
    alien2.print_status()
    alien3.print_status()
    print()
    print("What should Larry do?\n")
    print("1. Fight an alien with his broom")
    print("2. Spray an alien with various cleaning products")
    print("3. Hide behind his cart")
    print("4. Get a medpack from Dave")
    print("5. Flee")
    user_input = int(input("\nChoice: "))
    print()
    if user_input == 1 or user_input == 2:
        larry.attack(alien1, alien2, alien3)
        if alien1.health > 0:
            alien1.attack(larry)
    elif user_input == 3:
        pass
    elif user_input == 5:
        print("Goodbye.\n")
        break
    else:
        print(f"Invalid input: {user_input}")
        print()