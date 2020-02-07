a = 0 
for i in range(5):
    a += 1
    if a == 3:
        pass
    a += 5
print(a)
a = 0
for i in range(5):
    a += 1
    if a == 3:
        continue
    a += 5
print(a)