import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
q = int(input('How many quarters? '))
d = int(input('How many dimes? '))
n = int(input('How many nickels? '))
p = int(input('How many pennies? '))
sum = 0
if q > 0:
    sum += round(q * .25, 2)
if d > 0:
    sum += round(d * .1, 2)
if n > 0:
    sum += round(n * .05, 2)
if p > 0:
    sum += round(p * .01, 2)
print('\nYou have a total of', locale.currency(round(sum, 2))+'\n',
      locale.currency(round(q * .25, 2))+' in quarters\n',
      locale.currency(round(d * .1, 2))+' in dimes\n',
      locale.currency(round(n * .05, 2))+' in nickels\n',
      locale.currency(round(p * .01, 2))+' in pennies\n')
