input = "abadabac"


def find_not_repeating_first_character(string): # 'string'을 인자로 받아 반복되지 않는 첫 글자를 찾는 함수를 정의합니다.
    occurrence_array = find_alphabet_occurrence_array(string) # 다른 함수 `find_alphabet_occurrence_array`를 호출하여 각 알파벳이 몇 번 나왔는지 세고, 그 결과를 `occurrence_array`에 저장합니다.
    not_repeating_char_array = [] # 한 번만 등장하는 알파벳을 담아둘 `not_repeating_char_array`라는 빈 리스트를 만듭니다.
    for index in range(len(occurrence_array)): # `occurrence_array` (알파벳 개수만큼, 즉 26개)의 길이만큼 반복문을 실행합니다.
        alphabet_occurrence = occurrence_array[index] # 현재 알파벳의 등장 횟수를 `alphabet_occurrence` 변수에 저장합니다.
        if alphabet_occurrence == 1: # 만약 알파벳이 딱 한 번만 등장했다면, 아래 코드를 실행합니다.
            not_repeating_char_array.append(chr(index + ord("a"))) # `index` 값(0~25)을 다시 알파벳으로 변환하여 (예: 0 -> 'a') `not_repeating_char_array` 리스트에 추가합니다.
    for char in string: # 이제 원래 입력받았던 `string`의 문자들을 처음부터 하나씩 다시 확인합니다.
        if char in not_repeating_char_array: # 현재 문자가 "한 번만 등장하는 알파벳 리스트"에 포함되어 있다면,
            return char # 그 문자가 바로 "반복되지 않는 첫 번째 문자"이므로, 그 문자를 반환하고 함수를 종료합니다.
    return "_" # 반복문을 모두 돌았는데도 "한 번만 등장하는 알파벳"을 찾지 못했다면, `_`를 반환합니다.


def find_alphabet_occurrence_array(string): # string을 인자로 받아 각 알파벳의 빈도수를 계산하는 함수를 정의합니다.
    alphabet_occurrence_array = [0] * 26 # 알파벳은 26자이므로, 0으로 채워진 26칸짜리 리스트를 만듭니다. 각 칸은 a부터 z까지의 알파벳 개수를 저장합니다.
    for char in string: # 입력받은 string의 각 문자를 순서대로 순회합니다.
        if not char.isalpha(): # 만약 문자가 알파벳이 아니면,
            continue # 아래 코드를 실행하지 않고 다음 문자로 넘어갑니다.
        arr_index = ord(char) - ord("a") # 문자의 아스키 코드 값에서 'a'의 아스키 코드 값을 빼서 리스트의 인덱스를 계산합니다. (예: 'a' -> 0, 'b' -> 1)
        alphabet_occurrence_array[arr_index] += 1 # 해당 알파벳의 인덱스에 해당하는 값을 1 증가시킵니다.
    return alphabet_occurrence_array # 알파벳 빈도수 계산이 끝난 리스트를 반환합니다.


result = find_not_repeating_first_character
print("정답 = d / 현재 풀이값 =", result("abadabac"))