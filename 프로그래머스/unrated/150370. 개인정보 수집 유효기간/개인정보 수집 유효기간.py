'''
enumerate
일단 날짜 나오면 day로 통일하기
딕셔너리 dict()'''

def convert_time(date):
    year,month,day = map(int,date.split('.'))
    return year*12*28 + month*28 +day

def solution(today, terms, privacies):
    answer = []
    # 오늘 날짜 변환하기
    today = convert_time(today)
    
    # 약관 day로 바꾸기
    term_dict = dict()
    for term in terms:
        term_name, term_month = term.split()
        term_dict[term_name] = int(term_month)*28
   
    # privacies 유효기간 구하기
    for idx,privacy in enumerate(privacies):
        start, term_num = privacy.split()
        end = convert_time(start) + term_dict[term_num]
       
        if end<=today:
            answer.append(idx+1)
        
    return answer