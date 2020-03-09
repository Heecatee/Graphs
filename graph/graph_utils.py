def has_digits(graph):
    for row in graph:
        if not any(i.isdigit() for i in row):
            return False
    return True


def print_2d_array(title, arr):
    print(title + ":")
    for row in arr:
        for col in row:
            print(col, end=" ")
        print("")
    print("")


def list_to_int_array(arr):
    new_arr = []
    index = 0
    for row in arr:
        new_arr.append([])
        for col in row:
            if type(col) == str:
                new_arr[index].append(int(col.split('(')[0].split(':')[0]))
            else:
                new_arr[index].append(int(col))
        index += 1
    return new_arr
