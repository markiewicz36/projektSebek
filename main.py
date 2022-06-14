import csv
import random

class Baza:
    def __init__(self):
        self.listaOsob = []
        self.listaSamochodow = []

    def dodajOsobe(self):
        print("-------------------------------\nUzupełnij dane:")
        imie = input("Imię:")
        nazwisko = input("Nazwisko:")
        wiek = input("Wiek:")
        try:
            nowaOsoba = Osoba(imie, nazwisko, wiek)
        except ValueError:
            print("Nie udało się dodać użytkownika!")
        self.listaOsob.append(nowaOsoba)

    def usunOsobe(self):
        print("-------------------------------\nWpisz ID użytkownika:")
        id = input("ID:")
        for x, i in enumerate(self.listaOsob):
            if i.id == id:
                try:
                    self.listaOsob.remove(i)
                    print("Usunięto!")
                except ValueError:
                    print("Błąd!")


    def wypiszUzytkownikow(self):
        print("-------------------------------\nLista użytkowników:")
        for x, i in enumerate(self.listaOsob):
            print(i.id,i.imie,i.nazwisko)

    def dodajSamochod(self):
        print("-------------------------------\nUzupełnij dane:")
        marka = input("Marka:")
        model = input("Model:")
        try:
            nowySamochod = Samochod(marka, model)
        except ValueError:
            print("Nie udało się dodać samochodu!")
        self.listaSamochodow.append(nowySamochod)

    def wypiszSamochody(self):
        print("-------------------------------\nLista samochodów:")
        for x, i in enumerate(self.listaSamochodow):
            print(x+1,i.marka, i.model, i.wlasciciel)

    def zapiszDoPliku(self):
        with open('D:\\projektSebek\\uzytkownicy.csv', mode='w') as plik_uzytkownikow:
            for i in self.listaOsob:
                zapis = csv.writer(plik_uzytkownikow, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
                zapis.writerow([i.imie, i.nazwisko, i.wiek, i.id])

        pustaLinia = ""
        with open("D:\\projektSebek\\uzytkownicy.csv") as f:
            for i in f:
                if not i.isspace():
                    pustaLinia += i
        f = open("D:\\projektSebek\\uzytkownicy.csv", "w")
        f.write(pustaLinia)

    def wczytajPlik(self):
        self.listaOsob.clear()
        with open('D:\\projektSebek\\uzytkownicy.csv') as plik_uzytkownikow:
            plik_uzytkownikow = csv.reader(plik_uzytkownikow, delimiter=',')
            licznik = 0
            for i in plik_uzytkownikow:
                tmp = Osoba(f'{i[0]}', f'{i[1]}', f'{i[2]}')
                tmp.set_id(f'{i[3]}')
                self.listaOsob.append(tmp)
                licznik += 1
            print(f'Wczytano {licznik} użytkowników.')

baza = Baza()


class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.listaSamochodow = []
        self.id = random.randint(0, 10000)

    def informacjeOsoba(self):
        print("-------------------------------")
        print(f"Imie: {self.imie} \nNazwisko {self.nazwisko}")

    def dodajSamochod(self, samochod):
        print("-------------------------------")
        self.listaSamochodow.append(samochod)
        print("Samochod dodany do użytkownika!")

    def sprawdzSamochody(self):
        print("-------------------------------")
        print(
            f"Użytkownik {self.imie} posiada {(len(self.listaSamochodow))} samochodów. \nLista posiadanych samochodów:")
        for i in self.listaSamochodow:
            print(i.marka)

    def set_id(self, id):
        self.id = id

class Samochod:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
        self.wlasciciel = "brak"

    def informacjaSamochod(self):
        print("-------------------------------")
        print(f"Marka: {self.marka} \nModel: {self.model}\nWłaściciel: {self.wlasciciel}")

    def ustawWlasciciela(self, osoba):
        print("-------------------------------")
        self.wlasciciel = osoba
        print("Właściciel zaktualizowany!")


def wyborMenu(wybor):
    while True:
        if wybor == '1':
            print("-------------------------------")
            print("1. Dodaj użytkownika")
            print("2. Usuń użytkownika")
            print("3. Wypisz użytkowników")
            print("4. Zapisz do pliku")
            print("5. Wczytaj plik")
            print("6. Menu główne")
            wyborTmp = input("Wybór:")
            if wyborTmp == '1':
                baza.dodajOsobe()
            elif wyborTmp == '2':
                baza.usunOsobe()
            elif wyborTmp == '3':
                baza.wypiszUzytkownikow()
            elif wyborTmp == '4':
                baza.zapiszDoPliku()
            elif wyborTmp == '5':
                baza.wczytajPlik()
            elif wyborTmp == '6':
                menu()
        elif wybor == '2':
            print("2")
        elif wybor == '3':
            exit(0)


def menu():
    while True:
        print("-------------------------------")
        print("Witaj w bazie danych wypożyczalni samochodowej!\nWybierz co chcesz zrobić:")
        print("-------------------------------")
        print("1. Operacje na użytkownikach")
        print("2. Operacje na samochodach")
        print("3. Wyjście")
        print("-------------------------------")
        wybor = input("Wybór:")
        wyborMenu(wybor)


if __name__ == '__main__':
    menu()
