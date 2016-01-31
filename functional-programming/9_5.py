d = {'a': 1, 'b': 2, 'c': 3}

def transform_values(func, dict):
    for key in dict:
        dict[key] = func(dict[key])
    return dict


print transform_values(lambda x: x*x, d)