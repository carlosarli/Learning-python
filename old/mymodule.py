def areaTrianglerect(a, b, c):
    return a * b * c / max(a, b, c)
def basicGeometry(a, b, c, d = 0):
    if d == 0:
        print('The Area of your triangle is :', areaTrianglerect(a, b, c))
    else:
        print('the are of your parallelogram is', a * b)
__version__ = '0.1'
