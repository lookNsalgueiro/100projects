print('Welcome to Treasue Island.')

print('Your mission is to find the treasure.')
answer1 = input(f'Do you wanna go left or right?').lower()
if answer1 == "right":
    print('Game Over!')
elif answer1 == "left":
    print('Nice! lets continue...')

    print('There is a lake in front of you...')
    answer2 = input(f'Do you want to swin or wait ?').lower()
    if answer2 == "swin":
        print('Game Over!')
    elif answer2 == "wait":
        print('Nice! lets continue...')

        print('There is three doors in front of you')
        answer3 = input(f'Witch door do you choose?').lower()
        if answer3 == "yellow":
            print('You Win!')
        elif answer3 == "red":
            print('Game Over!')
        elif answer3 == "blue":
            print('Game Over!')
        else:
            print('Please choose a valid answer!')
    else:
        print('Please choose a valid answer!')
else:
    print('Please choose a valid answer!')