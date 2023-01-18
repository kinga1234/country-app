from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from data import data, country_name


window = Tk()
window.title("country app")
window.config(padx=50, pady=50, bg="#B1DDC6")

my_combo = ttk.Combobox(window, values=country_name)
my_combo.pack(pady=20)
# val = my_combo.get()


def get_selection():
    choose_country = my_combo.get()
    index_country = country_name.index(choose_country)
    n_data = data["list"][index_country]
    if "borders" not in n_data:
        n_data["borders"] = "0"
    data_to_print = f"{n_data['name']['common']}" \
                    f"\nBorders: {' '.join(n_data['borders'])} " \
                    f"\nCapital: {''.join(n_data['capital'])}" \
                    f"\nContinents: {' '.join(n_data['continents'])} " \
                    f"\nCurrencies: {list(list(n_data['currencies'].values())[0].values())[0]}" \
                    f"\nFlags: {n_data['flags']['png']}" \
                    f"\nLanguages: {' '.join(list(n_data['languages'].values()))} " \
                    f"\nPopulation: {n_data['population']} "

    messagebox.showinfo("info", data_to_print)


button = Button(window, text="show information", command=get_selection)
button.pack(pady=20)


window.mainloop()
