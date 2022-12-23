def Main():

    with open("packing.txt", "r") as f:
        bags = [
            [bag[: len(bag) // 2], bag[len(bag) // 2 :]] for bag in f.readlines()
        ]

    print(bags)

    for bag in bags:
        


Main()
