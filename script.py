

def readFile(filename):
    infile = open(filename, 'r')
    flashcards = []
    for line in infile:
        line = line.strip()
        line = line.lower()
        lineLst = line.split(";")
        lineLst[1] = lineLst[1].replace(",", "")
        lineLst[1] = lineLst[1].replace("""", "")
        flashcard_top = lineLst[0]
        flashcard_bottom = lineLst[1]
        flashcards.append([flashcard_top, flashcard_bottom])
    infile.close()
    return flashcards


def main():

    flashcards = readFile("flashcardfile.txt")

    outfile = open("flashcards_answers.csv", 'w')
    for card in flashcards:
        line = card[1] + "," + "\n"
        outfile.write(line)
    outfile.close()

main()
