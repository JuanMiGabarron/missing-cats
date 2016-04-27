import json
import random

from missing_cats.owner import Owner
from missing_cats.stations_graph import StationsGraph


# load the json files
def load_file(filename):
    with open(filename) as data_file:
        return json.load(data_file)


# get 2 random stations, they must be diferent
def get_random_pair(stations):
    pair1 = random.choice(stations)
    while True:
        pair2 = random.choice(stations)
        if pair1 != pair2:
            break
    return pair1, pair2


# run the main program
def run(num_owners):
    N = num_owners
    MAX_MOVEMENTS = 100000
    average_text = 'Average number of movements required to find a cat: {}'

    stations = load_file('data/tfl_stations.json')
    connections = load_file('data/tfl_connections.json')
    stations_graph = StationsGraph(stations, connections)

    list_owners = []

    for i in range(N):
        id_station_own, id_station_cat = get_random_pair(
            stations_graph.get_stations_ids())
        owner = Owner(i, stations_graph)
        owner.travel(stations_graph.find_station_by_id(id_station_own))
        owner.cat.travel(stations_graph.find_station_by_id(id_station_cat))
        list_owners.append(owner)

    cats_found = 0

    for i in range(MAX_MOVEMENTS):
        owner_without_cat = filter(
            lambda x: x if not x.cat_found else None,
            list_owners)
        for owner in owner_without_cat:
            if owner.is_looking_cat():
                cats_found += 1
                owner.found_cat()
            else:
                owner.cat.move()
                owner.move()

    happy_owners = filter(lambda x: x if x.cat_found else None, list_owners)

    print 'Total number of cats: ' + str(N)
    print 'Number of cats found: ' + str(cats_found)
    print average_text.format(average_movements(happy_owners))
    owner_max_movements(happy_owners)


# get the average movements by the owners trying to find their cats
def average_movements(owners):
    sum_movements = sum(map(lambda x: x.movements, owners))
    return sum_movements/len(owners) if sum_movements > 0 else 0


# get the owner with the greatest number of movements
def owner_max_movements(owners):
    max_owner = None
    for owner in owners:
        if max_owner is None or owner.movements > max_owner.movements:
            max_owner = owner
    if max_owner:
        print 'The owner {} has more movements with {}'.format(
            max_owner.id,
            max_owner.movements)


# Read how many cats run away
def read_owners():
    N = raw_input('Input the number of owners and cats: ')
    if N.isdigit() and N >= 1:
        return int(N)
    else:
        raise ValueError('Not a number or number is less than 1')

if '__main__' == __name__:
    num = read_owners()
    run(num)
