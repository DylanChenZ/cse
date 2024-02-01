tc = int(input())
array = []
for i in range(tc):
  array.append(int(input()))
array.sort()
print("fastest: " + str(array[1]), "slowest: " + str(array[len(array)-1]), sep="\n")
print("average: " + str(sum(array)/len(array)))