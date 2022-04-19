"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""
"""
Calculates the area of a square. The length of the base is read in a loop
until it is greater than or equal to zero and of the correct type. A flag
variable controls the loop.
"""


def main():

    # MUUTTUJIEN ALUSTUKSET (AAKKOSJÄRJESTYKSESSÄ TYYPPIPAREITTAIN)
    height_of_the_frame = 0
    width_of_the_frame = 0

    inner_input = ""
    mark_input = ""
    outer_input = ""

    invalid_inner_input = True
    invalid_outer_input = True

    while invalid_outer_input:

        while invalid_inner_input:
            inner_input = input("Enter the width of a frame: ")

            try:
                width_of_the_frame = int(inner_input)

                if base_length > 0:
                    invalid_inner_input = False

                else:
                    continue

            except ValueError:
                continue

            except TypeError:
                continue

            # Sisemmän while-loopin koodi päättyy tähän

        outer_input = input("Enter the height of a frame: ")

        try:
            height_of_the_frame = int(outer_input)

            if base_length > 0:
                invalid_outer_input = False

            else:
                continue

        except ValueError:
            continue

        except TypeError:
            continue

    mark_input = input("Enter a print mark: ")




if __name__ == "__main__":
    main()