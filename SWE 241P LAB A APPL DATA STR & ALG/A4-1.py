# Task—1

from collections import deque
class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.connected_cities = []
        self.visited = False

    def add_connected_city(self, city):
        self.connected_cities.append(city)

# Task-2
class IslandArchipelago:
    def __init__(self):
        self.cities= {}
        self.num_cities = 0
    def add_city(self, name, population):
        city = City(name, population)
        self.cities[name] = city
        self.num_cities = self.num_cities + 1

    def get_city(self, target):
        if target in self.cities:
            return self.cities[target]
        else:
            return None

    def __contains__(self, x):
        return x in self.cities

    def connect_cities(self, city1_name, city2_name):
        city1 = self.cities.get(city1_name)
        city2 = self.cities.get(city2_name)
        # print(city2.name)
        if city1 and city2:
            city1.add_connected_city(city2)
            city2.add_connected_city(city1)

    def get_cities_keys(self):
        return self.cities.keys()

    def get_cities_values(self):
        return self.cities.values()

    def read_city_population(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                city_name, population = line.strip().split(' : ')
                # print(city_name, population)
                self.add_city(city_name, int(population))
    def read_road_network(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                city1_name, city2_name = line.strip().split(' : ')
                # print(city1_name, city2_name)
                self.connect_cities(city1_name, city2_name)

    def adjacency_list_representation(self):
        adjacency_list = {}
        for city_name, city in self.cities.items():
            # print(city_name,city)
            adjacency_list[city_name] = [connected_city.name for connected_city in city.connected_cities]
        return adjacency_list

# Task-3
    def dfs(self,city):
        city.visited = True
        for connected_city in city.connected_cities:
            if not connected_city.visited:
                self.dfs(connected_city)

    def count_islands(self,city_list):
        num_islands = 0
        for city in city_list:
            if not city.visited:
                num_islands += 1
                self.dfs(city)
        return num_islands

# Task—4
    def dfs_population(self, city):
        city.visited = True
        population = city.population
        for connected_city in city.connected_cities:
            if not connected_city.visited:
                population += self.dfs_population(connected_city)
        return population

    def calculate_island_populations(self, city_list):
        populations = []
        for city in city_list:
            if not city.visited:
                island_population = self.dfs_population(city)
                populations.append(island_population)
        return populations

# Task—5
    @staticmethod
    def bfs(graph, start, end):
        # Create a queue to store nodes to be visited
        queue = deque()
        # Create a set to store visited nodes
        seen = set()
        # Create a dictionary to store the parent node of each node
        parent = {}
        queue.append(start)
        seen.add(start)

        while queue:
            node = queue.popleft()
            if node == end:
                path = []
                while node != start:
                    path.append(node)
                    node = parent[node]
                path.append(start)
                path.reverse()
                return len(path)-1
            else:
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        queue.append(neighbor)
                        seen.add(neighbor)
                        parent[neighbor] = node
        return 'NAN'


# Test
if __name__ == "__main__":
    archipelago = IslandArchipelago()

    # Read the files
    archipelago.read_city_population('city_population.txt')
    archipelago.read_road_network('road_network.txt')

    # Task2: Get the adjacency list representation of the city graph
    adjacency_list = archipelago.adjacency_list_representation()
    print(adjacency_list)

    #Task3: Test count_islands
    # city_list = archipelago.get_cities_values()
    # amount = archipelago.count_islands(city_list)
    # print(amount)
    #
    # for city in city_list:
    #     city.visited = False

    # # Task4: Test calculate_island_populations
    # population = archipelago.calculate_island_populations(city_list)
    # print(population)

    # Task5: min_num_pathways
    city_list = list(archipelago.get_cities_keys())
    start = city_list[0]
    end = city_list[5]
    num_path = archipelago.bfs(adjacency_list,start,end)
    print(num_path)




















