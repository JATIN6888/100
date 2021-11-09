class Car(object):
    def __init__(self,model,color,compny,speed):
        self.color=color
        self.model=model
        self.compny=compny
        self.speed=speed
    def start(self):
        print("started")
        
    def stop(self):
        print("stoped")
a=Car("c6","red","audi",360)
print(a.start())

print(a.compny)
print(a.model)
print(a.speed)
print(a.color)