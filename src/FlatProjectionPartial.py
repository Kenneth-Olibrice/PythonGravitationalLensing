import pandas as pd

from Util import read_data, gnomonic_projection
import math
import matplotlib.pyplot as plt
import seaborn as sns

star_names = ["50Alp", "48Bet", "85Eta", "64Gam", "69Sig",
              "77Eps", "79Zet"]
stars = []
read_data("../res/bsc5.dat", stars)
df = pd.DataFrame(stars)
count = 0
data = [[], []]

for star in stars:
    if star.constellation == "UMa" and star.name[:6].strip(" ") in star_names:
        count += 1
        # print(f"{star.coord.ra} , {star.coord.dec}  {star.name}")
        print(f"Name: {star.name[:6].strip(" ")} , {star.coord.ra.deg} , {star.coord.dec.deg} ")
        x, y = gnomonic_projection(star.coord.ra.deg, star.coord.dec.deg, 10, 40, 3)
        data[0].append(x)
        data[1].append(y)

# for x in data[0]:
#     print(x)

plt.plot(data[0], data[1], 'ro')
plt.show()
