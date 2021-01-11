import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(p1, p2):
        return math.sqrt(((p1.x - p2.x)**2) + ((p1.y - p2.y)**2))

p1 = Point(1.5, 1)
p2 = Point(1.5, 2)

print(p1.dist(p2)) # 1.0