'''
Created on 06/02/2018

@author: asus
'''

if __name__ == '__main__':
    
    text = input('Some text: ')
    
    dict = {}
    
    for word in text.split(): ## split by space
            ## other variant _.split('.'), _.split('\t')
       
        if word in dict: dict[word] += 1
        else: dict[word] = 1
        
    print(dict)