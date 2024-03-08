from data.manager.distance_manager import DistanceManager


class RoutingManager:
    def __init__(self):
        # Initialize with a DistanceManager instance
        self.distance_manager = DistanceManager()

    def route(self, address_ids: list):
        # Calculate the optimal route given a list of address IDs
        global last_point
        points_count = len(address_ids)
        visited = [False] * points_count
        # Start the path with the first address and its distance from the hub (address ID 1)
        path = [(address_ids[0], self.distance_manager.get_distance(1, address_ids[0]))]
        visited[0] = True

        for _ in range(1, points_count):
            last_point = path[-1][0]  # Last visited point
            nearest_neighbor = None  # Nearest neighbor to the last visited point
            min_distance = float('inf')  # Initialize minimum distance to infinity

            for i, point in enumerate(address_ids):
                if not visited[i]:
                    distance = self.distance_manager.get_distance(last_point, point)
                    if distance < min_distance:
                        nearest_neighbor = point
                        min_distance = distance

            path.append((nearest_neighbor, min_distance))
            visited[address_ids.index(nearest_neighbor)] = True

        # Return to the hub (address ID 1) after visiting all points
        return path + [(1, self.distance_manager.get_distance(last_point, 1))]
