# create a class 2-d vector and use it to create a class 3-d vector
class vector2d:
    x=5
    y=4
class vector3d(vector2d):
    z=7

v=vector3d()
print(f"{v.x} and {v.y} and {v.z}")