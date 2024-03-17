import matplotlib.pyplot as plt
import pandas as pd
from Util import read_data


data = []

read_data("../res/bsc5.dat", data)
df = pd.DataFrame(data)

# df.to_csv("../res/star_data.csv")

# Allows you to plot a constellation with ra on the x-axis and dec on the y-axis
target_constellation = "Peg"  # Edit this to pick a specific constellation
for star in data:
    format = 'bo'
    if star.constellation == target_constellation:
        format = 'ro'

    plt.plot([star.right_ascension], [star.declination], format)

plt.show()
