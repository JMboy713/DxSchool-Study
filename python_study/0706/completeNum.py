num = int(input())


def cnt_perfectNumber(num):
    complete_number = []
    for i in range(2, num+1):
        divisor = [1]
        for j in range(2, (i//2)+1):
            if i % j == 0:
                divisor.append(j)
        if i == sum(divisor):
            complete_number.append(i)

    return (len(complete_number))


print(cnt_perfectNumber(num))