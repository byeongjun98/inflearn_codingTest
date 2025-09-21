def find_max_plus_or_multiply(array):
    sum = 0
    for number in array:
        if number <= 1 or sum <= 1:
            sum += number
        elif number >= 2 or sum >= 2:
            sum *= number
    return sum

result = find_max_plus_or_multiply

print("정답 = 728 / 현재 풀이값 =", result([0,3,5,6,1,2,4]))