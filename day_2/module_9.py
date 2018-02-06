'''
Created on 06/02/2018

@author: asus
'''

if __name__ == '__main__':
    
    ### insert text
    text = input('Insert text: ')
    
    dict = {}
    for char_1 in text:
        
        #print(char_1)
        if (not char_1.isalpha()): continue ## go to the begin of the loop
        if char_1 in dict:
            dict[char_1] += 1
        else:
            dict[char_1] = 1
            
    for key in sorted(dict.keys()):   
        print(key, dict[key])