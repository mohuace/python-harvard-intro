import sys


def main():
    #Tuples store a pair of values which are immutable
    coordinates_tuple = (656.78, 555.343)

    #Cant update elements. Will throw error
    #coordinates_tuple[0] = 677.77

    latitude, longitude = coordinates_tuple
    print("The latitude is",latitude)
    print("The longitude is",longitude)

    coordinates_list = [656.78, 555.343]

    #We can use tuples when know the values are constant and won't change
    #It is more efficient memory wise. Eg:

    print(f"The list takes {sys.getsizeof(coordinates_list)} bytes")
    print(f"The tuple takes {sys.getsizeof(coordinates_tuple)} bytes")

main()