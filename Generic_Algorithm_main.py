import random as rn
import scipy as sp
# https://wikidocs.net/book/1553

# 초기값 설정
def init(x1, x2):
    x = []
    for i in range(4):
        limmax = rn.randint(x1, x2)
        x.append(limmax)
    return x
    #
    # for xlist in range(4):
    #     print("intial solution value: ", x[xlist])

def sik(x):
    return -x * x + 38 * x + 80


# selection(선택 연산)
def selection(arr):
    print("arr is : ",arr)
    fit = []
    ratio = []
    for i in range(4):
        fit.append(sik(arr[i]))
    print("fit: ", fit)

    # 비율
    for i in range(4):
        if(i == 0):
            ratio.append(arr[i]/sum(fit))
        else:
            ratio.append(ratio[i-1] + fit[i] / sum(fit))
    print("ratio: ",ratio, "fit: ",fit, "ratio sum:",sum(ratio))
# TODO: selection 함수 비율 다시 출력시키기

# main
start = 1
end = 31

# test

# 초기값 출력
initval = init(start,end)
print("initial solution value: ",initval)
selection(initval)
