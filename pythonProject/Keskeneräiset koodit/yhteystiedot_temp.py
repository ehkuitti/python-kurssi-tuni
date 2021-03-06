"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def read_file(str_tiedostonimi):
    # MUUTTUJIEN ALUSTUKSET (MUUTTUJATYYPPEINEEN)

    # LISTAT
    lst_kontaktit = []

    # MERKKIJONOT
    str_stripattu_avain = ""
    str_stripattu_nimi = ""
    str_stripattu_puhnro = ""
    str_stripattu_email = ""
    str_stripattu_skype = ""

    # SANAKIRJAT
    dict_kontaktit = {}
    dict_arvot = {}

    # TOTUUSARVOT
    skype_puuttuu = False

    try:
        tiedosto = open(str_tiedostonimi, mode="r")

    except OSError:
        print(f"Error: Opening the file '{str_tiedostonimi} failed!")
        return

    for rivi in tiedosto:
        # Splitataan tiedoston yksittäinen rivi alkiotaulukoksi puolipisteen
        # kohdalta
        lst_kontaktit = rivi.split(";", maxsplit=-1)

        # Stripataan tiedostot whitespaceistä
        str_stripattu_avain = lst_kontaktit[0].strip()
        str_stripattu_nimi = lst_kontaktit[1].strip()
        str_stripattu_puhnro = lst_kontaktit[2].strip()
        str_stripattu_email = lst_kontaktit[3].strip()
        str_stripattu_skype = lst_kontaktit[4].strip()

        if str_stripattu_skype == "":
            skype_puuttuu = True

        for avain in dict_kontaktit:
            dict_kontaktit[str_stripattu_avain] = dict_arvot

            if skype_puuttuu:
                dict_arvot[name] = str_stripattu_nimi
                dict_arvot[phone] = str_stripattu_puhnro
                dict_arvot[email] = str_stripattu_email

            # Jos Skype ei ei-puutu eli Skype on tiedossa
            elif not skype_puuttuu:
                dict_arvot[name] = str_stripattu_nimi
                dict_arvot[phone] = str_stripattu_puhnro
                dict_arvot[email] = str_stripattu_email
                dict_arvot[skype] = str_stripattu_skype

        syote = input()
        splitattu_syote = syote.split("]")
        syote_avain = splitattu_syote[0]
        syote_arvo = splitattu_syote[1]
        #
        # for avain, arvo in dict_kontaktit.items()
        #     if avain == syote_avain:
        #         for alkio in dict_arvot:
        #             dict_kontaktit


def main():
    str_tiedostonimi = ""
    str_tiedostonimi = input("Syötä tiedostonimi: ")

    read_file(str_tiedostonimi)


if __name__ == "__main__":
    main()
