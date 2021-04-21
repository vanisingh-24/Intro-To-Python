##Iterate through all keys

statesAndCapitals = {
                     'Gujarat' : 'Gandhinagar',
                     'Maharashtra' : 'Mumbai',
                     'Rajasthan' : 'Jaipur',
                     'Bihar' : 'Patna'
                    }

for state in statesAndCapitals:
    print(state)

# iterate through all keys in a dictionary in a specific order

from collection import OrderedDict

statesAndCapitals = OrderedDict([
                                 ('Gujarat', 'Gandhinagar'),
                                 ('Maharashtra', 'Mumbai'),
                                 ('Rajasthan', 'Jaipur'),
                                 ('Bihar', 'Patna')
                                ])

for state in statesAndCapitals:
    print(state)  

# Iterate through all values

statesAndCapitals = {
                     'Gujarat' : 'Gandhinagar',
                     'Maharashtra' : 'Mumbai',
                     'Rajasthan' : 'Jaipur',
                     'Bihar' : 'Patna'
                    }

for capital in statesAndCapitals.values():
    print(capital)

# Iterate through all key, value pairs

statesAndCapitals = {
                     'Gujarat' : 'Gandhinagar',
                     'Maharashtra' : 'Mumbai',
                     'Rajasthan' : 'Jaipur',
                     'Bihar' : 'Patna'
                    }

for state, capital in statesAndCapitals.items():
    print(state, ":", capital)



