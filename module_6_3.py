import random as r

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self.cords = [0,0,0]
        self.speed = speed

    def move(self, dx, dy, dz):
        dx = dx * self.speed
        dy = dy * self.speed
        dz = dz * self.speed
        self.cords[0] += dx
        self.cords[1] += dy
        if self.cords[2] + dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            self.cords[2] += dz

    def get_cords(self):
        print(f'X: {self.cords[0]}, Y: {self.cords[1]}, Z: {self.cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful")
        else:
            print("Be careful, i'm attacking you O_O")

    def speak(self):
        print(f"{self.sound}")

class Bird(Animal):
    beak = True

    def __init__(self, speed):
        super().__init__(speed)

    def lay_eggs(self):
        print(f"Here are(is) {r.randint(1, 4)} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def __init__(self, speed):
        super().__init__(speed)

    def dive_in(self, dz):
        dz = abs(dz) * self.speed / 2
        self.cords[2] -= dz

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

    def __init__(self, speed):
        super().__init__(speed)
        self.sound = "Click-click-click"


class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    
    def __init__(self, speed):
        super().__init__(speed)
    
db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()