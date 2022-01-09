import itertools 

class primjer:

    def __init__(obj, rel, fo):
        obj.rel=rel
        obj.fo=fo




def primjeri():
    p1=primjer(["A","B","C","D","E","F","G","H","I","J"], 
               ["A->B","BD->F","C->DG","F->CE","G->I"])
    
    p2=primjer(["A","B","C","D","E","F","G","H","I","J"], 
               ["J->GH", "HI->ED", "B->I","E->AC","GC->F"])
    
    p3=primjer(["A","B","C","D","E","F","G","H","I","J"], 
               ["ACD->FJ", "BE->AH","FI->CDG","G->BE","HJ->I"])
    
    p4=primjer(["A","B","C","D","E","F","G","H","I","J"], 
               ["CD->E","G->E","E->HI","J->CG","H->JD"])
    
    p5=primjer(["A","B","C","D","E","F","G","H","I","J"], 
               ["A->EF","F->CH","I->DB","CJ->I","BF->JE","E->CD"])
    
    p6=primjer(["A","B","C","D","E","F","G","H","I","J"], 
               ["DI->B","AJ->F","GB->FJE","AJ->HD","I->CG"])
    
    p7=primjer(["A","B","C","D","E","F","G","H","I","J"], 
               ["A->B","C->DE","H->CI","B->CHF","F->DJ"])
    
    p8=primjer(["A","B","C","D","E","F","G","H","I","J"], 
               ["BC->HI","IF->D","J->A","HA->BEF","G->CJ","DE->G"])
    
    p9=primjer(["A","B","C","D","E","F","G","H","I","J"], 
               ["B->C","E->F","H->I","J->A","D->G"])
    
    p10=primjer(["A","B","C","D","E","F","G","H","I","J"], 
                ["H->F","ED->B","FE->B","FE->GC","H->DI","I->AEG"])
    
    baza=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]
    print_primjeri(baza)
    izbor_primjera(baza)

def izbrisi_primjer(baza):
    n=int(input("Unesite broj primjera koji želite izbrisati:"))
    baza.remove(baza[n-1])
    print_primjeri(baza)

def novi_primjer(baza):
    
    temp_rel=input("Unesite relacijsku shemu:")
    while (temp_rel.isalpha()==False):
         temp_rel=input("Krivi unos, unesite relacijsku shemu:")
    rel=[]
    temp_rel=temp_rel.upper()
    for i in range(0,len(temp_rel),1):
        rel.append(temp_rel[i])
        
    fo=[]
    n=0
    n=input("Unesite broj f. o. u relaciji:")
    while (n.isdigit()==False):
         n=input("Krivi unos, unesite broj f.o. u relaciji:")
    n=int(n)
    for i in range(0,n,1):
        temp_fo=input("Unesite funkcionalnu ovisnost:")
        while (provjera_unosa_fo(rel,temp_fo.upper())==False):
             temp_fo=input("Krivi unos, unesite funkcionalnu ovisnost:")
             
        fo.append(temp_fo.upper())
    
    p=primjer(rel,fo)
    baza.append(p)
    return baza

def provjera_unosa_fo(rel,fo):
    
    if "->" not in fo:
        return False
    
    for element in fo:
        if (element != "-") and (element != ">"):
            if element not in rel:
                return False
    
    y=fo.split("->")
    if y[0].isalpha()==False:
        return False
    if y[1].isalpha()==False:
        return False
    return True
    
    
def print_primjeri(baza):
     c=1
     for i in baza:
         print("primjer",c,":","relacijska shema:",i.rel,"\n            funkcionalne ovisnosti:",i.fo)
         print("\n")
         c+=1


def izbor_primjera(baza):
       
    
        curr=input("Unestite primjer 1-10 za postojeći primjer, slovo p za unos novog primjera, slvo a za prikaz svih primjera, slovo b za brisanje ili x za izlaz: ")
        
        if curr.isdigit()==True:
            curr=int(curr)
            if((curr<=len(baza)) & (curr>0)):
                print ("Odabrali ste primjer",curr)
                key_search(baza[curr-1])
                return izbor_primjera(baza)  
        
        if ((curr== "x") or (curr=="X")):
            return 0
        
        if ((curr== "b") or (curr=="B")):
            izbrisi_primjer(baza)
            return izbor_primjera(baza)
        
        if ((curr== "a") or (curr=="A")):
            print_primjeri(baza)
            return izbor_primjera(baza)
        
        if ((curr== "p") or (curr=="P")):
            novi_p=novi_primjer(baza)
            key_search(baza[len(novi_p)-1])
            return izbor_primjera(baza)
            
        else:
            return izbor_primjera(baza)

def split (fo):
    x=[]
    for i in range (0,len(fo),1):
        y=fo[i].split("->")
        x=x+y
    return x
    
def containeri (p):
    temp_left=[]
    left=[]
    right=[]
    mid=[]
    temp=[]
    f=split(p.fo)
    for i in range (0,len(p.rel),1):
        for j in range (0,len(f),2):
            if p.rel[i]  in f[j]:
                if p.rel[i]  not in temp_left:
                    temp_left.append(p.rel[i])
        for k in range (1,len(f),2):
            if p.rel[i] in f[k]:
                if p.rel[i]  not in right:
                    right.append(p.rel[i])
    for x in temp_left:
        if x in right:
            mid.append(x)
          
    for x in temp_left:
        if x not in mid:
            if x not in left:
                left.append(x)
                
    for x in p.rel:
        if x not in left:
            if x not in right:
                temp.append(x)
    
    return left,mid,temp

def ograda (atribut,fo,rel):
    f=split(fo)
    og=atribut
    ograda=[]
    bContinue = True
    
    while (bContinue):
        temp_ograda=""
        temp_ograda=temp_ograda.join(ograda)
        for i in range (0,len(f),2):
            br=0
            for j in range (0,len(f[i]),1):
                if f[i][j] in og:
                    br=br+1
                    if br == len(f[i]):
                        og=og+f[i+1]    
        
        for x in og:
            if x not in ograda:
                ograda.append(x)
        ograda.sort()
        
        og=""
        og=og.join(ograda)

        
        if (ograda==rel):
            break
        
        if(len(ograda) > (len(temp_ograda))):
            bContinue=True
        else:
            bContinue=False
            
            
    return ograda


def key_search (p):
    l_cont,mid_cont,temp_cont=containeri(p)
    
    relacija=[]
    for element in p.rel:
        if element not in temp_cont:
            relacija.append(element)
    relacija.sort()
    
    
    keys=[]
    for k in range(0,len(mid_cont)+1,1):
        temp = list(itertools.combinations(mid_cont, k))
        unq = list(set(temp))
      
        if (len(l_cont)==0):
            for i in range (0,len(unq),1):
                temp_str = "".join(unq[i])
                if (ograda(temp_str,p.fo,relacija))==relacija:
                    temp_str += "".join(temp_cont)
                    keys.append(temp_str)
                
        if (len(l_cont)>0):
            for i in range (0,len(unq),1):
                temp_str = "".join(l_cont) + "".join(unq[i])
                if ograda(temp_str,p.fo,relacija)==relacija:
                    temp_str += "".join(temp_cont)
                    keys.append(temp_str)
    
        if(len(keys)>0):
            break
    
    print("RELACIJA: ",p.rel)
    print("OVISNOSTI: ",p.fo)
    print("KLJUCEVI:   ",keys)
    print()
    print("Atributi s lijeva f.o.-",l_cont,"\nAtributi s obje strane f.o.-",mid_cont,"\nAtributi koji nisu unutar f.o.-",temp_cont)
    
    
primjeri()






