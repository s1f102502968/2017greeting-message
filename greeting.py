
from datetime import datetime

def greet():
    hour = datetime.now().hour
    if hour <= 11:
        message = 'Good morning'
        message = ',' + name + '-san!
        print(message)
    elif hour <= 17:
        message = 'Hello'
        message = ',' + name + '-san!
        print(message)
    else:
        message = 'Good evening'
        message = ',' + name + '-san!
        print(message)



greet('Inoue')