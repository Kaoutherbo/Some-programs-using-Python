myName= 'Kaouther'
myName="Kaouther"

# in string paragraph which contain ' must be inside "" or using '\'
man = "JK's songs are so nice"
man = 'JK \'s songs are so nice '

GOLDEN = 'The album solo of Jung kook'
print(GOLDEN[23])
print(GOLDEN[18:27]) # print The string 'Jung kook' which is from 18 position to 27 position 
print(GOLDEN[2:-1]) 

# concatination of strings
GOAT1 = 'Leo'
GOAT2 = ' Messi'
print(GOAT1+GOAT2)
# upper method to transform the string to uppercase
GOAT2=GOAT2.upper()
print(GOAT2)
# using split method 
clubs = "barcelona , psg , inter miami"
print(clubs.split(","))

# calcuate the lengh of string

print(len(GOAT1))