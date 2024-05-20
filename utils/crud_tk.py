from tkinter import *
import requests
from bs4 import BeautifulSoup
import tkintermapview


def dodaj_uzytkownika():
    imie = entry_imie.get()
    nazwisko = entry_nazwisko.get()
    posty = entry_posty.get()
    miejscowosc = entry_miejscowosc.get()
    user = User(imie, nazwisko, posty, miejscowosc)

    users.append(user)
    print(user.imie)
    lista_uzytkownikow()
    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_posty.delete(0, END)
    entry_miejscowosc.delete(0, END)
    entry_imie.focus()


def lista_uzytkownikow():
    listbox_lista_obiektow.delete(0, END)
    for idx, user in enumerate(users):
        listbox_lista_obiektow.insert(idx, f'{user.imie} {user.nazwisko}')


def pokaz_szczegoly_uzytkownika():
    i = listbox_lista_obiektow.index(ACTIVE)
    print(i)
    imie = users[i].imie
    nazwisko = users[i].nazwisko
    posty = users[i].posty
    miejscowosc = users[i].miejscowosc
    map_widget.set_position(users[i].coords[0], users[i].coords[1])
    map_widget.set_zoom(15)

    label_imie_szczegoly_wartosc.config(text=imie)
    label_nazwisko_szczegoly_wartosc.config(text=nazwisko)
    label_posty_szczegoly_wartosc.config(text=posty)
    label_miejscowosc_szczegoly_wartosc.config(text=miejscowosc)


def usun_uzytkownika():
    i = listbox_lista_obiektow.index(ACTIVE)
    users[i].marker.delete()
    users.pop(i)
    lista_uzytkownikow()


def edytuj_uzytkownika():
    i = listbox_lista_obiektow.index(ACTIVE)
    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_posty.delete(0, END)
    entry_miejscowosc.delete(0, END)

    entry_imie.insert(0, users[i].imie)
    entry_nazwisko.insert(0, users[i].nazwisko)
    entry_posty.insert(0, users[i].posty)
    entry_miejscowosc.insert(0, users[i].miejscowosc)
    button_dodaj_uzytkownika.config(text="Zapisz zmiany", command=lambda: aktualizuj_uzytkownika(i))


def aktualizuj_uzytkownika(i):
    users[i].imie = entry_imie.get()
    users[i].nazwisko = entry_nazwisko.get()
    users[i].posty = entry_posty.get()
    users[i].miejscowosc = entry_miejscowosc.get()
    users[i].coords = User.get_coords(users[i])
    users[i].marker.delete()
    users[i].marker = map_widget.set_marker(users[i].coords[0], users[i].coords[1], text=f"{users[i].imie}")
    lista_uzytkownikow()

    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_posty.delete(0, END)
    entry_miejscowosc.delete(0, END)

    button_dodaj_uzytkownika.config(text='Dodaj uzytkownika', command=dodaj_uzytkownika)