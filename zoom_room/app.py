import tkinter as tk
from tkinter import ttk, filedialog
from driver import navigate
import locators as element


# main GUI window
root = tk.Tk()
root.title("Zoom Room")

# main frame within window
main = ttk.Frame(root)
main.pack(fill="both", expand=True, padx=1, pady=(4, 0))

# buttons - there must be a prettier way to code these
calc2h_button = ttk.Button(root, text="Calculus 2 Lecture", command=lambda : navigate(element.Name.CALC2_H)).pack(side="left", fill="x", expand=True)
calc2t_button = ttk.Button(root, text="Calculus 2 Review", command=lambda : navigate(element.Name.CALC2_T)).pack(side="left", fill="x", expand=True)
phys2h_button = ttk.Button(root, text="Physics 2 Lecture", command=lambda : navigate(element.Name.PHYS2_H)).pack(side="left", fill="x", expand=True)
phys2t_button = ttk.Button(root, text="Physics 2 Review", command=lambda : navigate(element.Name.PHYS2_T)).pack(side="left", fill="x", expand=True)
difeqh_button = ttk.Button(root, text="Differential Equations Lecture", command=lambda : navigate(element.Name.DIFEQ_H)).pack(side="left", fill="x", expand=True)
difeqt_button = ttk.Button(root, text="Differential Equations Review", command=lambda : navigate(element.Name.DIFEQ_T)).pack(side="left", fill="x", expand=True)

# activating main loop
root.mainloop()














