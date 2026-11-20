#Lium Powers, Python programming, 11/19/2026

#Takes input from a file and makes it uppercase, printing to a new file
def toUpper():
    with open("regulartext.txt", "r") as regular:
        with open("uppercase.txt", "w") as upper:

            #takes input of file and stores it as a string
            file = regular.read()
            out = upper.write(file.upper() + " ")


toUpper()