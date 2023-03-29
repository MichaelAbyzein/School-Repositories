#Nesting Dictionary in dictionary

users = {
    'gustav54': {
        'first' : "gustav",
        'last' : "sindler",
        'location': "sweden"
    },
    'sanders co' : {
        'first' : "ronald",
        'last' : "sanders",
        'location' : "ohio"
    }

}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    fullname = f"{user_info['first'].title()} {user_info['last'].title()}"
    location = user_info['location'].title()
    print(f"\tFullname:{fullname}")
    print(f"\tLocation:{location}")