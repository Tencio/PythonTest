#Decimal manages numbers and keeps them exactly as they are, without dropping or changing any decimal, it is most likely used for economic or bank's software
import decimal

money = decimal.Decimal(1000.99)

print(money)

