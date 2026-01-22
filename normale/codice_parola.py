import random as rd




def parola():
    a=["cane","gatto","volpe","lucertola","tigre","giaguaro","coccodrillo","ilvicinodicasachesiguardasanremo","filosofo","tartaruga","cicerone","ilpartigianoregiano","mianonnaincariola","lalattugassassina"]
    rand = rd.randint(0 , len(a)-1)
    word=a[rand].lower()
    x1=list(word)
    x2=[]

    for i in range(len(x1)):
        x2.append("_")
    x=[x1,x2]
    return x


