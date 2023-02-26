sel = []
def buy(user,sel,emoticons):
    plus=False
    spend=0
    rate = user[0]#구매 의향이 있는 할인율
    price = user[1]
    
    total_buy=0
    for idx in range(len(sel)):
        if sel[idx]>=rate:
            total_buy+=emoticons[idx]*(100-sel[idx])//100
    if total_buy>=price:
        plus=True
    else:
        spend=total_buy
    #print("sel",sel,"total buy",total_buy,"plus",plus,"spend",spend)
    return plus,spend

ans = []
def select(users,emoticons):
    #0:10 1:20 2:30 3:40
    if len(sel)==len(emoticons):
        total_plus=0
        total_spend=0
        #print(sel)
        for user in users:
            plus,total_buy=buy(user,sel,emoticons)
            total_spend+=total_buy
            if plus==True:
                total_plus+=1     
        ans.append((total_plus,total_spend))
        
        return
    for i in range(10,41,10):
        sel.append(i)
        select(users,emoticons)
        sel.pop()
def solution(users, emoticons):
    answer = []
    select(users,emoticons) #이모티콘 할인율 조합
    answer=sorted(ans,key=lambda x:(-x[0],-x[1]))[0]
    return answer