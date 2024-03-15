def convert_gallons_to_cups(gallons):
    def gallons_to_quarts(gallons):
        print(f"Converting {gallons} gallons to quarts!")
        return gallons * 4

    def quarts_to_pints(quarts):
        print(f"Converting {quarts} quarts to pints")
        return quarts * 2

    def pints_to_cups(pints):
        print(f"Converting {pints} pints to cups")
        return pints * 2

    quarts = gallons_to_quarts(gallons)
    pints = quarts_to_pints(quarts)
    cups = pints_to_cups(pints)
    return cups

print(convert_gallons_to_cups(1))
print(convert_gallons_to_cups(3))


