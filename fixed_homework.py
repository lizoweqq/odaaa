# очікуваний результат у вигляді: My name is David, I am 14 years old👣

# example
# f = '\N{Footprints}'  # not informative naming, the correct code below
smile_footprint = '\U0001F463'

user_name = "David"
user_age = 14
result = "My name is " + user_name + ", I am " + str(user_age) + " years old" + smile_footprint

print(result)
