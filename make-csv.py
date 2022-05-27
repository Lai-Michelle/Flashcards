
def main():

    infile = open("flashcardfile.txt", 'r')
    csv_file_contents = ""
    for line in infile:
        line = line.strip()
        lineLst = line.split(";")
        answer = lineLst[1].strip()
        csv_file_contents += answer + ","
    infile.close()
    csv_file_contents += "\n"

    outfile = open("flashcard_answers.csv", 'w')
    outfile.write(csv_file_contents)
    outfile.close()

main()
