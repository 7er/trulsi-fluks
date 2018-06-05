def sort(input_list):
    max_value = 1000
    min_value = 0
    search_index = [0 for each in range(max_value)]
    for each in input_list:
        if each < min_value or each >= max_value:
            raise RuntimeError('angst ugyldig verdi {}'.format(each))
        search_index[each] += 1
    result = []
    for index, count in enumerate(search_index):
        for each in range(count):
            result.append(index)
    return result
