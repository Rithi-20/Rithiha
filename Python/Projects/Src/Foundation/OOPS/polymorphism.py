# Same method can be used in different form in different classes this is polymorphism
class animal:
    def sound(self):
        return "Any sound"

class bird:
    def sound(self):
        return "Chirp"

class dog:
    def sound(self):
        return "bark"

s=bird()
print(s.sound())