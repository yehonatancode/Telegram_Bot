import random


d = dict.fromkeys((range(1000)))
for i in range(1000):
    #You can choose the bounds of the random, the range wasn't mentioned in the question
     d[i] = random.randint(1,1000)

print("Please enter your desired number to pick off dictionary")
x = input()
x=int(x)

#the punch in this question is that dictionary is not a direct-access data structure.
print(d)
num = list(d.values())[0] #getting the base value-key in the dictionary
for i in range(x+1): #the index starts off 0, therefore needs to be incremented by 1
    num = int(d[i])
print(num)

#print(num)