from tkinter import *


root = Tk() #przez to pojawia się okienko
root.geometry('800x700')   #to określa rozmiar okienka
root.title('Map Book')   #nazwanie aplikacji w lewym górnym rogu


ramka_lista_uzytkownikow = Frame(root) #tworzymy ramki w aplikacji
ramka_formulaz = Frame(root)
ramka_szczegoly_obiektu = Frame(root)

ramka_lista_uzytkownikow.grid(row=0, column=0)
ramka_formulaz.grid(row=0, column=1)
ramka_szczegoly_obiektu.grid(row=1, column=0)

# ramka_lista_obiektow
label_lista_obiektow = Label(ramka_lista_uzytkownikow, text= 'Lista znajomych: ')
listbox_lista_obiektow = Listbox(ramka_lista_uzytkownikow, width=30)
button_pokaz_szczegoly = Button(ramka_lista_uzytkownikow, text='Pokaż szczegóły')
button_usun_uzytkownika = Button(ramka_lista_uzytkownikow, text='Usuń ')
button_edytuj_uzytkownika = Button(ramka_lista_uzytkownikow, text='Edytuj ')

label_lista_obiektow = Label(ramka_formulaz, text= 'Formula: ')
listbox_lista_obiektow.grid(row=0, column=0, columnspan=3)
button_pokaz_szczegoly.grid(row=1, column=0)
button_usun_uzytkownika.grid(row=1, column=1)
button_edytuj_uzytkownika.grid(row=1, column=2)

# ramka_formulaz
label_formularz = Label(ramka_formulaz, text= 'Formularz edycji dodawania: ')
label_formularz.grid(row=0, column=0, columnspan=3)

#ramka_szczegoly_obiektow









root.mainloop()

