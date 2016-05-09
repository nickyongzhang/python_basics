# The idea of eval is to evaluate an expression in the form of 
# a string and return the value. 

# Keep in mind, just like the pickle module we talked about, 
# eval has no security against malicious attacks. 
# Don't use eval if you cannot trust the source. 
list_str = "[1,5,7,8,2]"
list_str = eval(list_str)

print(list_str)
print(list_str[1])

# if we input 6>5 for the first print out it will be 6>5
# for the second print out it will be True
x = raw_input("code:")
print(x)
check_this_out = eval(raw_input("code:"))
print(check_this_out)