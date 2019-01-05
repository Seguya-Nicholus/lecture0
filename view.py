class Robot():
    def __init__(self, name=None):
        self.name = name

    def say_hi(self):
        if self.name:
            print("Hi Iam not a Robot ,my name is " + self.name)
        else:
            print("I am a Robot")

x = Robot()
x.say_hi()
y = Robot("Nicholus")
y.say_hi()