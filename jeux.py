import os
import random
import tkinter as tk
from PIL import Image, ImageTk

def example():
    data_in = entry.get()
    label.config(text=data_in)

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
        print("mot tres large")
        return
    for i, lettre in enumerate(mot):
        if lettre == mot_target[i]:
            mask[i] = 1

def est_gagner():
    return all(mask)

def jeux():
    global chance
    if chance <= 1:
        label2.config(text="Vous avez perdu bon homme mcha vchrab 3abdi.")
        canvas.itemconfigure(cadre_image, image=image_pils[(max_chance - chance + 1)])
        return
    mot_input = entry.get()
    evaluer(mot_input)
    faire_masker()
    if est_gagner():
        label2.config(text=f"Bravo!")
    else:
        chance -= 1
        label2.config(text=f"chance rester: {chance}")

    canvas.itemconfigure(cadre_image, image=image_pils[(max_chance - chance)])

window = tk.Tk()
window.title("Bon Homme")
window.geometry("500x500")

label = tk.Label(window)
label.pack()

canvas = tk.Canvas(window, width=500, height=400)
canvas.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="proposer", command=jeux)
button.pack()

label2 = tk.Label(window)
label2.pack()

print(sorted(os.listdir("./photos")))
image_pils = [Image.open("photos/" + path) for path in sorted(os.listdir("./photos"))]
image_pils = [ImageTk.PhotoImage(image) for image in image_pils]
cadre_image = canvas.create_image(250, 200, image=image_pils[0])

max_chance = 7
chance = max_chance
label2.config(text=f"chance rester: {max_chance}")

with open("./mot_franc_filtrer.txt", "r") as f:
    mots = f.read()

mots = mots.split("\n")
mot_target = random.choice(mots) 
print(mot_target)
mask = [0] * len(mot_target)
mask[0] = 1

label.config(text=faire_masker())

window.mainloop()
