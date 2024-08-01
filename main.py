class Cars:
    brand = "Mahindra"
    model = "XUV"

    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def fun(self):
        print("This is a newly launched car with CNG feature")


car1 = Cars("breezze", "white")
print(car1.brand,car1.model)
print(car1.name, car1.colour)
car1.fun()
