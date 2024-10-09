import os
import random
import tkinter as tk
from PIL import Image, ImageTk

def faire_masker():
    mot = ""
    for i, bit in enumerate(mask):
        if bit:
            mot += mot_target[i]
        else:
            mot += "_"
    label.config(text=mot)

def evaluer(mot):
    if len(mot) > len(mot_target):
        label_err.config(text="mot tres large")
        return
    for i, lettre in enumerate(mot):
        if lettre == mot_target[i]:
            mask[i] = 1

def est_gagner():
    return all(mask)

def jeux():
    global chance
    if chance <= 1:
        label2.config(text="Vous avez perdu bon homme mcha vchrab 3abdi.", fg="#846134")
        canvas.itemconfigure(cadre_image, image=image_pils[(max_chance - chance + 1)])
        return
    mot_input = entry.get()
    label_err.config(text="")
    evaluer(mot_input)
    faire_masker()
    if est_gagner():
        label2.config(text=f"Bravo!", fg="green", font=("Ariel", 14))
    else:
        chance -= 1

    canvas.itemconfigure(cadre_image, image=image_pils[(max_chance - chance)])

window = tk.Tk()
window.title("Bon Homme")
window.geometry("900x500")
couleur = "#3c3e43"
window.configure(bg=couleur)

frame_gauche = tk.Frame(window, bg=couleur)
frame_gauche.pack(side="left")

label = tk.Label(frame_gauche, bg=couleur, fg="#AAAAAA", font=("Ariel", 20))
label.grid(row=0, column=0, padx=10, pady=100)

entry = tk.Entry(frame_gauche)
entry.grid(row=1, column=0, padx=10, pady=10)

button = tk.Button(frame_gauche, text="proposer", command=jeux)
button.grid(row=1, column=1, padx=10, pady=20)

label2 = tk.Label(frame_gauche, fg="#AAAAAA", bg=couleur, font=("Ariel", 12))
label2.grid(row=2, column=0, padx=10, pady=10)

label_err = tk.Label(frame_gauche, fg="#AA1111", bg=couleur, font=("Ariel", 12))
label_err.grid(row=3, column=0, padx=10, pady=10)

canvas = tk.Canvas(window, width=400, height=400, bg=couleur, highlightthickness=0)
canvas.pack(side="right", padx=10)

image_pils = [Image.open("photos/" + path) for path in sorted(os.listdir("./photos"))]
image_pils = [ImageTk.PhotoImage(image) for image in image_pils]
cadre_image = canvas.create_image(250, 200, image=image_pils[0])

max_chance = 7
chance = max_chance
label2.config(text="proposer une lettre")

with open("./mot_franc_filtrer.txt", "r") as f:
    mots = f.read()

mots = mots.split("\n")
mot_target = random.choice(mots) 
print(mot_target)
mask = [0] * len(mot_target)
mask[0] = 1

label.config(text=faire_masker())

window.mainloop()
