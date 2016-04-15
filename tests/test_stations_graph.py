import unittest

from missing_cats.stations_graph import StationsGraph


class TestStationsGraph(unittest.TestCase):

    def test_stations_graph(self):
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
        self.assertEqual(len(stations_graph.find_connections(
            stations_graph.find_station_by_id('1'))),
            2,
            'Station with id 1 has wrong number of connections')

        self.assertFalse(
            stations_graph.find_station_by_id(3),
            'Station with id 3 not found'
            )

        self.assertEqual(
            sorted(stations_graph.get_stations_ids()),
            ['1', '2', '3'],
            'The ids of the stations are wrong')
