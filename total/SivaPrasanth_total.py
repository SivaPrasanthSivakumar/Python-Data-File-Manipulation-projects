inputFileName = input("Input file name: ")
outputFileName = input("Output file name: ")

infile = open(inputFileName, "r")
outfile = open(outputFileName, "w+")

total = 0.0
count = 0

line = infile.readline()
while line != "":
    value = float(line)
    outfile.write("%15.2f\n" % value)
    total = total + value
    count = count + 1
    line = infile.readline()

outfile.write("%12s\n" % "      ------------")
outfile.write("total: %8.2f\n" % total)
avg = total / count
outfile.write("Average: %8.2f\n" % avg)

infile.close()
outfile.close()
