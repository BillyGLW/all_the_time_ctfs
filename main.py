#     A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
#    +----------------------------------------------------
# A | A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# B | B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
# C | C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
# D | D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
# E | E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
# F | F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
# G | G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
# H | H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
# I | I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
# J | J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
# K | K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
# L | L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
# M | M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
# N | N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
# O | O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
# P | P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
# Q | Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
# R | R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
# S | S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
# T | T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
# U | U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
# V | V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
# W | W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
# X | X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
# Y | Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
# Z | Z A B C D E F G H I J K L M N O P Q R S T U V W X Y
import string

to_decode = 'UFJKXQZQUNB'
key = 'SOLVECRYPTO'

count = 0
x = 0
flag = []
while (count <= len(to_decode) -1):
	if string.ascii_letters[x] == key[count:count+1]:
		_temp = string.ascii_letters[x:len(string.ascii_letters)] + string.ascii_letters[26:x]
		x = 0
		print(_temp)
		for _y in range(len(_temp)):
			if _temp[_y] == to_decode[count:count+1]:
				print(string.ascii_letters[_y+26])
				flag += string.ascii_letters[_y+26]
				count = count + 1
				break
	x = x+1

print("**** FLAG: %s ****" % (''.join(flag)))

