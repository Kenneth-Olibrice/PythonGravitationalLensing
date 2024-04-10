import pandas as pd
import math
from Util import read_data, gnomonic_projection, average
import matplotlib.pyplot as plt

star_names = ["50Alp", "48Bet", "85Eta", "64Gam", "69Sig",
              "77Eps", "79Zet"]
stars = []
target_stars = []
read_data("../res/bsc5.dat", stars)
df = pd.DataFrame(stars)
data = [[], [], [], [], []]

displacement = (1.75 / 60) / 60

for star in stars:
    if star.constellation == "UMa" and star.name[:6].strip(" ") in star_names:
        target_stars.append(star)

avg_ra = average([star.coord.ra.deg for star in target_stars])
avg_dec = average([star.coord.dec.deg for star in target_stars])

for star in target_stars:
    print(f"Name: {star.name[:6].strip(" ")} , {star.coord.ra.deg} , {star.coord.dec.deg} ")
    r = (avg_ra - star.coord.ra.deg, avg_dec - star.coord.dec.deg)
    length = math.sqrt(math.pow(r[0], 2) + math.pow(r[1], 2))
    displaced_ra = star.coord.ra.deg + displacement * math.cos(r[0] / length)
    displaced_dec = star.coord.dec.deg + displacement * math.sin(r[1] / length)

    x1, y1 = gnomonic_projection(star.coord.ra.deg, star.coord.dec.deg, avg_ra, avg_dec, 1)
    x, y = gnomonic_projection(displaced_ra, displaced_dec, avg_ra, avg_dec, 1)
    data[0].append(x)
    data[1].append(y)
    data[3].append(x1)
    data[4].append(y1)

    if star.name[:6].strip(" ") in star_names:
        data[2].append(6)
    else:
        data[2].append(0)


for i in range(len(data[0])):
    plt.plot([data[0][i]], [data[1][i]], 'ro')
    plt.plot([data[3][i]], [data[4][i]], 'bo')
plt.show()
