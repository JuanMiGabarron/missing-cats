

class Station(object):

    def __init__(self, id_station, station_name):
        self.id_station = id_station
        self.station_name = station_name
        self.open_station = True

    # station in maintenance, cleaning love
    def close(self):
        self.open_station = False
