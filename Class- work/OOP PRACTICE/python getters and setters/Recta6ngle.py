
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self) -> float:
        self._width
        return self._width

    @property
    def height(self) -> float:
        self._height
        return self._height

    @width.setter
    def width(self,new_width):
        if new_width > 0:
            self._width = new_width

        else:
            print("width must 5be greater than 0")

    @height.setter
    def height(self,new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("height must 5be greater than 0")


rectangle = Rectangle(4, 3)
print(rectangle.width)
print(rectangle.height)

