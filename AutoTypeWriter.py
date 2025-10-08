import pyautogui
import time
import tkinter as tk
from tkinter import simpledialog
import sys

# ===== Custom Bigger Input Dialog =====
class BigInputDialog(simpledialog._QueryString):
    def body(self, master):
        self.geometry("800x550")
        self.title("Auto Type Writer")

        tk.Label(master, text="Enter the text to type below:", font=("Arial", 14)).pack(pady=10)

        self.entry = tk.Text(
            master,
            wrap="word",
            font=("Courier", 12),
            height=30,
            width=90
        )
        self.entry.pack(padx=15, pady=10, expand=True, fill="both")
        return self.entry

    def getresult(self):
        return self.entry.get("1.0", tk.END).strip()


# ===== Countdown Popup =====
def show_countdown(seconds, on_finish):
    countdown = tk.Toplevel()
    countdown.title("Get Ready!")
    countdown.geometry("400x200")
    countdown.configure(bg="#1e1e2e")
    countdown.attributes('-topmost', True)

    label = tk.Label(
        countdown,
        text="",
        font=("Arial", 16, "bold"),
        fg="#f8f8f2",
        bg="#1e1e2e",
        justify="center"
    )
    label.pack(expand=True, fill="both")

    def update(s):
        if s > 0:
            label.config(text=f"Place your cursor...\nTyping starts in {s} ⏳")
            countdown.after(1000, update, s - 1)
        else:
            countdown.destroy()
            on_finish()

    update(seconds)


# ===== Main Program =====
root = tk.Tk()
root.withdraw()

dialog = BigInputDialog(root, "Auto Type Writer")
text = dialog.result

# ===== Typing Function =====
def start_typing():
    time.sleep(0.5)  # slight delay for stability
    pyautogui.typewrite(text, interval=0.01)  # very fast typing
    root.destroy()
    sys.exit(0)

if text:
    show_countdown(5, start_typing)
    root.mainloop()
