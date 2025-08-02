factory_1= list(map(int, input().split()))#接收系統3行
factory_2 = list(map(int, input().split()))
people = int(input())
for i in range(people + 1):#找出所有可能的人員分配
    A = i
    B = people - i
    output_value1 = factory_1[0]*A**2 + factory_1[1]*A + factory_1[2]#最大收益公式
    output_value2 = factory_2[0]*B**2 + factory_2[1]*B + factory_2[2]
    if i == 0:#判斷是否已達最大收益 由for影響
        Gros＿output＿value = output_value1 + output_value2
    if output_value1 + output_value2 > Gros＿output＿value:
        Gros＿output＿value = output_value1 + output_value2
print(Gros＿output＿value)
#我一直在找最佳解 結果我自己想的就是最佳解XD