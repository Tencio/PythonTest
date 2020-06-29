import math
class Calculo():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

    def __sub__(self, otro_punto):
        delta_x = self.x -otro_punto.x 
        delta_y = self.y - otro_punto.y
        return math.sqrt(delta_x**2 + delta_y**2)

p1 = Calculo(22,30)
p2 = Calculo(25,35)      

print(p1 - p2)       
    
