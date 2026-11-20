#Lium Powers, Computer Science,  11/__/2026

def tempConversion():
    with open("tempConv.txt", "w") as outfile:

        #Prints headers in file
        outfile.write(("Fahrenheit").center(10))
        outfile.write(("Celsius").center(10) + "\n")

        #goes for each temp from -300 to 212 fahrenhiet
        for i in range(512):
            fahr = (i - 300)
            cels = (((i - 300) - 32) * (5/9))
            outfile.write(str(fahr).center(10))
            #format, variable:.precision - fixed decimal
            outfile.write(str("{0:2.3f}".format(cels)).center(10) + "\n")

        outfile.close
            
tempConversion()
    