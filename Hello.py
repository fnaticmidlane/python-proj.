from math import sqrt
class Point:

    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y

    def __str__ (self):
        return "({}, {})".format(self.x, self.y)

    def distance_from_origin(self):
        d= sqrt(self.x ** 2 + self.y ** 2)
        return d

    def __eq__ (self,p ):
        return self.x == p.x and self.y == p.y
        
 

  #  def __add__(self,p , q):
  #       return "({} , {})". format(self.x + self.q, self.y + self.q)


# p = Point()
# print("p.x = {}, p.y = {}".format(p.x, p.y))

p = Point(x = 2, y = 4)
print("p.x = {}, p.y = {}".format(p.x, p.y))

q = Point(x = 2, y = 4)
print("q.x = {}, q.y = {}".format(p.x, p.y))


print("p = {}".format(p))
print("q = {}".format(q))
print(p.distance_from_origin())
print (p == q)

# print (("{} + {}").format(self.x + self.q, self.y + self.q))



