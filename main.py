from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#9090C0"
RED = "#E7DADA"
GREEN = "#4F666A"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    # timer_text: 00:00
    timer_label.config(text="Timer")
    # timer_label: "Timer"
    canvas.itemconfig(timer_text, text="00:00")
    # reset check_marks
    global reps
    reps = 0
    check_marks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        timer_label.config(text="WORK", fg=RED)
        count_down(work_sec)
    elif reps % 2 == 0 and reps != 8:
        timer_label.config(text="BREAK", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="BREAK", fg=GREEN)
        count_down(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
            check_marks.config(text=marks)


# ---------- ------------------ UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
# window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)
window.config(padx=100, pady=50)

canvas = Canvas(width=200, height=224)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=RED, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

start = Button(text="Start", command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", command=reset_timer)
reset.grid(column=2, row=2)

check_marks = Label(fg=RED)
check_marks.grid(column=1, row=3)

window.mainloop()
