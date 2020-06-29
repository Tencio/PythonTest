#Importin math to use sqrt function
import math

#Tuples are a list that cannot be changed or edited

Example = (1, 2, 3)

print(type(Example))

#Challenge, calculate the distance between two points on a cartesian plane using tuples

def Pitagoras(Point1, Point2):

    DeltaX = Point1[0] - Point2[0]
    DeltaY = Point1[1] - Point2[1]

    Pit1 = pow(DeltaX, 2)

    Pit2 = pow(DeltaY, 2)

    Result = math.sqrt(Pit1 + Pit2)

    print(Result)

#Passing the parameters as tuples
Pitagoras((25, 20), (10, 15))

