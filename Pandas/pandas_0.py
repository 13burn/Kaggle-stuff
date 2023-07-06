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

fruit_prices = pd.read_csv("data\Fruit_Prices_2020.csv")
print(fruit_prices.head() )
