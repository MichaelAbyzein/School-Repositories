a = '1'
s = 0
print('Enter Numbers to add to the sum.')
print('Enter q or Q to quit.')

a = input('Number? ')

while a == 'q' and a == 'Q':
    print('Total Sum:', s)
    a = '0'

while a != 'q' and a != 'Q':
    a = float(a)
    s = s + a
    print('Current Sum:', s)
    a = input('Number? ')

while a == '':
    a = input('Insert something you dummy!')
print('Total Sum: ', s)