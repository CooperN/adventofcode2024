rawdata = open("inputs/day1.txt").read()
data = str(rawdata).split('\n')

lista = []
listb = []

listdata = [a.split() for a in data]

lista, listb = zip(*listdata)

sorteda = []
sortedb = []

sorteda = sorted(lista)
sortedb = sorted(listb)

distancelist = []
distancetotal = 0

for a,b in zip(sorteda,sortedb):
    distance = abs(int(a)-int(b))
    distancelist.append(distance)
    distancetotal = distancetotal + distance

print(f'Answer 1: Distance is {distancetotal}')


uniquelocations = set(sorteda)

score = 0

for location in sorteda:
    b = sortedb.count(location)
    score = score + (int(b)*int(location))

print(f'Answer 2: Sorted score is {score}')
