#!/home/fish/anaconda3/bin/python
import numpy as np
import sys
from six.moves import cPickle as pickle

def encode(c):
    """
    Encoding, ACGT => 1234
    """ 
    if c in ['A', 'a']:
        return 0
    elif c in ['C', 'c']:
        return 1
    elif c in ['G', 'g']:
        return 2
    elif c in ['T', 't']:
        return 3
    else:
        sys.exit()

def encodingSeq2PWM(train_data, f):
    train_file = train_data
    if isinstance(train_file, str):
        train_file_f = open(train_file, 'r')

    name  = list()
    #data structure (sample_size, 101*2f, 4)
    data  = np.zeros((1, 101 + 2*f ,4), dtype=np.float32)
    #label structure (sample_size, 2)
    label = np.zeros((1, 2), dtype=np.float32) 
    #build flanking block
    flanking = np.array([0.25 for i in range(f*4)]).reshape(f, 4)
    for line in train_file_f:
        n, seq, l = line.split()
        #store name
        name.append(n)

        #store data
        idx = np.asarray(list(map(encode, seq)))
        c = (np.arange(4) == idx[:, np.newaxis]).astype(np.float32) 
        e = np.insert(c ,0, flanking, axis=0)
        e = np.insert(e ,e.shape[0] , flanking, axis=0)
        e = e[np.newaxis, :]
        data = np.concatenate((data, e))

        #store label
        a = np.array([int(l)])
        d = (np.arange(2) == a[:, np.newaxis]).astype(np.float32)
        label = np.concatenate((label, d))

    #delete first sample. (fake one)
    data = np.delete(data, 0, 0)

    #save as a pickle file
    pack = {'name':n, 'seq':data, 'label':label}
    fh = open('test.pickle', 'wb')
    pickle.dump(pack,fh)
    fh.close()

    #read from pickle file
    fh = open('test.pickle', 'rb')
    save = pickle.load(fh)
    n     = save['name']
    seq   = save['seq']
    label = save['label']

    train_file_f.close()

if  __name__ == '__main__':

    import sys
    import argparse

    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description="")
    parser.add_argument('train_data', type=str, help='')
    parser.add_argument('flanking_len', type=int, help='')

    args = parser.parse_args()

    print(args.train_data)
    encodingSeq2PWM(args.train_data, args.flanking_len)
