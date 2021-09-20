import time
import random

word_its = '''IT'S'''

word_time = '''                                        TIME'''

word_for = '''                                                                                FOR...'''

title1 = '''   ██╗      █████╗ ██████╗ ██████╗ ██╗   ██╗ ██████╗ ██╗   ██╗███████╗███████╗████████╗'''
title2 = '''   ██║     ██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝'''
title3 = '''   ██║     ███████║██████╔╝██████╔╝ ╚████╔╝ ██║   ██║██║   ██║█████╗  ███████╗   ██║   '''
title4 = '''   ██║     ██╔══██║██╔══██╗██╔══██╗  ╚██╔╝  ██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║   '''
title5 = '''   ███████╗██║  ██║██║  ██║██║  ██║   ██║   ╚██████╔╝╚██████╔╝███████╗███████║   ██║   '''
title6 = '''   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   '''

text1 = '''    Somewhere, in the outer reaches of deep space, a janitor named Larry could count down
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
00100001," Rusty beeped.
    
    "Boy is it ever! I'll head over to the Officer's Quarters and see if they left any
bottles of suds behind in the fridge. That sure was one hell of a party..."

'''

# (Press "Enter" to move Larry to the Officer's Quarters.)

text2 = '''
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
are you doing all the way out here? I thought they closed this wing down before the party."

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

'''

# (Press "Enter" to make Larry raid the mini-fridge.)

text3 = '''
    "Light beer sure hits differently when it isn't yours," posited Larry.

    "You said it, man. The tastiest style of beer is free beer."

    The two shared stories about their time working on moon base CRM-114, all the nonsense
they both had to endure that simply didn't matter in the grand scheme of things, and then
chatted about what Larry's life outside of the agency might look like. Larry wondered if
they even made fishing rods anymore now that all the meat back on Earth was lab-grown, but
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

'''

# (Press "Enter" to make Larry run for cover.)

text4 = '''
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

    "Those bastards must've rewired him or something. I might be able to fix him back
though. Look, I'll hold down the fort here. Just grab what you can and get back here
ASAP!"

    "Got it. I'll be back in a bit!"

    Larry turned to fight, knowing that these three aliens and that old rust bucket were
the only things standing between him and a lifetime of sipping mojitos while lounging
poolside...

'''

text5 = '''
    "Hey assholes!!!", shouted Larry.

    He threw his empty beer bottle at the scouts as hard as he could, hitting the first
alien square in the head. He figured that making the first move couldn't hurt, being that
he could almost taste the mojitos...

'''

text_win = "You won! (Write something longer.)"

text_lose = "Larry retired prematurely. (Write something longer.)"

# Text Printing Functions
def type_print(string):
    for i in string:
        print(i, end = '', flush = True)
        time.sleep(0.0325)

def fast_type_print(string):
    for i in string:
        print(i, end = '', flush = True)
        time.sleep(0.01)

# Parent Character Classes
class Human():
    def __init__(self, health, broom_power, spray_power):
        self.health = health
        self.broom_power = broom_power
        self.spray_power = spray_power

    def alive(self, health):
        self.health = health
        life = True
        if self.health <= 0:
            life = False
        return life

class Alien():
    def __init__(self, health, armor, power):
        self.health = health
        self.armor = armor
        self.power = power

    def alive(self, health):
        self.health = health
        life = True
        if self.health <= 0:
            life = False
        return life

class Robot():
    def __init__(self, battery, power):
        self.battery = battery
        self.power = power

# Child Characters
class Larry(Human):
    def attack_alien1(self, alien1):
        hit = random.randint(1, 4)
        if hit != 2:
            alien1.health -= self.broom_power
            fast_type_print(f"    *** Larry does {self.broom_power} damage to the first alien. ***\n\n")
        else:
            fast_type_print("    *** Larry misses. ***\n\n")

    def attack_alien2(self, alien2):
        hit = random.randint(1, 4)
        if hit != 2:
            alien2.health -= self.broom_power
            fast_type_print(f"    *** Larry does {self.broom_power} damage to the second alien. ***\n\n")
        else:
            fast_type_print("    *** Larry misses. ***\n\n")

    def attack_alien3(self, alien3):
        hit = random.randint(1, 4)
        if hit != 2:
            alien3.health -= self.broom_power
            fast_type_print(f"    *** Larry does {self.broom_power} damage to the third alien. ***\n\n")
        else:
            fast_type_print("    *** Larry misses. ***\n\n")
    
    def spray(self, alien1, alien2, alien3):
        if spray.ammo > 0:
            alien1.armor -= self.spray_power
            alien2.armor -= self.spray_power
            alien3.armor -= self.spray_power
            spray.ammo -= 25
            fast_type_print(f"    *** Larry's various cleaning products reduce each alien's armor by {self.spray_power}. ***\n\n")

    def print_status(self):
        fast_type_print(f"--> Larry has {self.health} health. His broom deals {self.broom_power} damage.\n")

class Dave(Human):
    pass
    # def attack(self, alien1, alien2, alien3):
    #     alien1.health -= self.power
    #     alien2.health -= self.power
    #     alien3.health -= self.power
    #     print(f"Dave does {self.power} damage to the aliens.\n")
    #     if alien1.health <= 0:
    #         fast_type_print("The first alien is dead.\n")
    #     if alien2.health <= 0:
    #         fast_type_print("The second alien is dead.\n")
    #     if alien3.health <= 0:
    #         fast_type_print("The third alien is dead.\n")

    def print_status(self):
        fast_type_print(f"--> Dave is holding {self.health} medpack(s) and {self.power} spray bottle refill(s).\n")

class Alien1(Alien):
    def attack_larry(self, larry):
        if self.health > 0:
            hit = random.randint(1, 3)
            if hit != 2:
                larry.health -= self.power
                fast_type_print(f"    *** The first alien does {self.power} damage to Larry. ***\n\n")
                if larry.health <= 0:
                    type_print(text_lose)
                    print()
                    print()
                    exit()
            else:
                fast_type_print("    *** The first alien misses. ***\n\n")
        else:
            fast_type_print("    *** The first alien is dead. ***\n\n")

    def attack_cart(self, cart):
        cart.cart_life -= 1

    def print_status(self):
        if self.health > 0:
            fast_type_print(f"--> The first alien has {self.health} health, {self.armor} armor, and deals {self.power} damage.\n")
        else:
            fast_type_print("--> The first alien is dead.\n")

class Alien2(Alien):
    def attack_larry(self, larry):
        if self.health > 0:
            hit = random.randint(1, 3)
            if hit != 2:
                larry.health -= self.power
                fast_type_print(f"    *** The second alien does {self.power} damage to Larry. ***\n\n")
                if larry.health <= 0:
                    type_print(text_lose)
                    print()
                    print()
                    exit()
            else:
                fast_type_print("    *** The second alien misses. ***\n\n")
        else:
            fast_type_print("    *** The second alien is dead. ***\n\n")

    def attack_cart(self, cart):
        cart.cart_life -= 1

    def print_status(self):
        if self.health > 0:
            fast_type_print(f"--> The second alien has {self.health} health, {self.armor} armor, and deals {self.power} damage.\n")
        else:
            fast_type_print("--> The second alien is dead.\n")

class Alien3(Alien):
    def attack_larry(self, larry):
        if self.health > 0:
            hit = random.randint(1, 3)
            if hit != 2:
                larry.health -= self.power
                fast_type_print(f"    *** The third alien does {self.power} damage to Larry. ***\n\n")
                if larry.health <= 0:
                    type_print(text_lose)
                    print()
                    print()
                    exit()
            else:
                fast_type_print("    *** The third alien misses. ***\n\n")
        else:
            fast_type_print("    *** The third alien is dead. ***\n\n")

    def attack_cart(self, cart):
        cart.cart_life -= 1

    def print_status(self):
        if self.health > 0:
            fast_type_print(f"--> The third alien has {self.health} health, {self.armor} armor, and deals {self.power} damage.\n")
        else:
            fast_type_print("--> The third alien is dead.\n")

class Rusty(Robot):
    def friendly(self):
        rusty.friendly = False
        return rusty.friendly

    def attack_larry(self, larry):
        if self.battery > 0:
            self.battery -= 5
            hit = random.randint(1, 3)
            if hit != 2:
                larry.health -= self.power
                fast_type_print(f"    *** Rusty does {self.power} damage to Larry. ***\n\n")
                if larry.health <= 0:
                    type_print(text_lose)
                    print()
                    print()
                    exit()
        else:
            fast_type_print(f"    *** Rusty's battery is at 0% and cannot attack. ***\n\n")

    def attack_cart(self, cart):
        if self.battery > 0:
            self.battery -= 5
            cart.cart_life -= 1
            fast_type_print(f"    *** Rusty also does {self.power} damage to Larry's cart. ***\n\n")
        else:
            fast_type_print(f"    *** Rusty's battery is at 0% and cannot attack. ***\n\n")

    def attack_alien1(self, alien1):
        if self.battery > 0:
            self.battery -= 5
            hit = random.randint(1, 4)
            if hit != 2:
                alien1.health -= self.power
                fast_type_print(f"    *** Rusty does {self.power} damage to the first alien. ***\n\n")
            else:
                fast_type_print("    *** Rusty misses. ***\n\n")
        else:
            fast_type_print(f"    *** Rusty's battery is at 0% and cannot attack. ***\n\n")

    def attack_alien2(self, alien2):
        if self.battery > 0:
            self.battery -= 5
            hit = random.randint(1, 4)
            if hit != 2:
                alien2.health -= self.power
                fast_type_print(f"    *** Rusty does {self.power} damage to the first alien. ***\n\n")
            else:
                fast_type_print("    *** Rusty misses. ***\n\n")
        else:
            fast_type_print(f"    *** Rusty's battery is at 0% and cannot attack. ***\n\n")

    def attack_alien3(self, alien3):
        if self.battery > 0:
            self.battery -= 5
            hit = random.randint(1, 4)
            if hit != 2:
                alien3.health -= self.power
                fast_type_print(f"    *** Rusty does {self.power} damage to the first alien. ***\n\n")
            else:
                fast_type_print("    *** Rusty misses. ***\n\n")
        else:
            fast_type_print(f"    *** Rusty's battery is at 0% and cannot attack. ***\n\n")

    def print_status(self):
        if self.battery > 0:
            fast_type_print(f"--> Rusty has {self.battery}% battery and deals {self.power} damage.\n")
        else:
            fast_type_print("--> Rusty needs to be recharged.\n")

# Items
class Medpack():
    def __init__(self, health):
        self.health = health

    def use_medpack(self):
        larry.health += self.health
        fast_type_print(f"    *** Larry's health increases to {larry.health}. ***\n\n")
        fast_type_print(f"    *** In turn, each alien does 1 damage to Larry's cart. ***\n\n")

class Spray_bottle():
    def __init__(self, ammo):
        self.ammo = ammo

    def refill_bottles(self):
        self.ammo = 100
        fast_type_print(f"    *** Dave refills Larry's spray bottles to {self.ammo}%. ***\n\n")
        fast_type_print(f"    *** In turn, each alien does 1 damage to Larry's cart. ***\n\n")
    
    def print_status(self):
        fast_type_print(f"--> Larry's spray bottles are at {spray.ammo}%.\n")

class Battery():
    pass

# Larry's Cart
class Cart():
    def __init__(self, cart_life):
        self.cart_life = cart_life
    
    def print_status(self):
        fast_type_print(f"--> Larry's cart can take {self.cart_life} more hits.\n")

# Main Gameplay Loop
larry = Larry(10, 2, 1)
dave = Dave(10, 1, 0)
alien1 = Alien1(5, 5, 1)
alien2 = Alien2(6, 5, 1)
alien3 = Alien3(6, 5, 1)
rusty = Rusty(100, 1)
cart = Cart(25)
medpack = Medpack(2)
spray = Spray_bottle(100)
rusty_is_friend = False

fast_type_print("""

This game requires a Terminal with a width of at least 92 characters and a height of at 
least 42 lines. If you are experiencing formatting errors, please resize your window now.


""")

dummy_key = input('Press "Enter" to continue.')

time.sleep(0.6)
print()
time.sleep(0.6)
print()
time.sleep(0.6)
print(word_its)
time.sleep(0.6)
print()
time.sleep(0.6)
print(word_time)
time.sleep(0.6)
print()
time.sleep(0.6)
print(word_for)
time.sleep(0.6)
print()
time.sleep(0.6)
print()
time.sleep(0.6)
print(title1)
time.sleep(0.6)
print(title2)
time.sleep(0.6)
print(title3)
time.sleep(0.6)
print(title4)
time.sleep(0.6)
print(title5)
time.sleep(0.6)
print(title6)
time.sleep(0.6)
print()
time.sleep(0.6)
print()
time.sleep(0.6)
type_print(text1)
dummy_key = input('''                 Press "Enter" to move Larry to the Officer\'s Quarters.''')
type_print(text2)
dummy_key = input('''                   Press "Enter" to make Larry raid the mini-fridge.''')
type_print(text3)
dummy_key = input('''                       Press "Enter" to make Larry run for cover.''')
type_print(text4)
dummy_key = input('''                 Press "Enter" to make Larry throw his empty beer bottle.''')
type_print(text5)
type_print("(((***)))---------------------------------------------(((***)))\n\n")

while (alien1.alive(alien1.health) == True or alien2.alive(alien2.health) == True or alien3.alive(alien3.health) == True) and larry.alive(larry.health) == True:
    larry.print_status()
    cart.print_status()
    spray.print_status()
    # dave.print_status()
    alien1.print_status()
    alien2.print_status()
    alien3.print_status()
    rusty.print_status()
    print()
    fast_type_print("\n      (((--- WHAT SHOULD LARRY DO? ---)))\n\n\n")
    fast_type_print("    OFFENSE:\n")
    fast_type_print("    1. Whack the first alien with his broom\n")
    fast_type_print("    2. Whack the second alien with his broom\n")
    fast_type_print("    3. Whack the third alien with his broom\n")
    fast_type_print("    4. Spray the aliens with various cleaning products\n\n")
    fast_type_print("    DEFENSE:\n")
    fast_type_print("    5. Get a medpack from Dave and use it behind his cart\n")
    fast_type_print("    6. Get Dave to refill Larry's spray bottles\n")
    fast_type_print("    7. Send Dave out to grab more supplies\n\n")
    fast_type_print("    MISC:\n")
    fast_type_print("    8. Attempt to rewire Rusty back to being friendly\n")
    fast_type_print("    9. Have Dave swap out Rusty's battery\n")
    fast_type_print("    10. Surrender\n\n")
    user_input = input("Enter a number: ")
    print()
    if user_input == "1":
        larry.attack_alien1(alien1)
        alien1.attack_larry(larry)
        alien2.attack_larry(larry)
        alien3.attack_larry(larry)
        if rusty_is_friend == False:
            rusty.attack_larry(larry)
        else:
            rusty.attack_alien1(alien1)
    elif user_input == "2":
        larry.attack_alien2(alien2)
        alien1.attack_larry(larry)
        alien2.attack_larry(larry)
        alien3.attack_larry(larry)
        if rusty_is_friend == False:
            rusty.attack_larry(larry)
        else:
            rusty.attack_alien2(alien2)
    elif user_input == "3":
        larry.attack_alien3(alien3)
        alien1.attack_larry(larry)
        alien2.attack_larry(larry)
        alien3.attack_larry(larry)
        if rusty_is_friend == False:
            rusty.attack_larry(larry)
        else:
            rusty.attack_alien3(alien3)
    elif user_input == "4":
        larry.spray(alien1, alien2, alien3)
        alien1.attack_larry(larry)
        alien2.attack_larry(larry)
        alien3.attack_larry(larry)
        if rusty_is_friend == False:
            rusty.attack_larry(larry)
        else:
            pass
    elif user_input == "5":
        medpack.use_medpack()
        alien1.attack_cart(cart)
        alien2.attack_cart(cart)
        alien3.attack_cart(cart)
        if rusty_is_friend == False:
            rusty.attack_cart(cart)
        else:
            pass
    elif user_input == "6":
        spray.refill_bottles()
        alien1.attack_cart(cart)
        alien2.attack_cart(cart)
        alien3.attack_cart(cart)
        if rusty_is_friend == False:
            rusty.attack_cart(cart)
        else:
            pass
    elif user_input == "7":
        # Send Dave out for supplies (code)
        alien1.attack_cart(cart)
        alien2.attack_cart(cart)
        alien3.attack_cart(cart)
        if rusty_is_friend == False:
            rusty.attack_cart(cart)
        else:
            pass
    elif user_input == "8":
        if rusty.battery > 0 and rusty_is_friend == False:
            rusty.attack_larry(larry)
        elif rusty_is_friend == False:
            rusty_is_friend = True
            fast_type_print('    *** Larry did it! "Trusty Rusty" is back on his side! ***\n\n')
        else:
            fast_type_print("    *** Rusty is already on your side. Choose again. ***\n\n")
    elif user_input == "9":
        if rusty_is_friend == True:
            rusty.battery = 100
            fast_type_print(f"    *** Rusty is back to {rusty.battery}% battery power! ***\n\n")
            alien1.attack_cart(cart)
            alien2.attack_cart(cart)
            alien3.attack_cart(cart)
            fast_type_print(f"    *** In turn, each alien does 1 damage to Larry's cart. ***\n\n")
        else:
            fast_type_print("    *** Rusty is still an ememy. Choose again. ***\n\n")
    elif user_input == "10":
        fast_type_print("    *** Never give up! Never surrender! ***\n\n")
    else:
        fast_type_print(f"Invalid input: {user_input}\n\n")
    fast_type_print("(((***)))---------------- END OF TURN ----------------(((***)))\n")
    print()

type_print(text_win)
print()
print()