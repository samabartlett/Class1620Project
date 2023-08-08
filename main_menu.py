#main_menu.py
import tkinter as tk
import csv
from shop_frame import ShopFrame
from view_transactions_frame import ViewTransactionsFrame

class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Shopping Cart")
        self.items = {'Cookie': 1.50, 'Sandwich': 4.00, 'Water': 1.00}
        self.transactions = {}
        self.create_widgets()

    def create_widgets(self):
        """Create the main menu buttons for navigating between pages"""
        self.button_shop = tk.Button(self, text="Shop", command=self.show_shop_frame)
        self.button_shop.pack()
        self.button_view_transactions = tk.Button(self, text="View Transactions", command=self.show_view_transactions_frame)
        self.button_view_transactions.pack()
        self.button_exit = tk.Button(self, text="Exit", command=self.destroy)
        self.button_exit.pack()

    def show_shop_frame(self):
        """Show the ShopFrame (destroying current frame)"""
        self.destroy_current_frame()
        self.shop_frame = ShopFrame(self, self.items, self.transactions, self.show_main_menu)
        self.shop_frame.pack()

    def show_view_transactions_frame(self):
        """Show the ViewTransactionsFrame (destroying current frame)"""
        self.destroy_current_frame()
        self.view_transactions_frame = ViewTransactionsFrame(self, self.transactions, self.show_main_menu)
        self.view_transactions_frame.pack()

    def show_main_menu(self):
        """Return to the main menu (destroying current frame and recreating widgets)"""
        self.destroy_current_frame()
        self.create_widgets()

    def destroy_current_frame(self):
        """Destroy the current frame and clear the window"""
        for frame in self.winfo_children():
            frame.destroy()

    def save_to_csv(self, transaction_label):
        """Save the current transactions contents to a CSV file
        Args:
            transaction_label (str): The label for the current transaction.
        This function saves the contents of the transactions to a CSV file named "transactions1.csv".
        The CSV file contains information about each item in the transaction, including the item's name, quantity, and price.
        The total price for the entire transaction is also calculated and saved in the CSV file.
        """
        with open("transactions1.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(["Transaction", "Item", "Quantity", "Price"])

            total_price = 0
            for item, quantity in self.transactions.items():
                price = self.items[item] * quantity
                total_price += price
                writer.writerow([transaction_label, item, quantity, f"${price:.2f}"])
            writer.writerow([transaction_label, "Total Price:", "", f"${total_price:.2f}"])