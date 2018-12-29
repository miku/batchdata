from operator import add
import dask

dsk = dict(a=1, b=2, c=(add, 'a', 'b'), d=(sum, ['a', 'b', 'c']))

if __name__ == '__main__':
    result = dask.get(dsk, 'c')
    print(result)
