#!/usr/bin/python3

class square():
    
    side = 0

    
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.side * self.side

    def PermiterOfMySquare(self):
        return (self.side * 4)

    def __str__(self):
        return "{}".format(self.side)

if __name__ == "__main__":

    s = square(side=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())