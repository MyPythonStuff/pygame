import pets

if(3<5):
    print('5 is greater than 3')

#range(0,5) and range(5) yield the same result
# substituting range(0,5) or range(5) will yield the same result
for x in range(5):
    print(x)
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
#Output: 2
fruits.count('tangerine')
#Output: 0
fruits.index('banana')
#Output: 3
fruits.index('banana', 4)  # Find next banana starting a position 4
#Output: 6
'orange' in fruits #checks to see if 'orange' is in fruits. will return True or False
#Output: True
fruits.reverse()
print(fruits)
#output: ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')
print(fruits)
#output: ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
print(fruits)
#output: ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
fruits.pop()
print(fruits)
#output: pear

myPet2 = pets.pets('dog', 'wahtever')
print(myPet2.getname())
myPet2.setname('scooby')
print(myPet2.getname())

myPet1 = pets.pets('cat', 'kitty')
print(myPet1.getname())
myPet1.setname('Mr.Meow')
print(myPet1.getname())