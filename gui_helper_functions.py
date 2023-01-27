from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
import random

from data import my_data, country_name

from functools import partial

populations = []
score = 0
num_que_1 = 0
num_que_2 = 0

window = Tk()


# Add line break after every 30 characters
def too_many_characters(characters):
    new_string = ""
    for i, letter in enumerate(characters):
        if i % 30 == 0 and i != 0:
            new_string += '-\n-'
        new_string += letter
    return new_string


# get user choose and print selected data about country
def get_selection(country_combobox, canvas_box, country_info_text):
    choose_country = country_combobox.get()
    index_country = country_name.index(choose_country)
    n_data = my_data[index_country]
    if "borders" not in n_data:
        n_data["borders"] = "-"
    if "capital" not in n_data:
        n_data["capital"] = "lack of information"

    populations.append({"country_name": n_data['name']['common'], "population": n_data['population']})
    data_to_print = f"{n_data['name']['common']}" \
                    f"\nBorders: {too_many_characters(' '.join(n_data['borders']))} " \
                    f"\nCapital: {''.join(n_data['capital'])}" \
                    f"\nContinents: {' '.join(n_data['continents'])} " \
                    f"\nFlags: {n_data['flags']['png']}" \
                    f"\nLanguages: {too_many_characters(' '.join(list(n_data['languages'].values())))} " \
                    f"\nPopulation: {n_data['population']} "

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
def next_question(canvas_box, country_info_text, score_label, canvas_quiz_box, quiz_text):
    global num_que_1, num_que_2
    canvas_box.itemconfig(country_info_text, text="")
    try:
        all_num_que = list(range(0, len(populations)))
        num_que_1 = random.choice(all_num_que)
        all_num_que.remove(num_que_1)
        num_que_2 = random.choice(all_num_que)
        # get key as str from list of dict
        que = f"{populations[num_que_1]['country_name']}      vs     {populations[num_que_2]['country_name']}"
        score_label.config(text=f"Score: {score}")
        canvas_quiz_box.config(bg="white")
        canvas_quiz_box.itemconfig(quiz_text, text=que)
    except IndexError:
        print("You have selected not enough countries, the minimum number is two.")


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
def give_feedback(is_right, canvas_box, country_info_text, score_label, canvas_quiz_box, quiz_text):
    if is_right:
        canvas_quiz_box.config(bg="green")
    else:
        canvas_quiz_box.config(bg="red")
    next_question_tmp = partial(next_question, canvas_box, country_info_text, score_label, canvas_quiz_box, quiz_text)
    window.after(1000, next_question_tmp)


# if user press right answer
def r_pressed(canvas_box, country_info_text, score_label, canvas_quiz_box, quiz_text):
    # function check answer can return false or true
    is_right = check_answer("first")
    give_feedback(is_right, canvas_box, country_info_text, score_label, canvas_quiz_box, quiz_text)


# if user press left answer
def l_pressed(canvas_box, country_info_text, score_label, canvas_quiz_box, quiz_text):
    is_right = check_answer("second")
    give_feedback(is_right, canvas_box, country_info_text, score_label, canvas_quiz_box, quiz_text)
