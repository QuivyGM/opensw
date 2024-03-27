#사용 배열
scnum=[]
name=[]
eng=[]
clan=[]
pyt=[]
sum=[0, 0, 0, 0, 0]
avg=[0, 0, 0, 0, 0]

#입력 함수
def info():
    for i in range(5):
        scnum.append(input("\n학번:\t"))
        name.append(input("이름:\t"))
        eng.append(int(input("영어:\t")))
        clan.append(int(input("C-언어:\t")))
        pyt.append(int(input("파이썬:\t")))
        sum[i], avg[i] = score_sum(eng[i], clan[i], pyt[i])
#총점/평균 계산 함수
def score_sum(q, w, e):
    sum=q+w+e
    return sum, sum/3

#학점 계산 함수
def grade(a):
    if(a>90):
        return "A"
    elif (a>80):
        return "B"
    elif (a>70):
        return "C"
    else:
        return "F"
#등수 계산 함수
def rank(a, arr):
    num=1
    for i in range(5):
        if(arr[i]>a):
            num+=1
    return num
#출력 함수
def info_out():
    for i in range(5):
        print (scnum[i], "\t\t", name[i], "\t", eng[i], "\t", clan[i], "\t", pyt[i], "\t", sum[i], "\t", sum[i]/3, "\t", grade(sum[i]/3), "\t", rank(sum[i], sum))

#============================ << main >> ============================

#정보 입력
info()

#정보 출력
print("\n=============================================================================")
print(" 학번\t\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
print("=============================================================================\n")

info_out()
print("")