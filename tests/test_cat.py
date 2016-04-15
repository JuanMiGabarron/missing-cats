import unittest

from missing_cats.cat import Cat
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
        cat = Cat(1, stations_graph)

        self.assertEquals(cat.id, 1, "This is not our cat!")

        current_station = stations_graph.find_station_by_id("1")
        cat.travel(current_station)
        self.assertEquals(
            cat.current_station,
            current_station,
            'The current station of the cat is wrong')

        cat.move()
        self.assertNotEquals(
            cat.current_station,
            current_station,
            'The movement of the cat is wrong')

        current_station.close()
        cat.move()
        self.assertFalse(
            cat.able_to_move,
            'The cat is stuck but it can travel')