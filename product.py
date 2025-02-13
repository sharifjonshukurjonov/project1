class Basket:
    def __init__(self, date):
        self.date = {}

    def add(self, product, price):
        self.date[product] = price

    def remove(self, amount):
        if amount in self.date:
            del self.date[amount]
        else:
            return f"omborda bunday maxsulot yo'q"

    def canculator(self):
        ans = 0
        for i in self.date.values():
            ans += i

        return ans


    def show(self):
        return (f"Ombordagi maxsulotlar\n"
                f"{self.date}")

b = Basket("olma")
print(b.add("anor", 200))
print(b.add("Banan", 100))
print(b.remove("olma"))
print(b.show())
print(b.canculator())
