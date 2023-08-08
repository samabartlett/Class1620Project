#view_transactions_frame.py
import tkinter as tk
import csv

class ViewTransactionsFrame(tk.Frame):
    """
    Initialize the ViewTransactionsFrame
    Args:
            transactions (list): A list of transactions data
            return_to_main_menu (function): A function to return to the main menu
    """
    def __init__(self, master, transactions, return_to_main_menu):
        super().__init__(master)
        self.transactions = transactions
        self.return_to_main_menu = return_to_main_menu
        self.create_widgets()
        self.view_transactions_contents()

    def create_widgets(self):
        """Create the widgets for the ViewTransactionsFrame"""
        self.label_transactions = tk.Label(self, text="----TRANSACTIONS----")
        self.label_transactions.pack()
        self.transactions_contents_label = tk.Label(self, text="", wraplength=300, justify='left')
        self.transactions_contents_label.pack()
        self.transactions_buttons_frame = tk.Frame(self)
        self.transactions_buttons_frame.pack()
        self.button_clear_transactions = tk.Button(self.transactions_buttons_frame, text="Clear Transactions", command=self.clear_transactions)
        self.button_clear_transactions.grid(row=0, column=0, padx=5, pady=5)
        self.button_exit = tk.Button(self, text="Exit", command=self.master.destroy)
        self.button_exit.pack(side=tk.BOTTOM)
        self.button_return_to_main_menu = tk.Button(self, text="Return to Main Menu", command=self.return_to_main_menu)
        self.button_return_to_main_menu.pack(side=tk.BOTTOM)

    def view_transactions_contents(self):
        """View the contents of the CSV file and display it in the label space"""
        try:
            with open("transactions1.csv", mode="r") as file:
                reader = csv.reader(file)
                transactions_text = "\n".join([", ".join(row) for row in reader])
                self.transactions_contents_label.config(text=transactions_text)
        except FileNotFoundError:
            self.transactions_contents_label.config(text="Transactions are empty. No contents found.")

    def clear_transactions(self):
        """Clear all the transactions and the contents of the CSV file"""
        self.transactions.clear()
        self.view_transactions_contents()
        header_row = ["Transaction", "Item", "Quantity", "Price"]
        with open("transactions1.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header_row)
        print("Transactions cleared.")
        self.master.show_view_transactions_frame()