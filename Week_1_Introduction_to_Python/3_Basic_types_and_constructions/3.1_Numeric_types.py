#-----------------------------------------------------------------------
# numeric types of variables
#-----------------------------------------------------------------------

#
# type int
#
print("Type (int)")

num = 1
print(num)

num = 1000000
print(num)

num = 1_000_000      # more readable
print(num)

num = 1_0_0_0_0_0_0  # the same result
print(num)

num = 1000**1000     # long arithmetics
print(num)
print(type(num))


#
# type float
#
print("\nType (float)")

num = 1.2
print(num)

num = 0.0
print(num)

num = 1000000.0002
print(num)

num = 1_000_000.0_002  # the same
print(num)

num = 1.2e2
print(num)


#
# Convertations of types
#
print("\nConvertations of types")

num = 150.2
print(num, type(num))

num = int(num)
print(num, type(num))

num = float(num)
print(num, type(num))

num = int(100.9)  # the fractional part is discarded
print(num)


#
# type complex
#
print("\nType (complex)")

num = 14 + 1j

print(num, type(num))
print(num.real)
print(num.imag)


#
# Arithmetic operations
#
print("\nArithmetic operations")

print(1 + 2)
print(1 + 2.0)  # float
print(1.0 - 2)
print(9 / 3)    # float
print(10 // 3)  # integer division
print(10 % 3)   # remainder of the division



#
# Bitwise operations
#
print("\nBitwise operations")

x = 4  # 00000100
y = 3  # 00000011

print("x =", x, ", ",
      "y =", y)
print("Побитовое или:", x | y)             # 00000111 = 7
print("Побитовое исключающее или:", x ^ y)
print("Побитовое и:", x & y)               # 00000000 = 0
print("Битовый сдвиг влево:", x << 3)      # 00100000 = 32
print("Битовый сдвиг вправо:", x >> 1)     # 00000010 = 2
print("Инверсия битов:", ~x)               # 11111011 ?


#
# Multiple assignment
#
print("\nMultiple assignment")

a, b = 100, 200
print(a, b)

a, b = b, a
print(a, b)

#
x = y = 0
x += 1

print(x)
print(y)

# difference between mutable and immutable types!
x = y = []
x.append(1)
x.append(2)

print(x)
print(y)


#
# decimal - calculations with a given precision
#
print("\ndecimal - calculations with a given precision")

from decimal import Decimal

print( Decimal('0.23') )
print( Decimal('0.23000') )

print(0.2 + 0.2 + 0.2 - 0.4)
print(Decimal('0.2')+Decimal('0.2')+Decimal('0.2')-Decimal('0.4'))

# precision 6 decimal places
import decimal
decimal.getcontext().prec=6
b = Decimal(5)/Decimal(13)
print('b = ', b)  # b = 0.384615


#
# module fractions to work with rational numbers
#
print("\nmodule fractions to work with rational numbers")
       
from fractions import Fraction

print( Fraction(5, 6)   )  # 5/6
print( Fraction(8, 12)  )  # 2/3
print( Fraction('-1.5') )  # -3/2
print( Fraction('3.7') + Fraction('5.2') )  # 89/10


















