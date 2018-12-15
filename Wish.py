class Wish:
#value cant be smaller than savings. i should check this!
    def __init__(self, id, description, value, savings = None):
        self.id = id
        self.value = value
        self.description = description
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

    def __str__(self):
        id = str(self.id)
        desc = str(self.description)
        value = str(self.value)
        savings = str(self.savings)
        return "[ id: " + id + " | description: " + desc + " | value: " + value + " | savings: " + savings + " ]"

    __repr__ = __str__