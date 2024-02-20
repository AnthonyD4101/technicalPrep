# Implement the IceCreamMachine's scoops method so that it returns all combinations
# of one ingredient and one topping. If there are no ingredients or toppings, the
# method should return an empty list

# For example, IceCreamMachine (["vanila", "chocolate", ["chocolate sauce"]).scoops()
# should return [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]

class IceCreamMachine:
    
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
        
    def scoops(self):
        return [[ingredient, toppings] for ingredient in self.ingredients for toppings in self.toppings]

if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print(machine.scoops()) #should print: [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]