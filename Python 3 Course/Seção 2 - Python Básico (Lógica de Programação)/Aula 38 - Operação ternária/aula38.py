logged_user = False

if logged_user:
    msg = 'User logged'
else:
    msg = 'User not logged'

# Mesma função

logged_user = False
msg = 'User logged' if logged_user else 'User not logged'

# ____________________________________

idade = 18

if idade >= 18:
    print('Access granted')
else:
    print('Access denied')

print(msg)

# Mesma função

idade = 17
eMaior = idade >= 18
msg = 'Access granted' if eMaior else 'Access denied'

print(msg)
