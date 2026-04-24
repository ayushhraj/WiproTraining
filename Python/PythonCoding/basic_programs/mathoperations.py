from mypack.basicshapes import area_of_square, perimeter_of_square, area_of_rect, perimeter_of_rect
from mypack.circle import area_of_circle, perimeter_of_circle

radius = int(input('Enter radius : '))

print('Area : ',area_of_circle(rad = radius))
print('Perimeter : ',perimeter_of_circle(rad = radius))

si = int(input('Enter side of square : '))
print('Area : ',area_of_square(side = si))
print('Perimeter : ',perimeter_of_square(side = si))

len = int(input('Enter length of rect : '))
bre = int(input('Enter breadth of rect : '))
print('Area : ',area_of_rect(l = len, b = bre))
print('Perimeter : ',perimeter_of_rect(l = len, b = bre))