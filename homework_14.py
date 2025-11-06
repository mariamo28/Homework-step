class ShoppingCart:

    def __init__(self):
        self.items = []
        self.prices = {
            "პური": 2.5,
            "კარაქი": 3.0,
            "ნადუღი": 1.5,
            "რძე": 2.0,
            "ყველი": 5.0,
            "კვერცხი": 0.5
        }

    def add_item(self, item_name, qty=1):
        if item_name in self.prices:
            self.items.append((item_name, qty))
            print(f" დამატებულია: {item_name} ({qty} ცალი)")
        else:
            print(f" შეცდომა: '{item_name}' არ მოიძებნა")

    def remove_item(self, item_name):
        for i, (name, qty) in enumerate(self.items):
            if name == item_name:
                self.items.pop(i)
                print(f" წაშლილია: {item_name}")
                return
        print(f" '{item_name}' არ არის კალათაში")

    def current_items(self):
        return self.items

    def calculate_total(self):
        total = 0
        for item_name, qty in self.items:
            if item_name in self.prices:
                total += self.prices[item_name] * qty
        return total

    def display_cart(self):
        print("\n" + "=" * 50)
        print("თქვენი კალათა:")
        print("=" * 50)

        if not self.items:
            print("კალათა ცარიელია")
            return

        for item_name, qty in self.items:
            price = self.prices.get(item_name, 0)
            subtotal = price * qty
            print(f"{item_name:15} x {qty:2} = {subtotal:6.2f} ლარი")

        print("-" * 50)
        print(f"{'ჯამი:':15}        {self.calculate_total():6.2f} ლარი")
        print("=" * 50 + "\n")


if __name__ == "__main__":
    cart = ShoppingCart()

    print("ნივთების დამატება:")
    cart.add_item(item_name="პური", qty=2)
    cart.add_item(item_name="კარაქი", qty=1)
    cart.add_item(item_name="ნადუღი", qty=6)
    cart.add_item(item_name="რძე", qty=2)

    print("ამჟამინდელი კალათა:")
    print(cart.current_items())
    print(f"ჯამი: {cart.calculate_total()}")

    cart.display_cart()
    print("ნივთის წაშლა:")
    cart.remove_item("რძე")

    print("ამჟამინდელი კალათა:")
    print(cart.current_items())
    print(f"ჯამი: {cart.calculate_total()}")

    cart.display_cart()