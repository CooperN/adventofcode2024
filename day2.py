
def main():

    rawdata = open("inputs/day2.txt").read()
    data = str(rawdata).split('\n')

    intlist = []
    #increasing or decreasing
    # increase or decrease by at most 3 and at least 1

    for i in data:
        rowlist = []
        for j in i.split():
            rowlist.append(int(j))
        intlist.append(rowlist)

    safe_rows = []

    for row in intlist:
        safe = True
        if row[0]<row[1]:
            increaseing = True
        else:
            increaseing = False
        for i in range(len(row) - 1):
            if increaseing:
                if row[i] > row[i+1]:
                    safe = False
            else:
                if row[i] < row[i+1]:
                    safe = False
            jump = abs(row[i]-row[i+1])
            if jump < 1 or jump > 3:
                safe = False
            if not safe:
                break
            if(i == len(row)-2):
                if safe == True:
                    safe_rows.append(row)

    print(f'Answer 1: {len(safe_rows)} safe rows')

    safe_rows = []

    for row in intlist:
        safe = rowcheck(row)
        if safe:
            safe_rows.append(row)
        else:
            for i in range(len(row)):
                temprow = row[:]
                temprow.pop(i)
                safe = rowcheck(temprow)
                if safe:
                    safe_rows.append(row)
                    break



    print(f'Answer 2: {len(safe_rows)} safe rows')


def rowcheck(row):
        safe = True
        if row[0]<row[1]:
            increaseing = True
        else:
            increaseing = False
        for i in range(len(row) - 1):
            if increaseing:
                if row[i] > row[i+1]:
                    safe = False
            else:
                if row[i] < row[i+1]:
                    safe = False
            jump = abs(row[i]-row[i+1])
            if jump < 1 or jump > 3:
                safe = False
            if not safe:
                return safe
            if(i == len(row)-2):
                if safe == True:
                    return safe


if __name__ == "__main__":
    main()
