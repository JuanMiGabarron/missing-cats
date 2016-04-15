import random

from cat import Cat
from base_user import BaseUser


class Owner(BaseUser):

    def __init__(self, id, graph):
        super(Owner, self).__init__(id, graph)
        self.cat = Cat(id, graph)
        self.cat_found = False

    # looking for the cat!
    def is_looking_cat(self):
        return self.current_station == self.cat.current_station

    # we found our lovely cat yay!
    def found_cat(self):
        self.cat_found = True
        self.current_station.close()  # love is in the air
        print "Owner {} found cat {} - {} is now closed".format(
            self.id,
            self.cat.id,
            self.current_station.station_name)

    # move to another non-visited station, if is possible
    def move(self):
        if self.able_to_move:
            connections = self.stations_graph.find_connections(
                self.current_station)
            available_stations = self.check_available_stations(connections)
            if available_stations:
                non_visited = self.get_non_visisted_stations(
                    available_stations)
                if non_visited:
                    self.travel(random.choice(non_visited))
                else:
                    self.travel(random.choice(available_stations))
            else:
                self.able_to_move = False
