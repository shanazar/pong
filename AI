from random import *

def juhuslikmaatriks(maatriksi_laius,maatriksi_kõrgus):
    maatriks=[]
    for i in range(maatriksi_laius):
        maatriks1=[]
        for  j in range(maatriksi_kõrgus):
            maatriks1.append(uniform(-1,1))
        maatriks.append(maatriks1)
    return maatriks

mudel=[juhuslikmaatriks(10,4),juhuslikmaatriks(10,10),juhuslikmaatriks(1,10)]
#print(mudel)

def errorifunktsioon(x):
    t=1/(1+0.5*abs(x))
    g=t*(2.7182**(-x**2-1.26551223+1.00002368*t+0.3740916*t**2+0.09678418*t**3-0.18628806*t**4+0.27886807*t**5-1.13520398*t**6+1.48851587*t**7-0.82215223*t**8+0.17087277*t**9))
    if x>=0:
        return 1-g
    else:
        return g-1

#print(errorifunktsioon(-0.2))
def sigmoid(x):
    return 1/(1+2.7182**(-x))

def normaaljaotus(x):
    return 1/((2*3.14159265359)**0.5)*(2.7182**-((x)**2)/2)

#print(normaaljaotus(0.5))

def maatriksite_korrutamine(maatriks1,maatriks2):
    väljund = []
    for i in range(len(maatriks1)):
        mat1=[]
        for j in range(len(maatriks2[0])):
            mat1.append(0)
        väljund.append(mat1)
    for i in range(len(maatriks1)):
        for j in range(len(maatriks2[0])):
            #print(i,j)
            for k in range(len(maatriks2[0])):
                väljund[i][j]+=maatriks1[i][k]*maatriks2[k][j]
    return väljund

def normaliseerimine(maatriks):
    väljund=[]
    for rida in maatriks:
        vahekas=[]
        for element in rida:
            vahekas.append(errorifunktsioon(element))
        väljund.append(vahekas)
    return väljund

def arvutaviga(pakkumine,tegelik):
    väljund=[]
    for i in range(len(pakkumine)):
        väljund.append(pakkumine[i][0]-tegelik[i])
    return väljund

#print(maatriksite_korrutamine( [[12,7,3],[4 ,5,6],[7 ,8,9]],[[5,8,1,2],[6,7,3,0],[4,5,9,1]]))

def arvasuund(palli_x,palli_y,asukoht,vastase_asukoht,skoor):
    esimenelayer=[[palli_x], [palli_y],[asukoht],[vastase_asukoht],[skoor]]
    #print(mudel[0])
    hiddenlayer1=normaliseerimine(maatriksite_korrutamine(mudel[0],esimenelayer))
    #print(hiddenlayer1)
    hiddenlayer2=normaliseerimine(maatriksite_korrutamine(mudel[1],hiddenlayer1))
    #print(hiddenlayer2)
    väljund=normaliseerimine(maatriksite_korrutamine(mudel[2],hiddenlayer2))
    print(väljund)
    return väljund[0][0]
