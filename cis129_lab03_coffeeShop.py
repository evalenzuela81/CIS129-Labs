print('***************************************\nMy Coffee and MUffin Shop')
#creates the user input of how many coffees are purchased    
coffeePurchased = int(input("Number of Coffee's Bought?\n"))
#creates the user input of how many muffins are purchased  
muffinsPurchased = int(input("Number of Muffin's Bought?\n"))
#new items
cakePurchased = int(input("Number of Cake's Bought?\n"))
print('***************************************\n\n***************************************')

print('My Coffee and Muffin Receipt')
# two variables that declare the price of the muffin and coffee   
coffee = int(5)
muffin = int(4)
cake = int(6)
# multiplys the set price of coffee/muffins by the users input of how many were purchased
c = coffee * coffeePurchased
m = muffin * muffinsPurchased
ck = cake * cakePurchased

print(coffeePurchased,"Coffee's at $",coffee,'each: $',c)
print(muffinsPurchased,"Mufin's at $",muffin,'each: $',m)
print(cakePurchased,"Cake's at $",cake,'each: $', ck)
# takes total cost of the coffee/muffins and multiplies them by .06 to get the amount of tax money 
tax = (float(c + m + ck) * .06)
# adds all the prices together the total cost of the coffee/muffins and tax cost
total = (float(c + m + ck) + tax)

print('6% tax: $', tax)
print('---------')

print('Total: $',total)
print('***************************************\n\n***************************************')
