import csv
from ds.graph import Graph
from util.strings import CSV_DISTANCE_FILE_PATH


class DistanceManager:
    def __init__(self):
        # Initialize a Graph to store distance data
        self.graph = Graph()
        # Load distance data from CSV file
        self._load_distances_from_csv()

    def _load_distances_from_csv(self):
        # Read and process the CSV file containing distance data
        with open(CSV_DISTANCE_FILE_PATH) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for i, row in enumerate(csv_reader):
                for j, distance in enumerate(row):
                    if distance == '':
                        distance = None
                    else:
                        distance = float(distance)
                    self.graph.add_edge(i + 1, j + 1, distance)
        # Uncomment the following line if you want to print a confirmation message
        # print("Distance data successfully loaded.")

    def get_distance(self, origin, destination):
        # Retrieve the distance between two locations
        return self.graph.get_edge_weight(origin, destination)
