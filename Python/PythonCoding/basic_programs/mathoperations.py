from mypack.basicshapes import areaofsquare, perimeterofsquare, areaofrect, perimeterofrect
from mypack.circle import areaofcircle, perimeterofcircle

radius = int(input('Enter radius : '))

print('Area : ',areaofcircle(rad = radius))
print('Perimeter : ',perimeterofcircle(rad = radius))

si = int(input('Enter side of square : '))
print('Area : ',areaofsquare(side = si))
print('Perimeter : ',perimeterofsquare(side = si))

len = int(input('Enter length of rect : '))
bre = int(input('Enter breadth of rect : '))
print('Area : ',areaofrect(l = len, b = bre))
print('Perimeter : ',perimeterofrect(l = len, b = bre))