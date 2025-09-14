# 2. [0 * 26] 각 알파벳의 빈도수를 저장한 배열을 만든다 
#  그리고 문자열을 돌면서 해당 문자가 알파벳이라면, 알파벳을 인덱스화 시켜서 알파벳의 빈도수를 업데이트 한다.
# a -> 0번째 인덱스의 값을 올리고, z가 나왔다면 가장 마지막인 25번째 인덱스의 값을 추가

def find_max_occurred_alphabet_array(string):
    alphabet_occurrence_array = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1
    print("alphbet_occurence_array is ", alphabet_occurrence_array)

    max_occurence = 0
    max_alphabet_index = 0
    
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence > max_occurence:
            max_occurence = alphabet_occurrence
            max_alphabet_index = index
    return chr(max_alphabet_index + ord("a"))


result = find_max_occurred_alphabet_array
print("정답 = e / 현재 풀이값 =", result("hello my name is byeongjun"))
print("정답 = l / 현재 풀이값 =", result("hello world"))
print("정답 = s / 현재 풀이값 =", result("best of best skill"))