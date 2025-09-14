def find_max_num(array):
    for number in array:
        is_max_num = True
        for compare_number in array:
            if number < compare_number:
                is_max_num = False
                break
        if is_max_num:
            return number

print("정답 = 5 / 현재 풀이값 = ", find_max_num([3,4,5,1,2,4]))
print("정답 = 6 / 현재 풀이값 = ", find_max_num([6,6,6]))
print("정답 = 1888 / 현재 풀이값 = ", find_max_num([6,9,2,7,1888]))