import string

user_data = ""; # строка, вводимая с клавиатуры
user_numb = int(0); # величина сдвига
rus_arr = []; # массив русских строчных букв
rus_arr_h = []; # массив русских заглавных букв
eng_arr = []; # массив английских строчных букв
eng_arr_h = []; # массив английских заглавных букв
a = ord('а');
nw_ind = int(0);

#функция сдвига
def shift(i, count, arr, user_numb, user_data):
    for j in range(0, count):
        if (user_data[i] == arr[j]):
            nw_ind = j + user_numb;
            if (nw_ind > count - 1):
                nw_ind -= count;
                user_data = user_data[:i] + arr[nw_ind] + user_data[i+1:];
                break;
            else:
                user_data = user_data[:i] + arr[nw_ind] + user_data[i+1:];
            break;
    return user_data

#заполнение массивов
for i in (string.ascii_lowercase):
    eng_arr.append(i);

for i in (string.ascii_uppercase):
    eng_arr_h.append(i);

for i in ([chr(i) for i in range(a,a+6)] + [chr(a+33)] + [chr(i) for i in range(a+6,a+32)]):
    rus_arr.append(i);

for i in ([chr(i) for i in range(a,a+6)] + [chr(a+33)] + [chr(i) for i in range(a+6,a+32)]):
    rus_arr_h.append(i.upper());

print("Введите сообщение: ", end = "");
user_data = input();
print("Введите размер смещения: ", end = "");
user_numb = int(input());

for i in range(0, len(user_data)):
    count = 33
    user_data = shift(i, count, rus_arr, user_numb, user_data)
    user_data = shift(i, count, rus_arr_h, user_numb, user_data)
    count = 26
    user_data = shift(i, count, eng_arr, user_numb, user_data)
    user_data = shift(i, count, eng_arr_h, user_numb, user_data)
print("\nРезультат: ", end = "");
print(user_data);
