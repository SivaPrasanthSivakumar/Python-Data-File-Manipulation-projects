def getLetterGrade(finalGrade):
    if(finalGrade >= 90):
        return "A"
    elif(90 > finalGrade >= 80):
        return "B"
    elif(80> finalGrade >= 70):
        return "C"
    elif(70> finalGrade >= 60):
        return "D"
    elif(60> finalGrade):
        return "F"

def writeStudentData(outfile,line):
    outfile.write("%s\t%s\t%d\t%d\t%d\t%d\t\t%d\t\t%s\n"%(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]))


def calculateAndWriteGrades():
    inputFileName = "input.txt"
    outputFileName = "output.txt"

    infile = open(inputFileName, "r")
    outfile = open(outputFileName, "w+")
    outfile.write("Name.\t\tID.\t(Test1)\t(Test2)\t(HW)\t(Project)\tTotalScore\tGrade\n")
    
    line = infile.readline()
    while line != "":
        line=line.split(":")
        if(len(line)==6):
            line[0]=line[0].strip(" ")
            line[1]=line[1].strip(" ")
            for i in range(2,6):
                line[i]=float(line[i].strip(" \n"))
            finalGrade=0.2*(line[2]+line[3]+line[5])+0.4*line[4]
            line.append(finalGrade)
            line.append(getLetterGrade(finalGrade))
            writeStudentData(outfile,line)
        print(line)
        line = infile.readline()
    infile.close()
    outfile.close()
calculateAndWriteGrades()