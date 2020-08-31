n = int(input())
a = [int(i) for i in input().split()]
d = dict()
cache = dict()
for i in a:
    d[i] = d[i] + 1 if i in d else 1


def get_value(i):
    if i in d:
        return i * d[i]
    else:
        return 0


def valid_configuration(dictionary):
    keys = list(dictionary.keys())
    for k in keys:
        if (k - 1 in dictionary) or (k + 1 in dictionary):
            return False
    return True


def sum_values(dictionary):
    keys = list(dictionary.keys())
    sum = 0
    for k in keys:
        sum += dictionary[k]
    return sum


def get_max(dictionary):
    if len(dictionary) == 0:
        return 0
    keys = list(dictionary.keys())
    dictionary_id = '-'.join([str(k) for k in keys])
    i = keys[0]
    element_i = get_value(i)
    if len(dictionary) == 1:
        return element_i
    elif dictionary_id in cache:
        return cache[dictionary_id]
    elif valid_configuration(dictionary):
        cache[dictionary_id] = sum_values(dictionary)
        print(cache[dictionary_id])
        return cache[dictionary_id]
    else:
        element_i_r = get_value(i + 1)
        element_i_l = get_value(i - 1)
        dict_copy1 = dict(dictionary)
        elements = []
        if element_i > 0:
            dict_copy1.pop(i - 1, None)
            dict_copy1.pop(i + 1, None)
            dict_copy1.pop(i, None)
            elements.append(get_max(dict_copy1))

        if element_i_l > 0:
            dict_copy2 = dict(dictionary)
            dict_copy2.pop(i - 2, None)
            dict_copy2.pop(i, None)
            dict_copy2.pop(i - 1, None)
            elements.append(element_i_l + get_max(dict_copy2))

        if element_i_r > 0:
            dict_copy3 = dict(dictionary)
            dict_copy3.pop(i, None)
            dict_copy3.pop(i + 2, None)
            dict_copy3.pop(i + 1, None)
            elements.append(element_i_r + get_max(dict_copy3))

        if element_i_l == 0 and element_i_r == 0:
            dict_copy2 = dict(dictionary)
            dict_copy2.pop(i - 1, None)
            dict_copy2.pop(i + 1, None)
            dict_copy2.pop(i, None)
            elements.append(element_i + get_max(dict_copy2))

        return max(elements)


print(d)
print(get_max(d))

