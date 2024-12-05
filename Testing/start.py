#Mad libs help

import secrets

listvar = ["number","noun","adj"]
print(listvar)
#newListvar = list(map(str, input("Put in information: ").split()))
#print(newListvar)

#for i in range(20):
    #x = random.randrange(1,4,1)
    #print(x)
x = secrets.SystemRandom().randrange(1,4,1)
print(x)

if x == 1:
    print("Print this")
elif x == 2:
    print("No this")
else:
    print("No print this")

word = secrets.choice(['needed_input0', 'need_input1', 'needed_input2'])
print(word)

#for i in range(20):
#    word = random.choice(['needed_input0', 'need_input1', 'needed_input2'])
#    print(word)

if word == 'needed_input0':
    print('Hi')
else:
    print('No')
