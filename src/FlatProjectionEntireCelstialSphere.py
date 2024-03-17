import matplotlib.pyplot as plt
from dataclasses import dataclass
import pandas as pd
from StarData import StarData

def parse_float(n):
    try:
        return float(n)
    except:
        return None

data = []
with open("../res/bsc5.dat") as catalog:
    buffer = catalog.readlines()
    for line in buffer:
        try:
            ra = parse_float(line[75:77]) + parse_float(line[77:79]) / 60 + parse_float(line[79:83]) / 3600
            dec = parse_float(line[84:86]) + parse_float(line[86:88]) / 60 + parse_float(line[88:90]) / 3600
            data.append(StarData(line[4:14], ra, dec, line[11:14].strip(), parse_float(line[102:107])))
        except:
            continue

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
