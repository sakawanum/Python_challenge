#P116

#1
list1 = ["ウォーキング・デッド",
         "アントラージュ",
         "ザ・ソプラノズ",
         "ヴァンパイア・ダイアリーズ"]
for lis in list1:
    print(lis)


#2
for i in range(25, 51):
    print(i)



#3
for index, list_1 in enumerate(list1):
    print(index)
    print(list_1)


#4
"""qs = ["1", "3", "8"]
while True:
    a = input("入力してください。:")
    if "q" == a:
        break
    if a not in qs:
        print("数字を入力するか、qで終了します。")
    if a in qs:
            print("正解")
    else:
            print("不正解")
"""
#4_解答

qs = [1, 3, 8]

while True:
    a = input("入力してください。:")
    if a == "q":
        break
    try:
        a = int(a)
    except ValueError:
        print("数字を入力するか、qで終了します。")
    if a in qs:
        print("正解")
    else:
        print("不正解") 


numbers = [11, 32, 33, 15, 1]

while True:
    answer = input("Guess a number or type q to quit.")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("please type a number or q to quit.")
    if answer in numbers:
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly!")


#5
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []
for i in list1:
    for j in list2:
        list3.append(i * j)
        
print(list3)

#5_解答
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []

for i in list1:
    for j in list2:
        mult = i * j
        list3.append(i * j)

print(list3)


