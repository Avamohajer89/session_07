#تمرین چهار 
transactions = [
    ("Ali", "deposit", 5000000),
    ("Ali", "withdraw", 1000000),
    ("Sara", "deposit", 8000000),
    ("Ali", "withdraw", 500000),
    ("Sara", "withdraw", 2000000),
    ("Reza", "deposit", 10000000)
]
def analyz_transaitions(transactions):
    dic1={}
    max_deposit=0
    most_withdrawals=0
    most_active=0
    mos_active_user=''
    for i in transactions:
         
         name=i[0]
         Type=i[1]
         amount=i[2]
         
         if name not in dic1:
             dic1[name]={'deposit':0,
                         'withdraw':0,
                         'balanc_change':0,
                         'transactions':0}
         dic1[name]['transactions']+=1
         
         if Type=='deposit':
             dic1[name]['deposit']+=amount
             dic1[name]['balanc_change']+=amount
         if Type=='withdraw':
            
             dic1[name]['withdraw']+=amount
             dic1[name]['balanc_change']-=amount
             
    for name in dic1:
        if dic1[name]['deposit']>max_deposit:
            max_deposit=dic1[name]['deposit']
        if dic1[name]['withdraw']>most_withdrawals:
            most_withdrawals=dic1[name]['withdraw']   
         
        if dic1[name]['transactions']>most_active:
            most_active=dic1[name]['transactions']  
            mos_active_user=name
        
    return dic1,max_deposit,most_withdrawals,mos_active_user 
   
result,max_deposit,most_withdrawals,mos_active_user=analyz_transaitions(transactions) 
for name,info in result.items():
    print(name,':',info)            
print('max_deposit:',max_deposit)  
print('most_withdrawals:',most_withdrawals) 
print('mos_active_user:',mos_active_user)
