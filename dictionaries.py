spacecraft = {"name": "James Webb", "distance": 134, "orbit": "Sun"}

def main():
    print("The name of the spacecraft is ", spacecraft["name"])
    print("The distance is: ", spacecraft["distance"])

    #This method gets the Value of the specified key if present, otherwise returns default value
    #in the second param
    print(spacecraft.get("distance", -1))
    print(spacecraft.get("abc", "Unknown"))


def iteration():
    distances = {"James": 123, "Tom": 344, "Son": 254}

    for name in distances.keys():
        print("The name is",name + " and the distance is:",distances[name])

main()
iteration()

