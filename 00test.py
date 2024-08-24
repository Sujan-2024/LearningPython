import random 
alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,'
number = '1,2,3,4,5,6,7,8,9,10,11,12,'
alphabet_upper = alphabet.upper()
combine_letters = alphabet + number + alphabet_upper
combine_letters_to = combine_letters.split(",")
# print(combine_letters)
random1 = random.choice(combine_letters)
random2 = random.choice(combine_letters)
random3 = random.choice(combine_letters)
random4 = random.choice(combine_letters)
random5 = random.choice(combine_letters)
random6 = random.choice(combine_letters)
random7 = random.choice(combine_letters)

password = random1 + random2 + random3 + random4 + random5 + random6 + random7

print(f"The password is {password}")

