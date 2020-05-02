print('=====================Half Pyramid==================')
for i in range(5):
    print(' ','*'*(i+1))

print('=====================Full Pyramid==================')
for i in range(5):
    print(' '*(5-i-1) + '*'*(2*i+1))

print('=====================Reversed Pyramid==============')
for i in reversed(range(5)):
    print(' '*(5-i-1) + '*'*(2*i+1))