import math

def closest(points, target_point):
    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    closest_point = points[0]
    shortest_distance = distance(target_point, closest_point)
    
    for point in points[1:]:
        current_distance = distance(target_point, point)
        if current_distance < shortest_distance:
            closest_point = point
            shortest_distance = current_distance

    return closest_point


def closest(points, target_point):
    def distance(point):
        x, y = point
        dx = x - tx
        dy = y - ty
        return dx**2 + dy**2

    tx, ty = target_point
    return min(points, key=distance)
