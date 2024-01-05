import customtkinter as tk


class TaxCalculator():
    def __init__(self):
        self.window = tk.CTk()
        self.window.title("Tax Calculator")
        self.window.geometry("400x250")
        self.window.resizable(False, False)

        self.padding: dict = {"padx": 30, "pady": 10}

        self.income_label = tk.CTkLabel(self.window, text="Income: ")
        self.income_label.grid(row=0, column=0, **self.padding)
        self.income_entry = tk.CTkEntry(self.window)
        self.income_entry.grid(row=0, column=1, **self.padding)

        self.tax_label = tk.CTkLabel(self.window, text="Tax: ")
        self.tax_label.grid(row=1, column=0, **self.padding)
        self.tax_entry = tk.CTkEntry(self.window)
        self.tax_entry.grid(row=1, column=1, **self.padding)

        self.result_label = tk.CTkLabel(self.window, text="Due amount: ")
        self.result_label.grid(row=2, column=0, **self.padding)
        self.result_entry = tk.CTkLabel(self.window, text="")
        self.result_entry.grid(row=2, column=1, **self.padding)

        self.calculate_button = tk.CTkButton(self.window, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=3, column=0, **self.padding)

    def run(self):
        self.window.mainloop()

    def calculate(self):
        try:
            income = float(self.income_entry.get())
            tax = float(self.tax_entry.get())
            result = income * tax / 100
            text = str(round(result, 2))
            self.update_result(text)
        except ValueError:
            pass

    def update_result(self, text: str):
        self.result_entry.configure(text=text, require_redraw=True)


if __name__ == "__main__":
    app = TaxCalculator()
    app.run()
