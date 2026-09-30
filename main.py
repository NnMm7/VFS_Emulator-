import tkinter as tk
from tkinter import scrolledtext
import shlex

VFS = "VFS_Emulator"

root = tk.Tk()
root.title(f"Эмулятор - {VFS}")

out = scrolledtext.ScrolledText(root)
out.pack(fill=tk.BOTH, expand=True)
out.configure(state=tk.DISABLED)

frame = tk.Frame(root)
frame.pack(fill=tk.X)

tk.Label(frame, text=f"{VFS}> ").pack(side=tk.LEFT)
entry = tk.Entry(frame)
entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

def print_line(text=""):
    out.configure(state=tk.NORMAL)
    out.insert(tk.END, text + "\n")
    out.see(tk.END)
    out.configure(state=tk.DISABLED)

def on_enter(event=None):
    line = entry.get()
    entry.delete(0, tk.END)
    print_line(f"{VFS}> {line}")

    if not line.strip():
        return

    try:
        parts = shlex.split(line)
    except ValueError:
        print_line("Ошибка: неправильное использование кавычек")
        return

    if not parts:
        return

    cmd = parts[0]
    args = parts[1:]

    if cmd == "exit":
        if args:
            print_line("Ошибка: команда exit не принимает аргументов")
        else:
            print_line("Завершение работы эмулятора...")
            root.destroy()
    elif cmd == "ls":
        print_line("ls: команда-заглушка")
        print_line(f"  аргументы: {args}")
    elif cmd == "cd":
        print_line("cd: команда-заглушка")
        print_line(f"  аргументы: {args}")
    else:
        print_line(f"Ошибка: неизвестная команда {cmd}")

entry.bind("<Return>", on_enter)
entry.focus_set()

print_line(f"Добро пожаловать в эмулятор ({VFS})")
print_line("Доступные команды: ls, cd, exit\n")

root.mainloop()