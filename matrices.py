import numpy as np

import sys
import argparse


def vectorMatrixMult(M, v):
    Mv=np.zeros(M.shape[0],)
    for i in range(M.shape[0]):
        for k in range(v.shape[0]):
            Mv[i]+=(M[i,k]*v[k])

    return Mv

def vectorAddition(v1,v2):
    numRows=v1.shape[0]
    v3=np.zeros(numRows,)

    for i in range(numRows):
        v3[i]=v1[i]+v2[i]

    return v3

def main(argv):
        parser = argparse.ArgumentParser()
        parser.add_argument("--X0", help="vector X[0]",
                            default=np.array([1,2]))
        parser.add_argument("--W1", help="vector W[1]",
                            default=np.array([0.25,-0.02]))
        parser.add_argument("--V1", help="vector V[1]",
                            default=np.array([-0.02,0.37]))
        parser.add_argument("--A",
                            help="matrix A",
                            default=np.array([[0.9,0.1],[-0.1,0.05]]))
        parser.add_argument("--C",
                            help="matrix C",
                            default=np.array([[5,0.9],[1.2,6.9]]))



        args = parser.parse_args()
        X0=args.X0
        W1=args.W1
        V1=args.V1
        C=args.C
        A=args.A

        #Solution using numpy functions
        #X1=np.add(np.dot(A,X0), W1)
        #print("X1= "+str(X1))
        #Y1=np.add(np.dot(C,X1), V1)
        #print("Y1= "+str(Y1))

        AX0=vectorMatrixMult(A, X0)

        X1=vectorAddition(AX0,W1)

        print("X1="+str(X1))

        CX1=vectorMatrixMult(C, X1)

        Y1=vectorAddition(CX1,V1)
        print("Y1="+str(Y1))





if __name__=="__main__":
    main(sys.argv)
