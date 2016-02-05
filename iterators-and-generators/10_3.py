import os


def all_lines(path):
    for filename in os.listdir(path):
        full_filename = os.path.join(path, filename)
        print "[{}]".format(full_filename)
        try:
            for line in open(full_filename):
                yield line
