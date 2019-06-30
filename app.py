print('Welcome to a car game')
print('''start - To start the car
stop - To stop the car
Quit - To quit''')
started = False
command = input('>').lower()
while command != 'quit':
    if command == 'start':
        if started:
            print('Car has already started')
        else:
            started= True
            print('Car has started')

    elif command == 'stop':
        if not started:
            print('Car has already stopped')
        else:
            print('Car has stopped')
            started=False
    else:
        print('Sorry I cannot understand')
    command = input('>').lower()