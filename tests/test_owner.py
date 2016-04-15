import unittest

from missing_cats.owner import Owner
from missing_cats.stations_graph import StationsGraph


class TestCat(unittest.TestCase):

    def test_cat(self):
        stations = [
            ["1", "Acton Town"],
            ["2", "Aldgate"],
            ["3", "Some other"],
        ]
        connections = [
            ["1", "2"],
            ["1", "3"],
        ]

        stations_graph = StationsGraph(stations, connections)
        owner = Owner(3, stations_graph)

        self.assertEquals(owner.id, 3, "The owner id is wrong")

        current_station = stations_graph.find_station_by_id("2")
        owner.travel(current_station)
        self.assertEquals(
            owner.current_station,
            current_station,
            'The current station of the cat is wrong')

        owner.cat.travel(current_station)
        self.assertTrue(
            owner.is_looking_cat(),
            'The cat not found but it is in the same station')
        owner.found_cat()
        self.assertTrue(
            owner.cat_found,
            'cat found is false, but the owner has the cat'
            )

        owner.move()
        self.assertNotEquals(
            owner.current_station,
            current_station,
            'The movement of the cat is wrong')

        owner.move()  # move to visit the third station
        self.assertEquals(
            len(owner.visited_stations),
            3,
            'The visited stations has the wrong number of stations')

        # move to a random location (the next random station is 1)
        owner.move()
        next_station = stations_graph.find_station_by_id("1")

        self.assertEquals(
            owner.current_station,
            next_station,
            'Owner fails to travel to a random station'
            )

        owner.move()  # move to the station 2 or 3
        next_station.close()  # close the station 1
        owner.move()  # Try to move to station 1

        self.assertFalse(
            owner.able_to_move,
            'The owner is stuck but he still can travel')
