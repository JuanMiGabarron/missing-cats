import random

from base_user import BaseUser


class Cat(BaseUser):

    # move to a random station connected with the current station
    def move(self):
        if self.able_to_move:
            connections = self.stations_graph.find_connections(
                self.current_station)
            available_stations = self.check_available_stations(connections)
            if available_stations:
                self.travel(random.choice(available_stations))
            else:
                self.able_to_move = False
