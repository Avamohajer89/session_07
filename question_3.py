#تمرین سوم 
def analyze_transactions():
    transactions = [("Ali", "deposit", 5000000),("Ali", "withdraw", 1000000),\
                        ("Sara", "deposit", 8000000),("Ali", "withdraw", 500000),\
                            ("Sara", "withdraw", 2000000),("Reza", "deposit", 10000000)]
    names = set([i[0] for i in transactions  ])
    result={}
    
    for name in names:
        total=0
        for i in transactions:
            if i[0]==name and i[1]=="deposit":
                total+=i[2]
            
        total1=0
        for j in transactions:
            if j[0]==name and j[1]=="withdraw":
                total1+=j[2]
                
        totalb=0
        for i in transactions:
            if i[0]==name and i[1]== "deposit":
                totalb+=i[2]
            elif i[0]==name and i[1]== "withdraw":
                totalb-=i[2]
                
        totalt=0
        for i in transactions:
            if i[0]== name :
                
                totalt+=1
        result[name]={"deposit":total,"withdraw":total1,\
                      "Balance change":totalb,"Number of transactions":totalt}
        
    result=dict(sorted(result.items()))
    print(result,"\n")
    
    max_deposit =set([ i["deposit"] for i in result.values()])
    final=max(max_deposit)
    print(f'Maximum deposit: {name,final}')
    
    max_withdraw =set([ i["withdraw"] for i in result.values()])
    final1=max(max_withdraw)
    for name, data in result.items():
     if data["withdraw"] == final1:
        print(f'Maximum withdraw: {name, final1}')
        
    max_transactions=[i["Number of transactions"] for i in result.values()]
    max_t = max(set(max_transactions))
    for name, data in result.items():
        if data["Number of transactions"]==max_t:
         print(f'Max transactions: {name, max_t}')
          
analyze_transactions()
