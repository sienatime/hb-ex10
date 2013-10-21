def main():
    f = open("prepositions.txt")
    lines = f.readlines()
    f.close()

    ignore = []

    for line in lines:
        if len(line.strip("\n")) <= 4:
            ignore.append(line.strip("\n"))

    print ignore

main()