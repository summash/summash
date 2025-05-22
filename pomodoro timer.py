import tkinter as tk
import pygame

root = tk.Tk()
root.title("Study Task Manager")



tk.Label(root, text="Pomodoro Work (min):").grid(row=8, column=0)
entry_work = tk.Entry(root)
entry_work.grid(row=8, column=1)

tk.Label(root, text="Short Break (min):").grid(row=9, column=0)
entry_short = tk.Entry(root)
entry_short.grid(row=9, column=1)

tk.Label(root, text="Long Break (min):").grid(row=10, column=0)
entry_long = tk.Entry(root)
entry_long.grid(row=10, column=1)

tk.Label(root, text="Cycles:").grid(row=11, column=0)
entry_cycles = tk.Entry(root)
entry_cycles.grid(row=11, column=1)

pomodoro_status = tk.Label(root, text="", fg="purple")
pomodoro_status.grid(row=13, column=0, columnspan=2)

def run_pomodoro():
    try:
        work = int(entry_work.get())
        short_break = int(entry_short.get())
        long_break = int(entry_long.get())
        cycles = int(entry_cycles.get())
        start_pomodoro(work, short_break, long_break, cycles)
    except ValueError:
        pomodoro_status.config(text="❌ Enter all durations as numbers.")
        
        


def start_pomodoro(work, short_break, long_break, cycles):
    def countdown(seconds, label, next_step):
        if seconds > 0:
            mins, secs = divmod(seconds, 60)
            label.config(text=f"⏳ {mins:02d}:{secs:02d}")
            root.after(1000, countdown, seconds - 1, label, next_step)
        else:
            next_step()

    def pomodoro_cycle(cycle):
        if cycle > cycles:
            pomodoro_status.config(text="🎉 Pomodoro complete!")
            return

        pomodoro_status.config(text=f"🍅 Pomodoro {cycle}: Work {work} min")
        countdown(work * 60, pomodoro_status, lambda: start_break(cycle))

    def start_break(cycle):
        if cycle < cycles:
            pomodoro_status.config(text=f"☕ Short break: {short_break} min")
            countdown(short_break * 60, pomodoro_status, lambda: pomodoro_cycle(cycle + 1))
        else:
            pomodoro_status.config(text=f"🎉 Long break: {long_break} min")
            countdown(long_break * 60, pomodoro_status, lambda: pomodoro_cycle(cycle + 1))

    pomodoro_cycle(1)
    
    
def sound():
    pygame.mixer.init()
    ping_sound = pygame.mixer.Sound("ping.ogg")



tk.Button(root, text="▶️ Start Pomodoro", command=run_pomodoro).grid(row=12, column=0, columnspan=2)

root.mainloop()