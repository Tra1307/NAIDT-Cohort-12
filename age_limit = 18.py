age_limit = 18

dd = int(input('What is your age?'))

if dd >= age_limit:
    print('You are allowed to vote')
else:
    print('you have to be', age_limit,'to vote')