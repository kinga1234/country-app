from tkinter import (
    ttk, Label, Canvas, Button, PhotoImage
)

from gui_helper_functions import (
    country_name,
    get_selection,
    show_plot,
    next_question,
    r_pressed,
    l_pressed
)
from functools import partial

up_arrow = PhotoImage(file="./up_arrow.png")


def set_widgets(window):
    # --- UI setup to country information ---
    choose_country_label = Label(text="Choose a country:", fg="black", bg="#B1DDC6", font=("Arial", 15))
    choose_country_label.grid(row=0, column=0)

    country_combobox = ttk.Combobox(window, values=country_name)
    country_combobox.grid(row=0, column=1)

    canvas_box = Canvas(window, width=370, height=280, bg="white")
    country_info_text = canvas_box.create_text(185, 140, text="", font=("Arial", 12, "italic"))
    canvas_box.grid(row=2, column=0, columnspan=2, pady=20)

    get_selection_tmp = partial(get_selection, country_combobox, canvas_box, country_info_text)
    button = Button(window, text="show information", command=get_selection_tmp)
    button.grid(row=1, column=1)

    # --- UI setup to plot ---
    plot_label = Label(
        text="PLOT: Click the button next to see plot with\n populations of the countries selected previous",
        fg="black", bg="#B1DDC6", font=("Arial", 10))
    plot_label.grid(row=3, column=0)

    plot_button = Button(window, text="show plot", command=show_plot)
    plot_button.grid(row=3, column=1)

    # --- UI setup to quiz about populations ---
    quiz_label = Label(text="QUIZ: Check your knowledge about the populations of the countries selected previous",
                       fg="black", bg="#B1DDC6", font=("Arial", 10))
    quiz_label.grid(row=0, column=2, columnspan=2, padx=20)

    score_label = Label(text="Score = 0", fg="black", bg="#B1DDC6", font=("Arial", 10))
    score_label.grid(row=1, column=3)

    canvas_quiz_box = Canvas(window, width=400, height=220, bg="white")
    quiz_text = canvas_quiz_box.create_text(200, 110, text="", font=("Arial", 15, "italic"))
    canvas_quiz_box.grid(row=2, column=2, columnspan=2)

    next_question_tmp = partial(next_question, canvas_box, country_info_text, score_label, canvas_quiz_box, quiz_text)
    quiz_button = Button(window, text="start quiz", command=next_question_tmp)
    quiz_button.grid(row=1, column=2)

    r_pressed_tmp = partial(r_pressed, canvas_box, country_info_text, score_label, canvas_quiz_box, quiz_text)
    r_button = Button(image=up_arrow, highlightthickness=0, command=r_pressed_tmp)
    r_button.grid(row=3, column=2)

    l_pressed_tmp = partial(l_pressed, canvas_box, country_info_text, score_label, canvas_quiz_box, quiz_text)
    l_button = Button(image=up_arrow, highlightthickness=0, command=l_pressed_tmp)
    l_button.grid(row=3, column=3)
