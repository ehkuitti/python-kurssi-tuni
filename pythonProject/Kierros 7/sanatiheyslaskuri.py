"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def count_amount_of_a_word():
    """Funktion tarkoituskena on tallentaa sanoja taulukkoon ja laskea niiden
    määriä."""
    amount_of_found_words = 0
    lenght_of_my_split_input = ""
    my_input = ""
    my_list = []
    my_lowercase_input = ""
    my_split_input = ""
    my_dict = {}
    is_input_valid = True
    word_count = 0

    print("Enter rows of text for word counting. Empty row to quit.")

    # Syötteen keräämistä jatketaan niin kauan, kunnes syötetään pelkkä enter
    while is_input_valid:

        my_input = input()

        if my_input == "":
            is_input_valid = False

        else:
            my_lowercase_input = my_input.lower()
            my_split_input \
                = my_lowercase_input.split()

        lenght_of_my_split_input = len(my_split_input)

        for i in range(0, lenght_of_my_split_input, 1):

            # Jos tiettyä sanaa ei löydy sanakirjasta, se lisätään sinne
            # avaimeksi. Sen arvoksi annetaan määrä, joka on indeksi + 1 (
            # indeksointi alkaa nollasta, positiivinen määrä ei).
            my_list.append(my_split_input[i])

            # Tällä koodilla listään arvoja
            # my_dict[my_split_input[i]] = my_split_input.count(
            #     my_split_input[i])



    print("My dict: ", my_dict)
    print("My list: ", my_list)


def main():

    count_amount_of_a_word()


if __name__ == "__main__":
    main()
