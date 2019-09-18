# Python Programming - Truzz Blogg
# Find the user and domain name in an email

# Method 1:
user_input = str(input("Enter your email: ")).strip()
print("Your original email is: {}".format(user_input))
user_name = user_input[:user_input.index("@")]
domain_name = user_input[user_input.index("@") + 1 :]
print("Domain Info: ")
print("Your user name is: {}  |  Your email provider is: {} ".format(user_name, domain_name))


# Method 2 - Using Partition ():
a = "learningpython@youtubemail.com"
parts = a.partition('@')
print(parts)

print("Your user name is: {}".format(parts[0]))
print("Your domain name is: {}".format(parts[2]))


# Method 3 - Using Split ():
b = str(input("Enter your email: "))
parts2 = b.split("@")
print("Resultado del split(): ", parts2)

print("Your USERNAME is: {}".format(parts2[0]))
print("Your DOMAIN_NAME is: {}".format(parts2[1]))