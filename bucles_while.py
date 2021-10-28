def run():
    num=2
    pot=0
    res=0
    LIMITE=100000


    while(res<LIMITE):
        res=pow(num,pot)
        
        if res<=LIMITE:
            print(str(num) + " a la " + str(pot) +  " es "+ str(res))

        pot+=1

if __name__=="__main__":
    run()