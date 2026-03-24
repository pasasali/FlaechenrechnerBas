import tkinter as tk


# ── Flächenrechner (links) ──────────────────────────────────────────────────

def calculate_area():
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
            area_result_label.config(text="Bitte eine Form auswählen.")
            return
        area_result_label.config(text=f"Fläche: {area:.2f}")
        area_formula_label.config(text=f"Formel: {formula}")
    except ValueError:
        area_result_label.config(text="Bitte gültige Zahlen eingeben.")
        area_formula_label.config(text="Formel:")


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


# ── Volumenberechnung (rechts) ─────────────────────────────────────────────

def update_volume_inputs(*args):
    koerper = koerper_var.get()
    if koerper == "Kugel":
        vol_label_a.config(text="Radius r:")
        vol_label_b.config(text="-")
        vol_label_c.config(text="-")
        vol_entry_b.delete(0, tk.END)
        vol_entry_b.config(state="disabled")
        vol_entry_c.delete(0, tk.END)
        vol_entry_c.config(state="disabled")
    else:  # Quader
        vol_label_a.config(text="Seite a:")
        vol_label_b.config(text="Seite b:")
        vol_label_c.config(text="Seite c:")
        vol_entry_b.config(state="normal")
        vol_entry_c.config(state="normal")


def calculate_volume():
    try:
        koerper = koerper_var.get()
        if koerper == "Quader":
            a = float(vol_entry_a.get())
            b = float(vol_entry_b.get())
            c = float(vol_entry_c.get())
            volume = a * b * c
            formula = f"V = a · b · c = {a} · {b} · {c} = {volume:.2f}"
        elif koerper == "Kugel":
            r = float(vol_entry_a.get())
            volume = (4 / 3) * 3.14159 * r ** 3
            formula = f"V = (4/3) · π · r³ = (4/3) · 3.14159 · {r}³ = {volume:.2f}"
        else:
            vol_result_label.config(text="Bitte einen Körper auswählen.")
            return
        vol_result_label.config(text=f"Volumen: {volume:.2f}")
        vol_formula_label.config(text=f"Formel: {formula}")
    except ValueError:
        vol_result_label.config(text="Bitte gültige Zahlen eingeben.")
        vol_formula_label.config(text="Formel:")


# ── Fenster & Layout ───────────────────────────────────────────────────────

root = tk.Tk()
root.title("Flächen- und Volumenrechner")
root.geometry("700x380")

main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

left_frame = tk.Frame(main_frame, bd=1, relief="groove")
left_frame.pack(side="left", fill="both", expand=True, padx=(0, 5))

right_frame = tk.Frame(main_frame, bd=1, relief="groove")
right_frame.pack(side="right", fill="both", expand=True, padx=(5, 0))

# ── Linke Seite: Flächenrechner ────────────────────────────────────────────

tk.Label(left_frame, text="Flächenrechner", font=("Arial", 11, "bold")).pack(pady=(8, 4))

shape_var = tk.StringVar(value="Rechteck")
shape_var.trace_add("write", update_inputs)

tk.Label(left_frame, text="Form auswählen:").pack(pady=(4, 2))
tk.OptionMenu(left_frame, shape_var, "Rechteck", "Dreieck", "Kreis").pack()

label_a = tk.Label(left_frame, text="Seite a:")
label_a.pack(pady=(8, 2))
entry_a = tk.Entry(left_frame)
entry_a.pack()

label_b = tk.Label(left_frame, text="Seite b:")
label_b.pack(pady=(6, 2))
entry_b = tk.Entry(left_frame)
entry_b.pack()

tk.Button(left_frame, text="Fläche berechnen", command=calculate_area).pack(pady=10)

area_result_label = tk.Label(left_frame, text="Fläche:")
area_result_label.pack(pady=2)
area_formula_label = tk.Label(left_frame, text="Formel:", wraplength=280)
area_formula_label.pack(pady=2)


# ── Rechte Seite: Volumenberechnung ───────────────────────────────────────

tk.Label(right_frame, text="Volumenberechnung", font=("Arial", 11, "bold")).pack(pady=(8, 4))

koerper_var = tk.StringVar(value="Quader")
koerper_var.trace_add("write", update_volume_inputs)

tk.Label(right_frame, text="Körper auswählen:").pack(pady=(4, 2))
tk.OptionMenu(right_frame, koerper_var, "Quader", "Kugel").pack()

vol_label_a = tk.Label(right_frame, text="Seite a:")
vol_label_a.pack(pady=(8, 2))
vol_entry_a = tk.Entry(right_frame)
vol_entry_a.pack()

vol_label_b = tk.Label(right_frame, text="Seite b:")
vol_label_b.pack(pady=(4, 2))
vol_entry_b = tk.Entry(right_frame)
vol_entry_b.pack()

vol_label_c = tk.Label(right_frame, text="Seite c:")
vol_label_c.pack(pady=(4, 2))
vol_entry_c = tk.Entry(right_frame)
vol_entry_c.pack()

tk.Button(right_frame, text="Volumen berechnen", command=calculate_volume).pack(pady=10)

vol_result_label = tk.Label(right_frame, text="Volumen:")
vol_result_label.pack(pady=2)
vol_formula_label = tk.Label(right_frame, text="Formel:", wraplength=280)
vol_formula_label.pack(pady=2)

# ── Start ──────────────────────────────────────────────────────────────────

update_inputs()
update_volume_inputs()

root.mainloop()
