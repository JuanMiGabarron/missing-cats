from station import Station


class StationsGraph(object):

    def __init__(self, stations, connections):
        self.graph = {}
        self._set_stations(stations)
        self._set_connected_stations(connections)

    # set the stations in the graph
    def _set_stations(self, stations):
        for station in stations:
            id_station, name_station = station
            self.graph[Station(id_station, name_station)] = []

    # set all the vertex of the graph
    def _set_connected_stations(self, connections):
        for connection in connections:
            id_1, id_2 = connection
            station1 = self.find_station_by_id(id_1)
            station2 = self.find_station_by_id(id_2)
            self.graph[station1].append(station2)
            self.graph[station2].append(station1)

    # find a station only by the id
    def find_station_by_id(self, id_station):
        for station in self.graph.keys():
            if station.id_station == id_station:
                return station

    # find all the stations connected of one station
    def find_connections(self, station):
        return self.graph.get(station)

    def get_stations_ids(self):
        return map(lambda x: x.id_station, self.graph.keys())
