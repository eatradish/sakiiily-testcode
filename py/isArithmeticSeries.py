def isArithmeticSeries(l: list) -> bool:
    a_1 = l[0]
    a_n = l[-1]
    n = len(l)
    sn = (a_1 + a_n) * n / 2
    if sum(l) == sn:
        return True
    else:
        return False

def my_sort(l: list) -> list:
    for i in range(len(l)):
      for j in range(len(l)):
        if l[i] > l[j]:
            [i],l[j] = l[j],l[i]
    return l
    # <- o(n^2)

def my_sort_2(l: list) -> list:
    # <- try o(nlogn)

if __name__ == '__main__':
    print(isArithmeticSeries(my_sort([5,3,2,1,7,6,4,8,10,9])))
    print(isArithmeticSeries(my_sort([4,6,3,2,7])))
