count = 0
names =[]
people = int(input("Enter number of people: "))
letter = input("Enter letter to be searched: ")
for name in range(people):
    names.append(input("Name: "))

for name in names:
    for n in name:
        if n.lower == letter.lower():
            count += 1
else:
    print("Total number of "+letter+": "+str(count))