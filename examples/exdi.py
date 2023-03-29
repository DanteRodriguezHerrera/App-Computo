import tkinter as tk
root = tk.Tk()
consulsts_frame = tk.Frame(root)
consulsts_frame.pack(expand=1, fill="both")

scrollbar1 = tk.Scrollbar(consulsts_frame)
scrollbar1.pack(side=tk.LEFT, fill=tk.Y)
listbox1 = tk.Listbox(consulsts_frame)
scrollbar1.config(command=listbox1.yview)
listbox1.pack(expand=1, fill="both", side="left")
listbox1.config(bg = "#329171", yscrollcommand=scrollbar1.set)

root.mainloop()