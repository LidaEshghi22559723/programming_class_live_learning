class Vehicle:
    def __init__(self, companyName, enginHorse, price, color):
        self.companyName = companyName
        self.enginHorse = enginHorse
        self.price = price
        self.color = color

    def printInfo(self):
        print("Company:", self.companyName)
        print("Engine Horsepower:", self.enginHorse)
        print("Price:", self.price)
        print("Color:", self.color)

    def compare(self, other):
        self.printInfo()
        print("___________________________________")
        other.printInfo()


car1 = Vehicle("BMW", 300, 50000, "Black")
car2 = Vehicle("Mercedes", 250, 45000, "White")

car2.compare(car1)