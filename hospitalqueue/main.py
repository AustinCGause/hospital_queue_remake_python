import tkinter as tk
import ttkbootstrap as ttk
import patient as Patient

# window
window = ttk.Window(themename = 'darkly', title = 'Hospital Queueing System', minsize = (600,500), scaling = False)


# login message
welcome = ttk.Label(window, text = 'Welcome to the SGMC Hospital Queueing System 1.0', font = ('Helvetica', '18', 'bold'))
welcome.pack(pady = 10)

# frame
frame = ttk.Frame(window, height = 200, width = 200).pack()

label = ttk.Label(frame, text = 'what the fuck').pack(side = 'bottom')
label = ttk.Label(frame, text = 'what the fuck').pack(side = 'top')

# patient queue table
# patient_table = ttk.Treeview(frame)
# patient_table.pack()

# run
window.mainloop()
