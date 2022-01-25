import time

i = int
i = 1
while (i >= 1):
    in1 = int(input('Set a timer for (seconds):'))
    print(in1, '\n')
    time.sleep(1)
    while in1 > 0:
        in1 -= 1
        print(in1, '\n')
        time.sleep(1)
    print('Time is Up!')
    in2 = 'n'
    while(in2 != 'N' and in2 != 'Y'):
        in2 = input('Set another timer? Y/N: ')
        if in2 == 'N':
            i = 0
        elif in2 == 'Y':
            i = 1
