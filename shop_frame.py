#shop_frame.py
import tkinter as tk

class ShopFrame(tk.Frame):
    def __init__(self, master, items, cart, return_to_main_menu):
        """
        Initialize the ShopFrame
        Parameters:
            items (dict): items available for purchase with their prices
            cart (dict): the cart with items and their quantities
            return_to_main_menu(): return to the main menu
        """
        super().__init__(master)
        self.items = items
        self.cart = cart
        self.return_to_main_menu = return_to_main_menu
        self.transaction_counter = 1  #Counter for transaction number
        self.create_widgets()

    def create_widgets(self):
        """Create the widgets for the ShopFrame"""
        self.label_shop = tk.Label(self, text="----SHOP----")
        self.label_shop.pack()
        self.cart_label = tk.Label(self, text="Cart Contents:")
        self.cart_label.pack()
        self.note_label = tk.Label(self, text="Cart items must be non-negative integers", fg="red")
        self.note_label.pack()
        self.cart_contents_label = tk.Label(self, text="", wraplength=300, justify='left')
        self.cart_contents_label.pack()
        self.cart_frame = tk.Frame(self)
        self.cart_frame.pack()

        self.item_entries = {}
        for idx, item in enumerate(self.items.keys(), start=1):
            label = tk.Label(self.cart_frame, text=f"{item}:")
            label.grid(row=idx, column=0, sticky="e", padx=5, pady=5)
            entry = tk.Entry(self.cart_frame)
            entry.grid(row=idx, column=1, padx=5, pady=5)
            self.item_entries[item] = entry
            add_button = tk.Button(self.cart_frame, text="+", command=lambda i=item: self.add_to_cart(i))
            add_button.grid(row=idx, column=2, padx=5, pady=5)
            remove_button = tk.Button(self.cart_frame, text="-", command=lambda i=item: self.remove_from_cart(i))
            remove_button.grid(row=idx, column=3, padx=5, pady=5)
        self.cart_buttons_frame = tk.Frame(self)
        self.cart_buttons_frame.pack()
        self.button_checkout = tk.Button(self.cart_buttons_frame, text="Checkout", command=self.update_cart)
        self.button_checkout.grid(row=1, column=0, padx=5, pady=5)
        self.button_exit = tk.Button(self, text="Exit", command=self.master.destroy)
        self.button_exit.pack(side=tk.BOTTOM)
        self.button_return_to_main_menu = tk.Button(self, text="Return to Main Menu", command=self.return_to_main_menu)
        self.button_return_to_main_menu.pack(side=tk.BOTTOM)
        self.update_cart_label()

    def add_to_cart(self, item):
        """
        Add items to the cart
        Parameters:
            item (str): the item to add to the cart
        """
        entry = self.item_entries[item]
        try:
            quantity = int(entry.get())
        except ValueError:
            quantity = 0
        if quantity > 0:
            if item in self.cart:
                self.cart[item] += quantity
            else:
                self.cart[item] = quantity
        self.update_cart_label()

    def remove_from_cart(self, item):
        """
        Remove items from the cart
        Parameters:
            item (str): item to remove from the cart
        """
        entry = self.item_entries[item]
        try:
            quantity = int(entry.get())
        except ValueError:
            quantity = 0
        if quantity > 0:
            if item in self.cart:
                self.cart[item] = max(self.cart[item] - quantity, 0)
        self.update_cart_label()

    def update_cart_label(self):
        """Update the cart label with the current cart contents"""
        cart_text = "\n".join([f"({quantity}) - {item} = ${self.items[item] * quantity:.2f}" for item, quantity in self.cart.items()])
        self.cart_contents_label.config(text=cart_text)

    def update_cart(self):
        """Update the cart and save to the CSV file"""
        self.update_cart_label()
        transaction_label = f"T{self.transaction_counter}"
        self.master.save_to_csv(transaction_label)  #Pass the current transaction label
        self.transaction_counter += 1  #Increment the transaction number for the next transaction