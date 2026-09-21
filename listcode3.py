L1 = [ 4, 6, 8, 7, 3, 5, 1, 10, 12, 15 ]
count_Even = 0
count_Odd = 0

for i in range(0, 10, 1):
   if (L1[i])%2 == 1:
      count_Odd = count_Odd + 1

   else:
      count_Even = count_Even + 1

print(count_Odd)
print(count_Even)

