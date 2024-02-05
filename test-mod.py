import numpy as np

print('loaded module')

def query(name, version, lb, ub):
    print('foo')
    return(np.ones((2,2)))

if __name__  == "__main__":
    res = query('abc', 2, (1,2),(3,4))
    print(res)
