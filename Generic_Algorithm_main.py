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
    print("arr is : ", arr)
    fit = []
    ratio = []
    for i in range(4):
        fit.append(sik(arr[i]))
    print("fit: ", fit)

    # 비율
    for i in range(4):
        if (i == 0):
            ratio.append(fit[i] / sum(fit))
        else:
            ratio.append(ratio[i - 1] + fit[i] / sum(fit))
    print("ratio: ", ratio, "ratio sum:", sum(ratio))
    print("fit: ", fit, "fit sum: ", sum(fit))

    sx = []
    for i in range(4):
        p = rn.random()
        if p < ratio[0]:
            sx.append(arr[0])
        elif p < ratio[1]:
            sx.append(arr[1])
        elif p < ratio[2]:
            sx.append(arr[2])
        else:
            sx.append(arr[3])
    return sx


def int2Bin(str):
    binlist = []
    for i in range(4):
        binlist.append(bin(str[i]))
    return binlist


# TODO: crossover 함수 작성
# TODO: invert 함수 작성
# TODO: mutation 함수 작성

# main
start = 1
end = 31
# test

# 초기값 출력
initval = init(start, end)
print("selection: ", selection(initval))

print("bin list: ", int2Bin(selection(initval)))
