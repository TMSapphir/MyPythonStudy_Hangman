import random as rd
import def_keymaster as ky


def data_sanitizer(func):

    #verify that func is str
    if type(func)==list:
        func="".join(func)
    
    #cryptation function
    def xor_cipher(txt,key):
        
        testo=list(txt)
        len_chiave=len(key)
        risultato=[]
        
        for i in range(len(txt)):
            #rotation of the key array
            chiave=key[i % len_chiave]
            
            
            #XOR cicle
            criz=testo[i]
            criz=ord(criz)
            criz=criz ^ ord(chiave)
            
            #add the value to risultato
            risultato.append(chr(criz))
            
        #convert risultato in str
        return "".join(risultato)
        
    return xor_cipher

@data_sanitizer
def stringario(func,key):
    return str(stringa)
    




def parola():
    a=["cane","gatto","volpe","lucertola","tigre","giaguaro","coccodrillo","ilvicinodicasachesiguardasanremo","filosofo","tartaruga","cicerone","ilpartigianoregiano","mianonnaincariola","lalattugassassina"]
    chiave=ky.keymaster()
    rand = rd.randint(0 , len(a)-1)
    func=a[rand].lower()
    x1=list(func)
    func="".join(func)
    x2=stringario(func,chiave)

    x2=list(x2)
    x=[x1,x2]
    return x


