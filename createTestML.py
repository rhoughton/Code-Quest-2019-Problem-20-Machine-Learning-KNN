import random
import math
class aBird():
    def __init__(abird):
        abird.length = round(random.uniform(12.3,21.38), 2)
        abird.width = round(random.uniform(5.17,8.66), 2)
        abird.wingspan = round(random.uniform(20.09,25.32), 2)
        abird.wingangle = round(random.uniform(88.51,89.04), 2)
class pBird():
    def __init__(pbird):
        pbird.length = round(random.uniform(13.34,20.03), 2)
        pbird.width = round(random.uniform(6.24,8.86), 2)
        pbird.wingspan = round(random.uniform(20.97,26.46), 2)
        pbird.wingangle = round(random.uniform(88.95,89.35), 2)
class cBird():
    def __init__(cbird):
        cbird.length = round(random.uniform(13.61,19.19), 2)
        cbird.width = round(random.uniform(5.33,7.74), 2)
        cbird.wingspan = round(random.uniform(20.64,24.59), 2)
        cbird.wingangle = round(random.uniform(88.09,90.21), 2)
class unknownBird():
    def __init__(unknownbird):
        unknownbird.length = round(random.uniform(12.3,21.38), 2)
        unknownbird.width = round(random.uniform(5.17,8.86), 2)
        unknownbird.wingspan = round(random.uniform(20.09,26.46), 2)
        unknownbird.wingangle = round(random.uniform(88.09,90.21), 2)
        

cases = 4

file = open ("birdinputfile.txt", "w")
file.write(str(cases) + "\n")

for i in range (cases):
    knownBirdsCases = 90 #random.randint(30, 100) #Preferably a large sample size that's a multiple of 3
    unknownBirdsCases = random.randint(1,10)
    g = round(knownBirdsCases/3)
    gx = g
    gy = g
    gz = g
    file.write(str(knownBirdsCases) + " " + str(unknownBirdsCases) + "\n")
    for i in range (knownBirdsCases):
        x = aBird()
        y = pBird()
        z = cBird()
        birdPicker = random.randint(1,3)
        if(birdPicker == 1 and gx > 0):
            file.write("Accipitridae " + str(x.length) + " " + str(x.width) + " " + str(x.wingspan) + " " + str(x.wingangle) + "\n")
            gx -= 1
        if(birdPicker == 2 and gy > 0):
            file.write("Passeridae " + str(y.length) + " " + str(y.width) + " " + str(y.wingspan) + " " + str(y.wingangle) + "\n" )
            gy -= 1
        if(birdPicker == 3 and gz > 0):
            file.write("Cathartidae " + str(z.length) + " " + str(z.width) + " " + str(z.wingspan) + " " + str(z.wingangle) + "\n" )
            gz -= 1
        elif (gy > 0):
            file.write("Passeridae " + str(y.length) + " " + str(y.width) + " " + str(y.wingspan) + " " + str(y.wingangle) + "\n" )
            gy -= 1
        elif (gz > 0):
            file.write("Cathartidae " + str(z.length) + " " + str(z.width) + " " + str(z.wingspan) + " " + str(z.wingangle) + "\n" )
            gz -= 1
        elif (gx > 0):
            file.write("Accipitridae " + str(y.length) + " " + str(y.width) + " " + str(y.wingspan) + " " + str(y.wingangle) + "\n" )
            gx -= 1
    for i in range(unknownBirdsCases):
        w = unknownBird()
        file.write(str(w.length) + " " + str(w.width) + " " + str(w.wingspan) + " " + str(w.wingangle) + "\n")
file.close()








