class Car():
    def __init__(self,model,motor,color):
        self.model = model
        self.motor = motor
        self.color = color
    def About_car(self):
        print ("This car model is" , self.model, "\nMotor power in hp is" , self.motor, "\nCorlor is ", self.color)

class Truck(Car):
    def __init__(self, model, motor, color, carrying_capacity):
        super().__init__(model, motor, color)
        self.carrying_capacity = carrying_capacity

    def About_car(self):
        print ("This truck model is ", self.model, "\nMotor power in hp is" , self.motor , "\nColor is ", self.color , "\nCarrying capacity in kg" ,self.carrying_capacity)

class Pick_up(Car):
    def __init__(self, model, motor, color,carrying_capacity):
        super().__init__(model, motor, color)
        self.carrying_capacity = carrying_capacity
    def About_car(self):
        print ("This pick up model is ", self.model, "\nMotor power in hp is ", self.motor, "\n Color is ", self.color, "\Carrying capacity in kg is ", self.carrying_capacity )

class Sedan(Car):
    def __init__(self, model, motor, color):
        super().__init__(model, motor,color)

    def About_car(self):
        print ("This sedan is ", self.model,"\nMotor power in hp is", self.motor,"\nColor is", self.color)