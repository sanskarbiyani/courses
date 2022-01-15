import re
x = 'My 2 favourite numbers are 19 and 42'
y = re.findall('[0-9]+',x) #find  1 or more digits
print(y)

y = re.findall('[AEIOU]+',x) #find ! or more letters mentioned
print(y)

x = 'From: Using ths: characters'
y = re.findall('^F.+:',x) #greedy matching(gives the largest)
print(y)

x = 'From: Using ths: characters'
y = re.findall('^F.+?:',x) #non-greedy matching(gives the smallest)
print(y)

#'\S+@\S+' --> one or more non-blank characters folowed by @ and followed by one or more non-blank characters

#'^From (\S+@\S+)' --> match the strong string but extract only the contents inside the paranthesis

#'@([^ ]*)' --> find me a string with @ and extract 0 or more non-blank characters

#'^From .*@([^ ]*)'

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+?@\S+',data) #find  1 or more digits
print(y)
