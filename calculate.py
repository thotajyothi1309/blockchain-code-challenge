import itertools
import math
def calculate_distance(point1, point2):
    """
    Calculate the Euclidean distance between two points.
    Args:
    point1 (tuple): The coordinates of the first point.
    point2 (tuple): The coordinates of the second point.
    Returns:
    float: The distance between the two points.
    """
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
def total_route_distance(route):
    """
    Calculate the total distance of a route.
    Args:
    route (list): A list of points representing the route.

    Returns:
    float: The total distance of the route.
    """
    distance = 0
    for i in range(len(route) - 1):
        distance += calculate_distance(route[i], route[i + 1])
    return distance
def optimize_route(locations, priorities):
    """
    Optimize a route based on priority and distance.
    Args:
    locations (list): A list of points representing the locations.
    priorities (list): A list of priorities corresponding to the locations.
    Returns:
    tuple: The optimized route and the total distance.
    """
    prioritized_locations = list(zip(locations, priorities))
    priority_order = {'high': 0, 'medium': 1, 'low': 2}
    prioritized_locations.sort(key=lambda x: priority_order[x[1]])
    sorted_locations = [loc for loc, _ in prioritized_locations]
    best_route = None
    min_distance = float('inf')
    for perm in itertools.permutations(sorted_locations):
        current_distance = total_route_distance(perm)
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = perm
    return best_route, min_distance
def get_coordinates(prompt):
    while True:
        try:
            x, y = map(int, input(prompt).split())
            return x, y
        except ValueError:
            print("Invalid input. Please enter two integer values separated by a space.")
def get_priority(prompt):
    while True:
        priority = input(prompt).strip().lower()
        if priority in ['high', 'medium', 'low']:
            return priority
        print("Invalid input. Please enter 'high', 'medium', or 'low'.")
def main():
    locations = []
    priorities = []
    n = int(input("Enter the number of delivery locations: "))
    for i in range(n):
        x, y = get_coordinates(f"Enter coordinates for location {i + 1} (x y): ")
        priority = get_priority(f"Enter priority for location {i + 1} (high, medium, low): ")
        locations.append((x, y))
        priorities.append(priority)

    optimized_route, total_distance = optimize_route(locations, priorities)
    print("Optimized Route:", optimized_route)
    print("Total Distance: {:.2f} units".format(total_distance))
if __name__ == "__main__":
    main()