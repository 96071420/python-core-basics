import sys

def read_series(filename):
    f =open (filename, mode='rt', encoding='utf-8')
    series = []
    for line in f:
        a = int(line.strip())
        series.append(a)
    f.close()
    return series


def main(filename):
    series = read_series(filename)
    print(series)