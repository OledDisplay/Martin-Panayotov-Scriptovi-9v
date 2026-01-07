
import sys

class OnlineShopAccount:
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance
        self.boughtitems = {}
    def add_funds(self, amount):
        self.balance += amount
    def buyitem(self, name, price):
        if(self.balance >= price ):
           self.balance -= price
           print(f"Bought {name} for {price}")
           self.boughtitems[name] = price
        else:
            print("Balance bad")
    def refund(self, name):
        if "car" in self.boughtitems:
            self.balance += self.boughtitems.pop(name)
            print(f"Refunded purchase of {name}")
        else:
            print("no such item purchased")
        
    def show_balance(self):
        print(f"Balance: {self.balance}")

def useOnlineShopAccount():
    User = OnlineShopAccount("Goshi", 20)
    User.add_funds(30)
    User.show_balance()
    User.buyitem("car", 20)
    User.show_balance()
    User.refund("car")
    User.show_balance()

class Player:
    maxhp = 100
    maxenergy = 100
    attack_power = 10

    def __init__(self, name, hp, energy):
        self.name = name
        self.hp = hp
        self.energy = energy
    
    def attack(self):
        if self.energy >= self.attack_power:
            self.energy -= self.attack_power
            print("Attacked!")
        else:
            print("Too tired!")
    def takedamage(self, amount):
        if(self.hp > amount):
            self.hp -= amount
            print(f"Took {amount} points of damage")
        else:
            print("died :(")
            sys.exit()
    def heal(self, amount):
            self.hp += amount
            if self.hp > self.maxhp:
                self.hp = self.maxhp
    


if "__main__":
    useOnlineShopAccount()
 