class car(object):
    def __init__(self,color,company,speedlimit):
        self.color = color
        self.company = company
        self.speedlimit = speedlimit

    def start(self):
        print("started")
    
    def stop(self):
        print("match ended")
    
    def accelerate(self):
        print("accelerating")
    
    def changegear(self,geartype):
        print("gear changed")

vlkwagen = car("red","volkwagen","500")
print(vlkwagen.start())
print(vlkwagen.stop())
print(vlkwagen.color)