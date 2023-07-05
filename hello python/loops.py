#planets
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    #print(planet, end=' ') # print all on same line
    pass


loud_hsort_planets = [planet.upper() + "!" 
                      for planet in planets 
                      if len(planet) < 6]

print(loud_hsort_planets)

"""
#list comprehension
squares = [n**2 for n in range(10)]
print(squares)
"""