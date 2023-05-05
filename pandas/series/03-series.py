import pandas as pd

sushi = {
    "salmon": "orange",
    "tuna": "red",
    "sashimi": "green"
}

new_series1 = pd.Series(sushi)
print(new_series1)

list1 = ["apple", "banana", "orange"]
labels1 = ["fruit1", "fruit2", "fruit3"]

new_series2 = pd.Series(list1, labels1)
print(new_series2)

