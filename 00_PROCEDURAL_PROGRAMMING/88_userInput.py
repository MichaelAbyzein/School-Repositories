
def build_profile(first, last, **info):
    info['fullname'] = f"{first.title()} {last.title()}"
    return info
    
user = build_profile('albert', 'einstein', location='nebraska', field='calculus')
print(user)