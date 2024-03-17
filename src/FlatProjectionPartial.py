from Util import read_data
import math
import matplotlib.pyplot as plt

data = []
radius = 16
scale = 1/radius
center = (0, 0)
print(center[0])
read_data("../res/bsc5.dat", data)
debounce = False

for star in data:
    if star.constellation == "Peg":
        if debounce == False:
            debounce = True
            center = (star.right_ascension, star.declination)

        alpha = (star.right_ascension / 24) * 2 * math.pi
        delta = (star.declination / 24) * 2 * math.pi
        A = math.cos(delta) * math.cos(alpha - center[1])
        F = scale * (180 / math.pi)/(math.sin(center[0]) * math.sin(delta) + A * math.cos(center[0]))

        LINE = -F * math.cos(center[0]) * math.sin(delta) - A * math.sin(center[0])
        SAMPLE = -F * math.cos(delta) * math.sin(alpha - center[1])
        plt.plot([LINE], [SAMPLE], f'{'ro' if star.Vmag > 5 else 'bo'}')

plt.show()

