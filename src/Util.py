from dataclasses import dataclass


@dataclass(order=True)
class StarData:
    name: str
    right_ascension: float
    declination: float
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
                data.append(StarData(line[4:14], ra, dec, line[11:14].strip(), parse_float(line[102:107])))
            except:
                continue