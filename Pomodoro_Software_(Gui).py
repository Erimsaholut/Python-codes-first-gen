from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
GREEN2 = "#367E18"
FONT_NAME = "Courier"
WORK_MIN = 0.10
SHORT_BREAK_MIN = 0.10
LONG_BREAK_MIN = 20
TURN = 1
TİMER = None
CHECK = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global CHECK, TURN
    window.after_cancel(TİMER)
    timer_text.config(text="Timer", fg=GREEN)

    CHECK = ""
    TURN = 1
    check_mark.config(text=CHECK)

    canvas.itemconfig(canvas_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_start():
    global TURN

    if TURN % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        timer_text.config(fg=GREEN2, text="Long Break")

    elif TURN % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        timer_text.config(fg=PINK, text="Short Break")

    else:
        countdown(WORK_MIN * 60)
        timer_text.config(fg=RED, text="Work Time", )

    TURN += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def tick_sign():
    global CHECK
    CHECK += "✔"
    check_mark.config(text=CHECK)


def countdown(count):
    minutes = int(count / 60)
    seconds = count % 60

    if 10 > seconds:
        seconds = "0" + str(seconds)
    if 10 > minutes:
        minutes = "0" + str(minutes)

    canvas.itemconfig(canvas_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global TİMER
        TİMER = window.after(1000, countdown, count - 1)
    else:
        timer_start()
        if TURN % 2 == 1:
            tick_sign()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro by Erim")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
foto = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=foto)
canvas_text = canvas.create_text(100, 130, fill="white", text="00:00", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=2, row=2)

timer_text = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=YELLOW, )

timer_text.grid(column=2, row=1)

start_button = Button(text="Start", highlightbackground=YELLOW, command=timer_start)
reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
start_button.grid(column=1, row=3)
reset_button.grid(column=3, row=3)

check_mark = Label(font=(FONT_NAME, 25, "bold"), foreground=GREEN, background=YELLOW)
check_mark.grid(column=2, row=4)

window.mainloop()
