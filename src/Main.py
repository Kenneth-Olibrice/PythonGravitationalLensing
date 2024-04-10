import pandas as pd

from Util import read_data, gnomonic_projection, average
import matplotlib.pyplot as plt

star_names = ["50Alp", "48Bet", "85Eta", "64Gam", "69Sig",
              "77Eps", "79Zet"]
stars = []
target_stars = []
read_data("../res/bsc5.dat", stars)
df = pd.DataFrame(stars)
data = [[], [], []]

for star in stars:
    if star.constellation == "UMa" and star.name[:6].strip(" ") in star_names:
        target_stars.append(star)

avg_ra = average([star.coord.ra.deg for star in target_stars])
avg_dec = average([star.coord.dec.deg for star in target_stars])

for star in target_stars:
    print(f"Name: {star.name[:6].strip(" ")} , {star.coord.ra.deg} , {star.coord.dec.deg} ")
    x, y = gnomonic_projection(star.coord.ra.deg, star.coord.dec.deg, avg_ra, avg_dec, 1)
    data[0].append(x)
    data[1].append(y)
    if star.name[:6].strip(" ") in star_names:
        data[2].append(6)
    else:
        data[2].append(0)


for i in range(len(data[0])):
    plt.plot([data[0][i]], [data[1][i]], 'ro' if data[2][i] > 5 else 'bo')
plt.show()
