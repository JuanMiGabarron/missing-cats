

# Base class which contains common method
class BaseUser(object):

    def __init__(self, id, graph):
        self.id = id
        self.stations_graph = graph
        self.visited_stations = []
        self.movements = 0
        self.able_to_move = True

    # check open stations to travel
    def check_available_stations(self, connections):
        return filter(lambda x: x if x.open_station else None, connections)

    # travel to the next station
    def travel(self, next_station):
        self.current_station = next_station
        self._visit_station(next_station)
        self._move()

    # visit a new station (I hope my cat is here - worried owner)
    def _visit_station(self, station):
        if station not in self.visited_stations:
            self.visited_stations.append(station)

    # You make a move when you change your current station
    def _move(self):
        self.movements += 1

    # check if is a valid location
    def get_non_visisted_stations(self, stations):
        return filter(
            lambda x: x if x not in self.visited_stations else None,
            stations)
