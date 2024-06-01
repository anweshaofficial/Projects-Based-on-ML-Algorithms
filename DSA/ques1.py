# Vallid Parenthesis 

#%%

#Can you create a function that takes a string containing just the characters '(', ')', '{', '}', '[' and ']', and determines if the string is valid? The string is valid if every opening bracket has a corresponding closing bracket of the same type, and the brackets are correctly nested.

#%%

def parastack(s):

    stack = [] 
    mapping = { ')':'(', '}':'{', ']':'['}

    for char in s:
        if char in mapping:
            top_ele = stack.pop() if stack else '#'

            if mapping[char] != top_ele:
                return False
            
        else:
            stack.append(char)
    return not stack

s = '('
print(parastack(s))

#%%
