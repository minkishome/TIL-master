blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
# dict_blood = dict()  # 빈 dict 선언
# for i in blood_types:
#     if i not in dict_blood:
#         dict_blood[i] = blood_types.count(i)
# print(dict_blood)


unique_blood_type = list(blood_types)

print(unique_blood_type)

count_dict = {}

for u in unique_blood_type:
    count_dict[u] = 0            # count_dict[]라는 dict에 키 값을 입력한다
    
print(count_dict)

for b in blood_types:
    count_dict[b] += 1          # 이 과정을 통해 value 값을 더한다. 

print(count_dict)