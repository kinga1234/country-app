from tkinter import *
from tkinter import ttk
from data import data, country_name
import pandas as pd
import matplotlib.pyplot as plt
import random

populations = []
score = 0

num_que_1 = 0
num_que_2 = 0


# Add line break after every 30 characters
def too_many_characters(characters):
    new_string = ""
    for i, letter in enumerate(characters):
        if i % 30 == 0 and i != 0:
            new_string += '-\n-'
        new_string += letter
    return new_string


# get user choose and print selected data about country
def get_selection():
    choose_country = country_combobox.get()
    index_country = country_name.index(choose_country)
    n_data = data[index_country]
    if "borders" not in n_data:
        n_data["borders"] = "-"
    if "capital" not in n_data:
        n_data["capital"] = "lack of information"
    # if "currencies" not in n_data:
    #     n_data["currencies"] = "lack of information"

    populations.append({"country_name": n_data['name']['common'], "population": n_data['population']})
    data_to_print = f"{n_data['name']['common']}" \
                    f"\nBorders: {too_many_characters(' '.join(n_data['borders']))} " \
                    f"\nCapital: {''.join(n_data['capital'])}" \
                    f"\nContinents: {' '.join(n_data['continents'])} " \
                    f"\nFlags: {n_data['flags']['png']}" \
                    f"\nLanguages: {too_many_characters(' '.join(list(n_data['languages'].values())))} " \
                    f"\nPopulation: {n_data['population']} "
    # f"\nCurrencies: {list(list(n_data['currencies'].values())[0].values())[0]}" \

    canvas_box.itemconfig(country_info_text, text=data_to_print)


def show_plot():
    df = pd.DataFrame(populations)
    df.plot(x="country_name", y="population", kind="bar")
    num_pop_data = [populations[num]["population"] for num in range(len(populations))]
    print(num_pop_data)
    for index, value in enumerate(num_pop_data):
        plt.text(x=index, y=value, s=f"{value}")

    plt.show()

# display next question in quiz and update score
def next_question():
    canvas_box.itemconfig(country_info_text, text="")
    all_num_que = list(range(0, len(populations)))
    global num_que_1, num_que_2
    num_que_1 = random.choice(all_num_que)
    all_num_que.remove(num_que_1)
    num_que_2 = random.choice(all_num_que)
    # get key as str from list of dict
    que = f"{populations[num_que_1]['country_name']}      vs     {populations[num_que_2]['country_name']}"
    # question = f"{list(populations[num_que_1].keys())[0]}    vs    {list(populations[num_que_2].keys())[0]}"
    score_label.config(text=f"Score: {score}")
    canvas_quiz_box.config(bg="white")
    canvas_quiz_box.itemconfig(quiz_text, text=que)


# check user answer and return true or false
def check_answer(user_answer):
    global num_que_1, num_que_2, score
    # get value as int from list of dict
    if populations[num_que_1]["population"] > populations[num_que_2]["population"]:
        correct_answer = "first"
        if user_answer == correct_answer:
            score += 1
            return True
        else:
            return False
    else:
        correct_answer = "second"
        if user_answer == correct_answer:
            score += 1
            return True
        else:
            return False


# change bg to green if answer is right and red if is wrong
def give_feedback(is_right):
    if is_right:
        canvas_quiz_box.config(bg="green")
    else:
        canvas_quiz_box.config(bg="red")

    window.after(1000, next_question)


# if user press right answer
def r_pressed():
    # function check answer can return false or true
    is_right = check_answer("first")
    give_feedback(is_right)


# if user press left answer
def l_pressed():
    is_right = check_answer("second")
    give_feedback(is_right)


# ----------------------------- UI SETUP ---------------------------------


window = Tk()
window.title("country app")
window.config(padx=50, pady=50, bg="#B1DDC6")


# --- UI setup to country information ---
choose_country_label = Label(text="Choose a country:", fg="black", bg="#B1DDC6", font=("Arial", 15))
choose_country_label.grid(row=0, column=0)

country_combobox = ttk.Combobox(window, values=country_name)
country_combobox.grid(row=0, column=1)

canvas_box = Canvas(window, width=370, height=280, bg="white")
country_info_text = canvas_box.create_text(185, 140, text="", font=("Arial", 12, "italic"))
canvas_box.grid(row=2, column=0, columnspan=2, pady=20)

button = Button(window, text="show information", command=get_selection)
button.grid(row=1, column=1)

# --- UI setup to plot ---
plot_label = Label(text="PLOT: Click the button next to see plot with\n populations of the countries selected previous",
                   fg="black", bg="#B1DDC6", font=("Arial", 10))
plot_label.grid(row=3, column=0)

plot_button = Button(window, text="show plot", command=show_plot)
plot_button.grid(row=3, column=1)

# --- UI setup to quiz about populations ---
quiz_label = Label(text="QUIZ: Check your knowledge about the populations of the countries selected previous",
                   fg="black", bg="#B1DDC6", font=("Arial", 10))
quiz_label.grid(row=0, column=2, columnspan=2, padx=20)

quiz_button = Button(window, text="start quiz", command=next_question)
quiz_button.grid(row=1, column=2)

score_label = Label(text="Score = 0", fg="black", bg="#B1DDC6", font=("Arial", 10))
score_label.grid(row=1, column=3)

canvas_quiz_box = Canvas(window, width=400, height=220, bg="white")
quiz_text = canvas_quiz_box.create_text(200, 110, text="", font=("Arial", 15, "italic"))
canvas_quiz_box.grid(row=2, column=2, columnspan=2)

up_arrow = PhotoImage(file="./up_arrow.png")

r_button = Button(image=up_arrow, highlightthickness=0, command=r_pressed)
r_button.grid(row=3, column=2)

l_button = Button(image=up_arrow, highlightthickness=0, command=l_pressed)
l_button.grid(row=3, column=3)


window.mainloop()
