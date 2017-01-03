# See https://docs.python.org/2/library/turtle.html
from turtle import *

color('red', 'yellow')
pendown()
begin_fill()
for i in [0, 1]:
    forward(100)
    left(90)
    forward(200)
    left(90)
end_fill()

color('green', 'blue')
begin_fill()
dot(70)
end_fill()
done()
