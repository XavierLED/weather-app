import tkinter as tk
import main

root = tk.Tk()
root.title("Weather App")
root.minsize(300, 300)

def get_weather():
    text_list.delete(0, tk.END)
    text = main.main(entry.get())
    if len(text) == 5:
        for i in text:
            text_list.insert(tk.END, i)
    else:
        text_list.insert(tk.END, text)
    entry.delete(0, tk.END)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = tk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew")

frame.columnconfigure(1, weight=1)
frame.rowconfigure(1, weight=1)

label = tk.Label(frame, text="Insert city name")
label.grid(row=0, column=0)

entry = tk.Entry(frame)
entry.grid(row=0, column = 1, sticky="ew")

entry.bind("<Return>", lambda event: get_weather())

entry_button = tk.Button(frame, text="Search", command=get_weather)
entry_button.grid(row=0, column=2)

text_list = tk.Listbox(frame)
text_list.grid(row=1, column=0, columnspan=3, sticky="nsew")

root.mainloop()

