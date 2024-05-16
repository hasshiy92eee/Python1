def get_tail(*args):
    return args[-1]

def get_tail2(*args):
    ret = 0
    for n in args:
        ret = n
    return ret

print(get_tail2(3, 5, 9, 20))