import tkinter as tk

def on_click(event):
    current_text = output.get("1.0", "end-1c")
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current_text)
            output.delete("1.0", tk.END)
            output.insert(tk.END, str(result))
        except Exception as e:
            output.delete("1.0", tk.END)
            output.insert(tk.END, "Error")

    elif button_text == "C":
        output.delete("1.0", tk.END)

    else:
        output.insert(tk.END, button_text)

root = tk.Tk()
root.title("Calculator")
root.configure(bg="black")

output = tk.Text(root, height=2)
output.pack(padx=10, pady=10)

btnframe = tk.Frame(root)
btnframe.columnconfigure(0, weight=1)
btnframe.columnconfigure(1, weight=1)
btnframe.columnconfigure(2, weight=1)
btnframe.columnconfigure(3, weight=1)

operators = ["/", "*", "-", "+"]
for i, operator in enumerate(operators):
    btn = tk.Button(btnframe, text=operator)
    btn.grid(row=0, column=i, sticky=tk.W+tk.E)
    btn.bind("<Button-1>", on_click)

numbers = ["7", "8", "9", "4", "5", "6", "1", "2", "3"]
for i, number in enumerate(numbers):
    btn = tk.Button(btnframe, text=number)
    btn.grid(row=i // 3 + 1, column=i % 3, sticky=tk.W+tk.E)
    btn.bind("<Button-1>", on_click)
    
btn = tk.Button(btnframe, text="0")
btn.grid(row=4, column=1, sticky=tk.W+tk.E)
btn.bind("<Button-1>", on_click)

equal_btn = tk.Button(btnframe, text="=")
equal_btn.grid(row=4, column=3, sticky=tk.W+tk.E)

clear_btn = tk.Button(btnframe, text="C")
clear_btn.grid(row=4, column=0, sticky=tk.W+tk.E)

equal_btn.bind("<Button-1>", on_click)
clear_btn.bind("<Button-1>", on_click)

btnframe.pack(fill='x')

root.mainloop()
