import argparse

#We create parser to instanciate the argparse ArgumentParser method

parser = argparse.ArgumentParser()

parser.add_argument('Param', help = 'Prints the string you use here')
parser.add_argument('Parameter', help = 'Prints the string you use here')

args = parser.parse_args()

print(args)

#We add arguments so it is like a self operating program without user being involved, so you "send" variables fo scripting