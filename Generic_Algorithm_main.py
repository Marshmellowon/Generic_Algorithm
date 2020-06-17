import random as rn
import pandas as pd
import matplotlib.pyplot as plt


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
    # print("arr is : ", arr)
    fit = []
    ratio = []
    for i in range(4):
        fit.append(sik(arr[i]))

    # 비율
    for i in range(4):
        if (i == 0):
            ratio.append(fit[i] / sum(fit))
        else:
            ratio.append(ratio[i - 1] + fit[i] / sum(fit))
    # print("ratio: ", ratio, "ratio sum:", sum(ratio))
    # print("fit: ", fit, "fit sum: ", sum(fit))

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
        binsrting = '{0:>8}'.format(bin(str[i])).replace("b", "0").replace(" ", "0")
        binlist.append(binsrting)
    return binlist


def crossover(arr):
    strarr = []
    for i in range(2):
        bita = str(arr[i])
        bitb = str(arr[i + 1])

        strarr.append(bita[:4] + bitb[4:])
        strarr.append(bitb[:4] + bita[4:])

    return strarr


def invert(char):
    ran = rn.random()
    a = int(char, 2)
    for i in range(5):
        p = 1 / 32
        if ran < p:
            a << 3
    return a


def mutation(mut):
    mutarr = []
    mutarr2 = []
    output = []
    mutint = list(map(str, mut))
    for i in range(4):
        mutarr.append(invert(mutint[i]))
        mutarr2.append(sik(invert(mutint[i])))
    maxvalue = max(mutarr)
    maxvalue2 = max(mutarr2)
    output.append(maxvalue)
    output.append(maxvalue2)
    return output


# -------------------------------main------------------------------

start = 1
end = 31
x = []
y = []
xinit = []
yinit = []
for i in range(1000):
    # 원래식
    ranvalue = rn.randint(start, end)
    ranvalue2 = sik(ranvalue)

    # 초기값 출력
    initval = init(start, end)

    # selection 출력
    select = selection(initval)

    # binarystr 선언
    binarystr = int2Bin(select)

    # crossover 선언
    cross = crossover(binarystr)

    # mutation 선언
    mutationed = mutation(cross)

    # 산점도 좌표 선언

    print("----------Data start----------")
    print("selection: ", select)
    print("selected value's binary: ", binarystr)
    print("crossover: ", cross)
    print("mutation: ", mutationed)

    x.append(mutationed[0])
    y.append(mutationed[1])
    xinit.append(ranvalue)
    yinit.append(ranvalue2)

initial = pd.DataFrame(
    {"x": xinit, "y": yinit}
)

body = pd.DataFrame(
    {'x': x, 'y': y}
)

plt.scatter(body['x'], body['y'], marker="o")
plt.scatter(initial["x"], initial["y"], marker="x")
plt.xlabel('weight')
plt.ylabel('height')
plt.show()

# TODO: 데이터 찾기
