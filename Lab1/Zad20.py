# tworzenie listy
parzyste = [0, 2, 4, 6, 8 ,10]
print(parzyste)
parzyste.append(12)
print(parzyste)

# pojedyncze elementy
print(parzyste[0])
print(parzyste[3])
print(parzyste[-2])

# pojedyncze dlugosci
print(len(parzyste))
# wyswietlanie wykrojonych fragmentow (slices)
print(parzyste[:])
print(parzyste[3:])
print(parzyste[3:6])
print(parzyste[-3:])
print(parzyste[:-3])
fragm = parzyste[1:-1]
print(fragm)
