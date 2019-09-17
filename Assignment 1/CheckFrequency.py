import re
def printWords(s): 

# split the string 
s = s.split(' ') 

# iterate in words of string 
for word in s: 

# if length is even 
if len(word)==1: 
print(word)  

oneWord = []
twoWord = []
threeWord = []


with open("data.txt", "r") as my_file:
  for line in my_file:
      str = line.split(' ')
      for word in str: 
      
       if len(word) == 1:
          oneWord.append(word)
       elif len(word) == 2:
          twoWord.append(word)
       elif len(word) == 3:
          threeWord.append(word)

  print ('one letter word: ', oneWord ,'\n\n')
  print('two letter word: ', twoWord ,'\n\n')
  print('three letter word: ', threeWord ,'\n\n')

  oneDuplicate = [False]*len(oneWord)
  twoDuplicate = [False]*len(twoWord)
  threeDuplicate = [False]*len(threeWord)

  print('One letter word: \n')
  for i in range(0,len(oneWord)):
    if(oneDuplicate.count(oneWord[i]) == 0):
      print(oneWord[i] , ': ' ,oneWord.count(oneWord[i]),end=' ,')
      oneDuplicate.append(oneWord[i])
  print('\n\n--------------------------')

  print('Two letter word: \n')
  for i in range(0,len(twoWord)):
    if(twoDuplicate.count(twoWord[i]) == 0):
      print(twoWord[i] , ': ' ,twoWord.count(twoWord[i]),end=' , ')
      twoDuplicate.append(twoWord[i])
  print('\n\n--------------------------')

  print('Three letter word:\n')
  for i in range(0,len(threeWord)):
    if(threeDuplicate.count(threeWord[i]) == 0):
      print(threeWord[i] , ': ' ,threeWord.count(threeWord[i]),end=' , ')
      threeDuplicate.append(threeWord[i])
  print('\n\n--------------------------')
