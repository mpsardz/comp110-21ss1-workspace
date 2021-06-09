"""Examples of object-oriented programming concepts."""

# class name 
class Point: 
    """Represent a 2d Point."""

    # Define attributes (related variables)
    x: float = 0.0
    y: float = 0.0

    # Define our own constructor 
    def __init__(self, x: float, y: float): 
        """Construct a point by giving a specific x and y."""
        #update our attributes to be assigned the value of parameters
        self.x = x
        self.y = y

    # define methods to give each object of your class certain caabilities
    def translate_x(self, dx: float) -> None:
        """TRanslate the point in the x direction."""
        # mutate the object it is called on
        self.x += dx
        return None 

    def reset_y(self) -> float:
        """Return the current value of y and then reset it."""
        result: float = self.y
        self.y = 0.0
        return result

# declare a new Point object
# to give it an initial value, we need to call the constructor
a: Point = Point(2.0, 3.0)
b: Point = Point(2.0, -1.0)
# method call! we provide the specific object being used 
# and the method name with arugments
a.translate_x(-6.0)
b.translate_x(1.0)
b.translate_x(4.0)

a.reset_y()

c: float = a.reset_y()
print(c)
print(a.y)






# define a new Point object
# to give it an initial value, we need to call the Constructor
a: Point = Point(2.0, 3.0)
#access attributes using the dot operator 

# ex. b: str = "abc"
# ex. c: int = 1 + 2 + 4
print(f"The y value is {a.y}")
# you can also directly update attributes using the dot operator 
a.x = 20.0

b: Point = Point()
# b.x = 2.0
#b.y = -1.0
