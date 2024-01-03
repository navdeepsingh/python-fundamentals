def division(num):
    try:
        num = 3.14 / num
    except ZeroDivisionError:
        print('Zero Division Error')    
    except Exception as e:
        print('ExceptionError:', e)    

# Path: exceptions.py
division(0)        
print('This is the end of the file')