import pandas as pd
import math
from Util import read_data, gnomonic_projection, average_ra_dec, lens
import matplotlib.pyplot as plt

print("Parsing bsc5 data...")
bsc5_path = "../res/bsc5.dat"
data = []
read_data(bsc5_path, data)

# Relative magnitude is graded using greek letters,
# with alpha being the brightest stars in a given constellation and so on.
# We are only interested in the brightest stars; those that make up familiar pictures like the big dipper.
desired_brightness = ["Alp", "Bet", "Gam", "Del", "Eps", "Zet", "Eta"]

constellation_names = {
    "Ari": "Aries",
    "Aqr": "Aquarius",
    "Cnc": "Cancer",
    "Cap": "Capricornus",
    "Gem": "Gemini",
    "Leo": "Leo",
    "Lib": "Libra",
    "Sgr": "Sagittarius",
    "Sco": "Scorpius",
    "Tau": "Taurus",
    "UMa": "Ursa Major",
    "Vir": "Virgo"
}

print("Which constellation would you like to view? (enter a number)")
name_index = 1
for key in constellation_names:
    print(f"{name_index}. {constellation_names[key]}")
    name_index += 1

choice = list(constellation_names.keys())[int(input()) - 1]

stars_to_view = []
for star in data:
    if choice in star.name:
        verify_count = 0
        for brightness in desired_brightness:
            if brightness in star.name:
                stars_to_view.append(star)

average_ra, average_dec = average_ra_dec(stars_to_view)

print(stars_to_view)
raw_x_values = []
raw_y_values = []
lensed_x_values = []
lensed_y_values = []

for star in stars_to_view:
    px, py = gnomonic_projection(star.coord.ra.deg, star.coord.dec.deg, average_ra, average_dec, 0.25)
    raw_x_values.append(px)
    raw_y_values.append(py)

    lensed_ra, lensed_dec = lens(star, average_ra, average_dec)
    plx, ply = gnomonic_projection(lensed_ra, lensed_dec, average_ra, average_dec, 0.25)
    lensed_x_values.append(plx)
    lensed_y_values.append(ply)

plt.title(f"{constellation_names[choice]}")
plt.plot(raw_x_values, raw_y_values, 'bo')
plt.plot(lensed_x_values, lensed_y_values, 'ro')
plt.savefig(f"../finished/{choice}.png")
plt.show()

