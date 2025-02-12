class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def info(self):
        return f"{self.name} nomli maxulot\nNarxi: {self.price} so'm\nMiqdori: {self.quantity}"

    def sell(self, amount):
        if amount > self.quantity:
            return f"Xatolik: Omborda faqat {self.quantity} dona mavjud!"
        self.quantity -= amount
        return f"{amount} dona {self.name} sotildi. Qolgan miqdor: {self.quantity}"

    def add(self, amount):
        self.quantity += amount
        return f"Yangi {amount} dona {self.name} qo'shildi. Jami miqdor: {self.quantity}"

class Electronics(Product):
    def __init__(self, name, price, quantity, warranty):
        super().__init__(name, price, quantity)
        self.warranty = warranty

    def info(self):
        return f"{self.name} nomli elektronika\nNarxi: {self.price} so'm\nMiqdori: {self.quantity}\nKafolat muddati: {self.warranty_period} oy"

    def warranty(self):
        return f"{self.name} uchun {self.warranty} oylik kafolat muddati."

class Food(Product):
    def __init__(self, name, price, quantity, expiration):
        super().__init__(name, price, quantity)
        self.expiration = expiration

    def info(self):
        return f"{self.name} nomli oziq-ovqat\nNarxi: {self.price} so'm\nMiqdori: {self.quantity}\nYaroqlilik muddati: {self.expiration_date}"

    def expiration_date(self):
        return f"{self.name} uchun yaroqlilik muddati: {self.expiration}"

    def sell(self, amount):
        if amount > self.quantity:
            return f"Xatolik: Omborda faqat {self.quantity} dona mavjud!"
        self.quantity -= amount
        return f"{amount} dona {self.name} sotildi. Qolgan miqdor: {self.quantity}"


