# Remove empty tuples from a list

def remove(tuples):
  tuples = [t for t in tuples if t]
  return tuples

tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
          ('krishna', 'akbar', '45'), ('',''),()]
print(remove(tuples))

# OR

def remove(tuples):
  tuples = filter(None, tuples)
  return tuples

tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
          ('krishna', 'akbar', '45'), ('',''),()]
print(remove(tuples))