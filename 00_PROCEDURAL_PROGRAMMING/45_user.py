

user_0 = {
    'username' : 'LGaming420',
    'first' : 'Lord',
    'last' : 'Farquad'
}

# for item in user_0:
#    print(item) #key...
#    print("val:", user_0[item])
    
print(user_0.items()) # [{'a'}, {'b'}, {'c', 'd'}, ()]
for key, val in user_0.items():
    print("key:", key)
    print("val:", val)
    
for key in user_0.keys():
    print("key:", key)
    
for val in user_0.values():
    print("val:", val)