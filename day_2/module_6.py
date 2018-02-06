'''
Created on 06/02/2018

@author: asus
'''

def fibonacci(value):
    if (value < 2): return 1
    
    value1 = 0
    value2 = 1
    
    for i in range(2, value):
        return_value = value1 + value2
        print('i {} value1 {} value2 {} soma: {}'.format(i, value1, value2, return_value))
        value1 = value2
        value2 = return_value
    return return_value
        
if __name__ == '__main__':
    
    print(fibonacci(10))