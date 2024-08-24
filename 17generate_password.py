import random
alphabet = 'a,b,c,d,e,f,g ,'
alphabet_upper = alphabet.upper()
number = '1,2,3,4,5,6,7,8'
all_combine = alphabet + alphabet_upper+number
all_combine_to_list = all_combine.split(",")
# print(all_combine_to_list)

random1 = random.choice(all_combine_to_list)
random2 = random.choice(all_combine_to_list)
random3 = random.choice(all_combine_to_list)
random4 = random.choice(all_combine_to_list)
random5 = random.choice(all_combine_to_list)
random6 = random.choice(all_combine_to_list)
random7 = random.choice(all_combine_to_list)

password = random1 + random2 + random3 + random4 + random5 + random6 + random7
print (f"The password is {password}")