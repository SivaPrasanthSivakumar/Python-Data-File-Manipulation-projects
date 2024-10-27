inputFileName = input("Input file name: ")
outputFileName = input("Output file name: ")

infile = open(inputFileName, "r")
outfile = open(outputFileName, "w+")

total = 0.0
for line in infile:
    if ":" in line:
        parts = line.split(":")
        item = parts[0]
        price = float(parts[1])
        total = total + price
        
        outfile.write("%-20s%10.2f\n" % (item, price))

outfile.write("%-20s%10.2f\n" % ("Total:", total))

infile.close()
outfile.close()
