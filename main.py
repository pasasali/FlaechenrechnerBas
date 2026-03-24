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

        history_entry = f"{shape}: {formula} = {area:.2f}"
        history_listbox.insert(0, history_entry)

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


def clear_history():
    history_listbox.delete(0, tk.END)


root = tk.Tk()
root.title("Flaechenrechner")
root.geometry("650x350")

# Main layout: left frame + right frame
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

left_frame = tk.Frame(main_frame)
left_frame.pack(side="left", fill="both", expand=True)

right_frame = tk.Frame(main_frame, bd=1, relief="sunken")
right_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))

# --- Left side (existing UI) ---
shape_var = tk.StringVar(value="Rechteck")
shape_var.trace_add("write", update_inputs)

tk.Label(left_frame, text="Form auswählen:").pack(pady=(10, 5))
shape_menu = tk.OptionMenu(left_frame, shape_var, "Rechteck", "Dreieck", "Kreis")
shape_menu.pack()

label_a = tk.Label(left_frame, text="Seite a:")
label_a.pack(pady=(10, 5))
entry_a = tk.Entry(left_frame)
entry_a.pack()

label_b = tk.Label(left_frame, text="Seite b:")
label_b.pack(pady=(10, 5))
entry_b = tk.Entry(left_frame)
entry_b.pack()

calc_button = tk.Button(left_frame, text="Berechnen", command=calculate)
calc_button.pack(pady=15)

result_label = tk.Label(left_frame, text="Fläche:")
result_label.pack(pady=5)

formula_label = tk.Label(left_frame, text="Formel:")
formula_label.pack(pady=5)

# --- Right side (history Listbox) ---
tk.Label(right_frame, text="Verlauf", font=("Arial", 10, "bold")).pack(pady=(8, 4))

history_listbox = tk.Listbox(right_frame, width=35, height=12)
history_listbox.pack(padx=8, pady=(0, 5), fill="both", expand=True)

clear_button = tk.Button(right_frame, text="Verlauf löschen", command=clear_history)
clear_button.pack(pady=(0, 8))

update_inputs()

root.mainloop()
