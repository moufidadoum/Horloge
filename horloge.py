import tkinter as tk
from tkinter import ttk, Label
from time import strftime
import datetime
from tkinter import messagebox

def horloge_heure():
    afficher_horloge['text'] = strftime(heuree)
    afficher_horloge.after(1000, horloge_heure)

def afficher_heure_24h():
    global heuree 
    heuree = '%H:%M:%S %p\n%b %d, %Y'
    boutton_24h["state"] = "disabled"
    boutton_12h["state"] = "normal"

def afficher_heure_12h():
    global heuree
    heuree = '%I:%M:%S %p\n%b %d, %Y'
    boutton_24h["state"] = "normal"
    boutton_12h["state"] = "disabled"

def regler_heure(heure):
    global heuree
    now = datetime.datetime.now()
    now = now.replace(hour=heure[0], minute=heure[1], second=heure[2])
    heuree = now.strftime('%H:%M:%S %p\n%b %d, %Y')
    afficher_horloge['text'] = heuree
    horloge_heure()

def ouvrir_fenetre_reglage():
    fenetre_reglage = tk.Toplevel(horloge)
    fenetre_reglage.title("Réglage de l'heure")

    heure_label = tk.Label(fenetre_reglage, text="Heure :")
    heure_label.grid(row=0, column=0)
    heure_entry = tk.Entry(fenetre_reglage)
    heure_entry.grid(row=0, column=1)

    minute_label = tk.Label(fenetre_reglage, text="Minute :")
    minute_label.grid(row=1, column=0)
    minute_entry = tk.Entry(fenetre_reglage)
    minute_entry.grid(row=1, column=1)

    seconde_label = tk.Label(fenetre_reglage, text="Seconde :")
    seconde_label.grid(row=2, column=0)
    seconde_entry = tk.Entry(fenetre_reglage)
    seconde_entry.grid(row=2, column=1)

    soumettre_bouton = tk.Button(fenetre_reglage, text="OK", command=lambda: regler_heure((int(heure_entry.get()), int(minute_entry.get()), int(seconde_entry.get()))))
    soumettre_bouton.grid(row=3, column=0)
    annuler_bouton = tk.Button(fenetre_reglage, text="Annuler", command=fenetre_reglage.destroy)
    annuler_bouton.grid(row=3, column=1)

horloge = tk.Tk()

horloge.title('Horloge')
horloge.geometry('800x600')
horloge.resizable(False, False)
tabControl = ttk.Notebook(horloge)
clock_tab = ttk.Frame(tabControl)

tabControl.add(clock_tab)
tabControl.pack(expand=1, fill="both")


afficher_horloge = Label(clock_tab,fg='black', font=("arial", 80))
afficher_horloge.place(x=50, y=200)

clock_label = Label(clock_tab,fg='black',font=("arial", 60, 'bold'), text = 'Horloge :')
clock_label.place(x=150, y=100)

boutton_24h = tk.Button(clock_tab,text="Format 24 heures",bd=10,bg="white", fg="blue",command=afficher_heure_24h,activeforeground="Orange",activebackground="blue",font="Andalus",height=2,highlightcolor="purple",justify="right",state = 'normal')
boutton_24h.place(x=50, y=470)

boutton_12h = tk.Button(clock_tab,text="Format 12 heures",bd=10,bg="white", fg="blue",command=afficher_heure_12h,activeforeground="Orange",activebackground="blue",font="Andalus",height=2,highlightcolor="purple",justify="right",state= 'disabled')
boutton_12h.place(x=250, y=470)

regler_heure_bouton = tk.Button(clock_tab,text="Régler l'heure",bd=10,bg="white", fg="blue",command=ouvrir_fenetre_reglage,activeforeground="Orange",activebackground="blue",font="Andalus",height=2,highlightcolor="purple",justify="right",state= 'normal')
regler_heure_bouton.place(x=450, y=470)

	
afficher_heure_12h()
horloge_heure()
horloge.mainloop()