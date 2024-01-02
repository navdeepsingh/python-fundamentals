try:
    int('a')
except ValueError as e:
    print('ValueError:', e)    

# Path: exceptions.py
print('This is the end of the file')