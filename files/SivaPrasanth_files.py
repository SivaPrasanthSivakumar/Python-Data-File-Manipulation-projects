from csv import reader, writer

# Open the two csv files with explicit encoding.
infile = open("movies.csv", encoding='utf-8')
csvReader = reader(infile)

outfile = open("class_demo.csv", "w", newline="", encoding='utf-8')
csvWriter = writer(outfile)

# Add the list of the column headers to the csv file.
headers = ["Name", "Year", "Producer"]
csvWriter.writerow(headers)

# Skip the row of column headers in the reader
next(csvReader)

# Filter the rows of data.
for row in csvReader:
    year = int(row[1])
    if 1998 <= year <= 1999:
        newRow = [row[0], row[1], row[2]] 
        csvWriter.writerow(newRow)

infile.close()
outfile.close()
