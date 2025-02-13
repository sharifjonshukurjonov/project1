import uuid


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.__id = uuid.uuid4()

    def get_id(self):
        return self.__id

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


# -------------------------------------------------------------------------->>> Basket


class Basket:
    def __init__(self):
        self.__id = uuid.uuid4()
        self.data = []

    def add(self, name, price, quantities):
        product = {
            "name": name,
            "price": price,
            "quantities": quantities,
            "id": self.__id
        }
        self.data.append(product)

    def remove(self, product_name):
        for product in self.data:
            if product["name"] == product_name:
                self.data.remove(product)
                return f"{product_name} o‘chirildi."
        return "Omborda bunday maxsulot yo‘q."

    def calculator(self):
        return sum(product["price"] * product["quantities"] for product in self.data)

    def get_id(self):
        return self.__id

    def show(self):
        return f"Savatdagi maxsulotlar: {self.data}"


products = {
    "Telefon": Product("Telefon", 300, 5),
    "Noutbuk": Product("Noutbuk", 100, 2)
}

basket = Basket()

while True:
    print("\n1. Product bo'limi\n2. Basket bo'limi\n3. Chiqish")
    ans = input("Iltimos son kiritin >> ")

    if ans == "1":
        print("\n1. Ma'lumotlar\n2. Sotish\n3. Qo'shish\n4. ID")
        pro_ans = input("Tanlang >> ")

        if pro_ans == "1":
            for product in products.values():
                print(product.info())
        elif pro_ans == "2":
            name = input("Maxsulot nomi: ")
            amount = int(input("Miqdori: "))
            if name in products:
                print(products[name].sell(amount))
            else:
                print("Bunday maxsulot yo‘q!")
        elif pro_ans == "3":
            name = input("Maxsulot nomi: ")
            amount = int(input("Miqdori: "))
            if name in products:
                print(products[name].add(amount))
            else:
                print("Bunday maxsulot yo‘q!")
        elif pro_ans == "4":
            name = input("Maxsulot nomi: ")
            if name in products:
                print(f"{name} ID: {products[name].get_id()}")
            else:
                print("Bunday maxsulot yo‘q!")

    elif ans == "2":
        print("\n1. Savatni ko'rish\n2. Maxsulot qo'shish\n3. Maxsulot o'chirish\n4. Jami narxni hisoblash")
        bask_ans = input("Tanlang >> ")

        if bask_ans == "1":
            print(basket.show())
        elif bask_ans == "2":
            name = input("Maxsulot nomi: ")
            price = int(input("Narxi: "))
            quantity = int(input("Miqdori: "))
            basket.add(name, price, quantity)
            print("Maxsulot savatga qo'shildi!")
        elif bask_ans == "3":
            name = input("O'chiriladigan maxsulot nomi: ")
            print(basket.remove(name))
        elif bask_ans == "4":
            print(f"Savatdagi jami narx: {basket.calculator()} so'm")

    elif ans == "3":
        print("Dastur tugadi.")
        break
    else:
        print("Iltimos 1, 2 yoki 3 ni tanlang!")
