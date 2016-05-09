exec("print('exec can compile a code')")

# This won't work
# list_str = "[5,6,2,1,6]"
# list_str = exec(list_str)
# print(list_str)

# This is interesting cuz we never define list_str explicitly
exec("list_str = [1,5,7,8,2]")
print(list_str)

# even awsome, function can be executed
exec("def test(): print('oooo snap!!!')")
test()

exec("""
def test2():
    print('lets see if multi line works....')
""")

test2()