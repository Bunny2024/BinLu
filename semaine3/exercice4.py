# affiche une table de carrés et de cubes pour une gamme de nombres donnée.

print("Table of Powers\n")

while True:
# utilisateur donne un start number
    start_number = int(input("Start number:"))
    stop_number = int(input("Stop number:"))

    print("\nNumber\tSquared\tCubed")
    print("======\t=======\t=====")
    if stop_number < start_number:
        print("Start number must be less than stop number.")
    else:
        for i in range(start_number, stop_number + 1):
            square = i ** 2
            cube = i ** 3
            print(f"{i}\t{square}\t{cube}")
        break



