class Wish:

    def __init__(self, value, savings = None):
        self.value = value
        if savings is None:
            self.savings = 0
        else:
            self.savings = savings

    def amount_needed(self):
        return (self.value - self.savings)

    def add_savings(self, amount):
        total = self.savings + amount
        rest = 0
        if total > self.value:
            rest = total - self.value
            self.savings = self.value
            print("value exceeded by " + rest + "euros! Value reached, wish soon will came true!")
        else:
            self.savings = self.savings + amount
        return

    def is_value_reached(self):
        return self.savings == self.value