def find_negative_pairs(array):
    pairs = []
    for i in range(len(array) - 1):
        if array[i] < 0 and array[i + 1] < 0:
            pairs.append((array[i], array[i + 1]))
    print("Pairs of consecutive negative numbers:", pairs)


def remove_duplicates(array):
    seen = set()
    unique_array = []
    for x in array:
        if x not in seen:
            unique_array.append(x)
