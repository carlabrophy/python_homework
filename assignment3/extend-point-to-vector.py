import math


class Point:
    """Represent a point in two-dimensional space."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        """Return True when two points have equal x and y values."""
        if not isinstance(other, Point):
            return False

        return self.x == other.x and self.y == other.y

    def __str__(self):
        """Return a readable string representation of the point."""
        return f"Point({self.x}, {self.y})"

    def distance(self, other):
        """Return the Euclidean distance to another point."""
        return math.sqrt(
            (other.x - self.x) ** 2
            + (other.y - self.y) ** 2
        )


class Vector(Point):
    """Represent a two-dimensional vector."""

    def __str__(self):
        """Override Point's string representation."""
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        """Add two vectors and return a new Vector."""
        return Vector(
            self.x + other.x,
            self.y + other.y,
        )


if __name__ == "__main__":
    # Create Point objects
    point1 = Point(1, 2)
    point2 = Point(1, 2)
    point3 = Point(4, 6)

    # Demonstrate string representation
    print(point1)
    print(point3)

    # Demonstrate equality
    print(f"point1 == point2: {point1 == point2}")
    print(f"point1 == point3: {point1 == point3}")

    # Demonstrate Euclidean distance
    print(
        f"Distance from point1 to point3: "
        f"{point1.distance(point3)}"
    )

    # Create Vector objects
    vector1 = Vector(2, 3)
    vector2 = Vector(4, 5)

    # Demonstrate the overridden Vector string representation
    print(vector1)
    print(vector2)

    # Demonstrate vector addition
    vector3 = vector1 + vector2
    print(f"{vector1} + {vector2} = {vector3}")

    # Vector inherits Point's equality and distance methods
    print(f"vector1 == Vector(2, 3): {vector1 == Vector(2, 3)}")
    print(
        f"Distance from vector1 to vector2: "
        f"{vector1.distance(vector2)}"
    )