def filter_list(lst):

    return [x for x in lst if x < 30 and x % 3 == 0]

    lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
    result = filter_list(lst)
    print(result)  # Вывод: [15, 3, 21, 9]
