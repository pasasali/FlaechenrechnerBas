import tkinter as tk


def calculate():
    try:
        shape = shape_var.get()

        if shape == "Rechteck":
            a = float(entry_a.get())
            b = float(entry_b.get())
            area = a * b
            formula = f"A = a · b = {a} · {b}"
        elif shape == "Dreieck":
            a = float(entry_a.get())
            h = float(entry_b.get())
            area = (a * h) / 2
            formula = f"A = (a · h) / 2 = ({a} · {h}) / 2"
        elif shape == "Kreis":
            r = float(entry_a.get())
            area = 3.14159 * r * r
            formula = f"A = π · r² = 3.14159 · {r}²"
        else:
            result_label.config(text="Bitte eine Form auswählen.")
            return

        result_label.config(text=f"Fläche: {area:.2f}")
        formula_label.config(text=f"Formel: {formula}")

    except ValueError:
        result_label.config(text="Bitte gültige Zahlen eingeben.")
        formula_label.config(text="Formel:")


def update_inputs(*args):
    shape = shape_var.get()

    if shape == "Kreis":
        label_a.config(text="Radius r:")
        label_b.config(text="-")
        entry_b.delete(0, tk.END)
        entry_b.config(state="disabled")
    elif shape == "Rechteck":
        label_a.config(text="Seite a:")
        label_b.config(text="Seite b:")
        entry_b.config(state="normal")
    elif shape == "Dreieck":
        label_a.config(text="Grundseite a:")
        label_b.config(text="Höhe h:")
        entry_b.config(state="normal")


root = tk.Tk()
root.title("Flaechenrechner")
root.geometry("400x300")

shape_var = tk.StringVar(value="Rechteck")
shape_var.trace_add("write", update_inputs)

tk.Label(root, text="Form auswählen:").pack(pady=(10, 5))
shape_menu = tk.OptionMenu(root, shape_var, "Rechteck", "Dreieck", "Kreis")
shape_menu.pack()

label_a = tk.Label(root, text="Seite a:")
label_a.pack(pady=(10, 5))
entry_a = tk.Entry(root)
entry_a.pack()

label_b = tk.Label(root, text="Seite b:")
label_b.pack(pady=(10, 5))
entry_b = tk.Entry(root)
entry_b.pack()

calc_button = tk.Button(root, text="Berechnen", command=calculate)
calc_button.pack(pady=15)

result_label = tk.Label(root, text="Fläche:")
result_label.pack(pady=5)

formula_label = tk.Label(root, text="Formel:")
formula_label.pack(pady=5)

update_inputs()

root.mainloop()