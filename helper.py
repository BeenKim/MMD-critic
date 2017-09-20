# maintained by rajivak@utexas.edu
import numpy as np

def format_numsel(numsel):
    ss = ''
    for i,j in enumerate(numsel):
        ss = ss + " %d:%d " %(i,j)
    return ss

def get_train_testindices(n, ntest, seed):
    np.random.seed(seed)
    testindices = np.random.choice(n,ntest,replace=False)
    trainindices = np.setdiff1d( range(n), testindices)
    return trainindices, testindices

def exit(str):
    print str
    exit(1)


def dir_exists(filename):
    import os
    dir = os.path.dirname(filename)

    try:
        os.stat(dir)
    except:
	try:
        	os.mkdir(dir)
	except:
		# for Mac mkdir this works:
        	os.makedirs(dir)
