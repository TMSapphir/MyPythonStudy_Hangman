import codice_parola as cp
import impiccato_codice as imp




word_list=cp.parola()
hanged=imp.impiccagione()


word,bar = word_list

bar1 = list(bar)
l=0
k=0
while k < len(hanged):
    print(hanged[k])

    if k >= len(hanged)-1:
        determination = -1 
        break

    print("la parola che devi indovinare: "+"     "+" ".join(bar))
    print("\n")

    x=input(f"inserisci la lettera: ",)
    for l in range(len(word)):
        if x.lower() == word[l]:
            bar[l]=x.lower()
    
    if x not in word:
        k=k+1
    
    if bar == word:

        print("\n\n")

        bar = list(bar1)
        print("HAI VINTO!!! " + f" LA PAROLA ERA: {' '.join(word).upper() }")
        break


    
