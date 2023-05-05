import pandas as pd

ice_cream = ["vanilla", "chocolate", "strawberry", "Rum Raisin"]
print(ice_cream)
print(type(ice_cream))
new_series1 = pd.Series(ice_cream)
print(new_series1)
print(type(new_series1))


lottery_numbers = [3, 5, 7, 9, 11, 13]
new_series2 = pd.Series(lottery_numbers)
print(new_series2)
