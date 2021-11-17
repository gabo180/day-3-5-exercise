# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lowercase = name1.lower()
name2_lowercase = name2.lower()

name_count_t = name1_lowercase.count("t") + name2_lowercase.count("t")
name_count_r = name1_lowercase.count("r") + name2_lowercase.count("r")
name_count_u = name1_lowercase.count("u") + name2_lowercase.count("u")
name_count_e = name1_lowercase.count("e") + name2_lowercase.count("e")
name_true_count = name_count_t + name_count_r + name_count_u + name_count_e
name_count_l = name1_lowercase.count("l") + name2_lowercase.count("l")
name_count_o = name1_lowercase.count("o") + name2_lowercase.count("o")
name_count_v = name1_lowercase.count("v") + name2_lowercase.count("v")
name_love_count = name_count_l + name_count_o + name_count_v + name_count_e

love_score = int(f'{name_true_count}{name_love_count}')

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")


