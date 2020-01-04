# list_ = [exp for var in iterable]

l1 = [i for i in range(1,11)]
l2 = [i*i for i in range(1,11)]
l3 = [i*i for i in range(1,11) if i%2==0]
l4 = [i + j for i in l1 for j in l2]
l5 = [i if i%2==0 else i*i for i in l1]
print("l1:",l1)
print("l2:",l2)
print("l3:",l3)
print("l4:",l4)
print("l5:",l5)
