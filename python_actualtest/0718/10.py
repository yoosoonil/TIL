# 문제 코드
number_list = [1, 23, 9, 6, 91, 59, 29]
max = max(number_list)

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max2 = max(number_list2)

if max > max2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max < max2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")

# 발생오류 : TypeError: 'int' object is not callable
# 발생원인 : 내장함수 max()를 변수명의 식별자로 사용하게 되어 내장함수가 변수로 덮어짐.
#            내장함수 max()가 아닌 변수 max가 되어 호출 불가능.
# 해결방법 : max라는 것을 변수로 바꾸어 max() 함수가 작동하게끔 변경.

# 수정 코드
number_list = [1, 23, 9, 6, 91, 59, 29]
max2 = max(number_list)                             # max = max(number_list) -> max2 = max(number_list)

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max3 = max(number_list2)



if max2 > max3:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max2 < max3:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")