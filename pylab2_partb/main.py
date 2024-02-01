sum = 0
total_word = 0
while 1:
 temp_len = len(str(input("Word: ")))
 if temp_len == 0:
   break
 sum += temp_len
 total_word += 1
print(sum/total_word)
