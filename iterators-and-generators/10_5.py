def my_chain(*args):
    for arg in args:
        for item in arg:
            yield item
