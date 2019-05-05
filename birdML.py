import math
#Toggle these to test with CodeQuestInput.txt or birdinputfile.txt
#with open("CodeQuestInput.txt", "rt") as inputFile:
with open("birdinputfile.txt", "rt") as inputFile:
    cases = int(inputFile.readline())
    
    abirdList= []
    abirdMasterList = []
    pbirdList = []
    pbirdMasterList = []
    cbirdList = []
    cbirdMasterList = []
    unknownbirdList = []
    abirdLengthList = []
    abirdWidthList = []
    abirdSpanList = []
    abirdAngleList = []
    pbirdLengthList = []
    pbirdWidthList = []
    pbirdSpanList = []
    pbirdAngleList = []
    cbirdLengthList = []
    cbirdWidthList = []
    cbirdSpanList = []
    cbirdAngleList = []
    abirdDistanceList = []
    pbirdDistanceList = []
    cbirdDistanceList = []
    c = []
    d = 0
    for caseNum in range (cases):
        print("Case: "  + str(caseNum + 1))
        birdAmount = (inputFile.readline())
        for i in range(len(birdAmount)):
            if (birdAmount[i] == " "):
                d = i
        knownBirds = (int(birdAmount[0:d]))
        unknownBirds = (int(birdAmount[d:len(birdAmount)]))
        """Test for the type of bird and insert into bird type list with only numerical data"""
        for i in range(knownBirds):    #this allows for the loop to run through only as many times as there are known birds so that the data tests stay consistent
            a = (inputFile.readline())
            if (a[0] == "A"):
                b = []
                for i in range (len(a)):
                    if (a[i] == " "):
                        b.append(i)
                for i in range(0,4):
                    if (i < 3):
                        abirdList.append(a[b[i]+1: b[i+1]])
                    if (i == 3):
                        abirdList.append(a[b[i]: len(a)-1])
                abirdMasterList.append(abirdList)
                abirdList = []
            if (a[0] == "P"):
                b = []
                for i in range (len(a)):
                    if (a[i] == " "):
                        b.append(i)
                for i in range(0,4):
                    if (i < 3):
                        pbirdList.append(a[b[i]+1: b[i+1]])
                    if (i == 3):
                        pbirdList.append(a[b[i]: len(a)-1])
                pbirdMasterList.append(pbirdList)
                pbirdList = []
            if (a[0] == "C"):
                b = []
                for i in range (len(a)):
                    if (a[i] == " "):
                        b.append(i)
                for i in range(0,4):
                    if (i < 3):
                        cbirdList.append(a[b[i]+1: b[i+1]])
                    if (i == 3):
                        cbirdList.append(a[b[i]: len(a)-1])
                cbirdMasterList.append(cbirdList)
                cbirdList = []

        
        """Insert data from each bird type into an overall categorical list for a total of 12 lists (3 bird types and 4 data types)"""
        for i in range (len(abirdMasterList)):
                abirdLengthList.append(abirdMasterList[i][0])
        for i in range (len(abirdMasterList)):
                abirdWidthList.append(abirdMasterList[i][1])
        for i in range (len(abirdMasterList)):
                abirdSpanList.append(abirdMasterList[i][2])
        for i in range (len(abirdMasterList)):
                abirdAngleList.append(abirdMasterList[i][3])

        for i in range (len(pbirdMasterList)):
                pbirdLengthList.append(pbirdMasterList[i][0])
        for i in range (len(pbirdMasterList)):
                pbirdWidthList.append(pbirdMasterList[i][1])
        for i in range (len(pbirdMasterList)):
                pbirdSpanList.append(pbirdMasterList[i][2])
        for i in range (len(pbirdMasterList)):
                pbirdAngleList.append(pbirdMasterList[i][3])

        for i in range (len(cbirdMasterList)):
                cbirdLengthList.append(cbirdMasterList[i][0])
        for i in range (len(cbirdMasterList)):
                cbirdWidthList.append(cbirdMasterList[i][1])
        for i in range (len(cbirdMasterList)):
                cbirdSpanList.append(cbirdMasterList[i][2])
        for i in range (len(cbirdMasterList)):
                cbirdAngleList.append(cbirdMasterList[i][3])
        """Test for unknown birds. The first for loop ensures that the loop goes through only as many times as their are unknown birds."""
        for i in range (unknownBirds):
            a = (inputFile.readline())
            b = []
            """Creates a list of only the tested unknown bird's four data points"""
            for i in range (len(a)):
                if (a[i] == " "):
                    b.append(i)
            unknownbirdList.append(a[0:b[0]])
            for i in range(0,3):
                if (i < 2):
                    unknownbirdList.append(a[b[i]+1: b[i+1]])
                if (i == 2):
                    unknownbirdList.append(a[b[i]+1: len(a)-1])
            """creates a list of distances for each known bird of a certain type as compared to the currently tested unknown bird"""
            for i in range (len(abirdMasterList)):
                distance = round(math.sqrt(pow((float(unknownbirdList[0])-float(abirdLengthList[i])),2) + pow((float(unknownbirdList[1])-float(abirdWidthList[i])),2) + pow((float(unknownbirdList[2])-float(abirdSpanList[i])),2) + pow((float(unknownbirdList[3])-float(abirdAngleList[i])),2)), 2)
                abirdDistanceList.append(distance)
            

            for i in range (len(pbirdMasterList)):
                distance = round(math.sqrt(pow((float(unknownbirdList[0])-float(pbirdLengthList[i])),2) + pow((float(unknownbirdList[1])-float(pbirdWidthList[i])),2) + pow((float(unknownbirdList[2])-float(pbirdSpanList[i])),2) + pow((float(unknownbirdList[3])-float(pbirdAngleList[i])),2)), 2)
                pbirdDistanceList.append(distance)


            for i in range (len(cbirdMasterList)):
                distance = round(math.sqrt(pow((float(unknownbirdList[0])-float(cbirdLengthList[i])),2) + pow((float(unknownbirdList[1])-float(cbirdWidthList[i])),2) + pow((float(unknownbirdList[2])-float(cbirdSpanList[i])),2) + pow((float(unknownbirdList[3])-float(cbirdAngleList[i])),2)), 2)
                cbirdDistanceList.append(distance)

            
            distanceMasterList = []
            for i in range (len(abirdDistanceList)):
                distanceMasterList.append(abirdDistanceList[i])
            for i in range (len(pbirdDistanceList)):
                distanceMasterList.append(pbirdDistanceList[i])
            for i in range (len(cbirdDistanceList)):
                distanceMasterList.append(cbirdDistanceList[i])
            f = [] #Position in distanceMasterList where the min values are taken from as to discern which type of bird it is based on the order the Master list had the xbirdDistanceLists inserted
            k5 = [] #five min data points from which the votes are derived from
            distanceMasterListCopy = []
            for i in range (len(distanceMasterList)):
                distanceMasterListCopy.append(distanceMasterList[i])
            """This checks for the min values of the combined distance lists and records their locations from the master list"""
            for i in range (5):
                k5.append(min(distanceMasterListCopy))
                for i2 in range (len(distanceMasterList)):
                    if (min(distanceMasterListCopy) == distanceMasterList[i2]):
                        f.append(i2)
                distanceMasterListCopy.remove(min(distanceMasterListCopy))
            ak = 0
            pk = 0
            ck = 0
            """Based off the recorded locations, we are able to find which type of bird the min value came from and add a vote for it in the variable K of the respective bird"""
            for i in range (len(f)):
                if (f[i] >= 0 and f[i] <= (len(abirdDistanceList)-1)):
                    ak += 1
                elif (f[i] >= len(abirdDistanceList) and f[i] <= (len(abirdDistanceList) + len(pbirdDistanceList)-1)):
                    pk += 1
                elif (f[i] >= (len(abirdDistanceList) + len(pbirdDistanceList)) and f[i] <= (len(abirdDistanceList) + len(pbirdDistanceList) + len(cbirdDistanceList)-1)):
                    ck += 1
                
            
            """Since k only takes the 5 minimum points, it's possible for there to be a tie on the amount of minimum distances for bird types. This while loop increments k by 1 until the tie is broken."""
            while (ak == pk or ak == ck or pk == ck):
                if (distanceMasterListCopy == []):
                    print("Tie: Insufficient Sample Size")
                    break
                k5.append(min(distanceMasterListCopy))
                for i2 in range (len(distanceMasterList)):
                    if (min(distanceMasterListCopy) == distanceMasterList[i2]):
                        f.append(i2)
                distanceMasterListCopy.remove(min(distanceMasterListCopy))
                if (f[len(f)-1] >= 0 and f[len(f)-1] <= (len(abirdDistanceList)-1)):
                    ak += 1
                elif (f[len(f)-1] >= len(abirdDistanceList) and f[len(f)-1] <= (len(abirdDistanceList) + len(pbirdDistanceList)-1)):
                    pk += 1
                elif (f[len(f)-1] >= (len(abirdDistanceList) + len(pbirdDistanceList)) and f[len(f)-1] <= (len(abirdDistanceList) + len(pbirdDistanceList) + len(cbirdDistanceList)-1)):
                    ck += 1
            """Whichever bird type has the most votes is the predicted unknown bird"""
            #print("a: " + str(ak) + " p: " + str(pk) + " c: " + str(ck)) #This shows the number of votes for each bird
            if (ak > pk and ak > ck):
                print("Accipitridae")
            elif (pk > ak and pk > ck):
                print ("Passeridae")
            elif (ck > ak and ck > pk):
                print("Cathartidae")
            
                
            abirdDistanceList = []
            cbirdDistanceList = []
            pbirdDistanceList = []
            unknownbirdList = [] 

        abirdLengthList = []
        abirdWidthList = []
        abirdSpanList = []
        abirdAngleList = []
        pbirdLengthList = []
        pbirdWidthList = []
        pbirdSpanList = []
        pbirdAngleList = []
        cbirdLengthList = []
        cbirdWidthList = []
        cbirdSpanList = []
        cbirdAngleList = []
        
            
        

        
        abirdMasterList = []
        pbirdMasterList= []
        cbirdMasterList = []

