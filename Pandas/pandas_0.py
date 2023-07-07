import pandas as pd



#0
#fruits = pd.DataFrame({"Apples":[30], "Bananas":[21]})
#print(fruits)

#1
#fruit_sales = pd.DataFrame({"Apples":[35, 41], "Bananas":[21,34]}, index=["2017 Sales", "2018 Sales"])
#print(fruit_sales)

"""
#2
liking = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

print(liking)
"""

"""
#3
sales = pd.Series([30, 35, 40.2], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print(sales)
"""

fruit_prices = pd.read_csv("data\Fruit_Prices_2020.csv")# index_col=0

#titles are Fruit,Form,RetailPrice,RetailPriceUnit,Yield,CupEquivalentSize,CupEquivalentUnit,CupEquivalentPrice
#print(fruit_prices)
#print(fruit_prices.iloc[2] )
#print(len(fruit_prices ))
"""
for fr in range(len(fruit_prices)):
    if fruit_prices.iloc[fr].RetailPrice > 5:
        print(fruit_prices.iloc[fr].Fruit, fruit_prices.iloc[fr].Form)

"""

#print(fruit_prices.iloc[0:3, :4])
#print(fruit_prices.sample()) #this one selects a random row
#print(fruit_prices.iloc[[2,4,6], 0:5])#to index specific rows
#print(fruit_prices.iloc[-2, :] )
print(type(fruit_prices))
#print(fruit_prices.loc[:, ["Fruit", "Form", "RetailPrice"] ])
#print(fruit_prices.loc[fruit_prices.RetailPrice > 6, ["Fruit", "Form", "RetailPrice"]] )
print(sum(fruit_prices.RetailPrice>5))#using len returns ALL the resutls, True or False

#print(dir(fruit_prices.Fruit))
#print(sum((fruit_prices.RetailPrice>5)  ))
