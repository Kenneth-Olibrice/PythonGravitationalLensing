import math
from math import cos, sin, radians, pi
from dataclasses import dataclass
from astropy.coordinates import SkyCoord

@dataclass(order=True)
class StarData:
    name: str
    coord : SkyCoord
    constellation: str
    Vmag: float


def parse_float(n):
    try:
        return float(n)
    except ValueError:
        return None


def parse_int(n):
    try:
        return float(n)
    except ValueError:
        return None


def read_data(path, data):
    with open(path) as catalog:
        buffer = catalog.readlines()
        for line in buffer:
            try:
                ra = parse_float(line[75:77]) + parse_float(line[77:79]) / 60 + parse_float(line[79:83]) / 3600
                dec = parse_float(line[84:86]) + parse_float(line[86:88]) / 60 + parse_float(line[88:90]) / 3600
                data.append(StarData(line[4:14], SkyCoord(ra=ra, dec=dec, unit='deg'), line[11:14].strip(), parse_float(line[102:107])))
            except:
                continue


def gnomonic_projection(star_ra, star_dec, center_ra, center_dec, scale):
    alpha = radians(star_ra)
    delta = radians(star_dec)
    alpha0 = radians(center_ra)
    delta0 = radians(center_dec)

    A = cos(delta) * cos(alpha - alpha0)
    F = scale * (180/pi) / (sin(delta0) * sin(delta) + A * cos(delta0))

    LINE = -F * (cos(delta0) * sin(delta) - A * sin(delta0))
    SAMPLE = -F * cos(delta) * sin(alpha - alpha0)

    return SAMPLE, LINE


def average_ra_dec(stars):
    stars_ra = []
    stars_dec = []
    for star in stars:
        stars_ra.append(star.coord.ra.deg)
        stars_dec.append(star.coord.dec.deg)

    return sum(stars_ra) / len(stars_ra), sum(stars_dec) / len(stars_dec)


# Takes a star and returns a ra and dec after applying a lensing operation
def lens(star, center_ra, center_dec):
    displacement = 1.75 / 3600 # Displacement of 1.75"

    # Calculate the vector between the given star and the center of lensing
    vec_ra = center_ra - star.coord.ra.deg
    vec_dec = center_dec - star.coord.dec.deg
    vec_magnitude = math.sqrt(math.pow(vec_ra, 2) + math.pow(vec_dec, 2))

    # Normalize the vector
    vec_ra /= vec_magnitude
    vec_dec /= vec_magnitude

    displaced_ra = star.coord.ra.deg + displacement * math.cos(vec_ra)
    displaced_dec = star.coord.dec.deg + displacement * math.sin(vec_dec)

    return displaced_ra, displaced_dec


def evil_sin(x):
    return x - ((x*x*x) / math.factorial(3)) + ((x*x*x*x*x) / math.factorial(5)) - ((x*x*x*x*x*x*x) / math.factorial(7))


def evil_cos(x):
    return 1 - ((x*x) / math.factorial(2)) + ((x*x*x*x) / math.factorial(4)) - ((x*x*x*x*x*x) / math.factorial(6))
