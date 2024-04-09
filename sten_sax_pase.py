from random import choice

# Lista med val
val = ["sten", "sax", "påse"]

def spela_sten_sax_pase():
    points_spelare = 0
    points_dator = 0
    while True:
        # Användarens val sparas i små bokstäver
        anv_val = input(f"Välj mellan {(", ".join(val))} (exit för att avsluta): ").lower()
        if anv_val == "exit":
            break
        if anv_val not in val:
            print("Felaktigt val, försök igen")
            continue
        # Datorns slumpade val
        dat_val = choice(val)

        # Visa valen
        print(f"Du valde {anv_val}")
        print(f"Datorn valde {dat_val}")

        #Utvärderar först om spelaren vinner, sen om dator och spelare valt samma, annars vinner datorn
        vinnare = (anv_val + " " + dat_val)
        if vinnare in ("sten sax", "sax påse", "påse sten"):
            points_spelare += 1
            print("Du vann!")
        elif anv_val == dat_val:
            print("Oavgjort!")
        else:
            print("Datorn vann!")
            points_dator += 1

        # Visa poäng
        print(f"Poäng: Du - {points_spelare}, Dator - {points_dator}")

spela_sten_sax_pase()
