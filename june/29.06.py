# iphone = 380000rub.
# скидка сначала 50%, а потом сделали снова скидку 50%
# iphone = ?

# 1) math
# 2) python solving


"""
answer 95000+

"""

price = 120000 # $
sale1 = 99 # % 100% = 1, 50% = 0.5
sale2 = 99 # %
sale3 = 99
# solution:
newprice1 = price-(price*sale1/100)

newprice2 = newprice1-(newprice1*sale2/100)

newprice3 = newprice2-(newprice2*sale3/100)

print ("after first sale: " + str(newprice1) + "$")
print ("after second sale: " + str(newprice2)+ "$")
print ("after second sale: " + str(newprice3)+ "$")