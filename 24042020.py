# Problem Wk 20/04: Stupid Addition

# Given 2 parameters, if:
#   both are strings, then add them as if they were integers
# 	if both are integers, then concatenate them
# 	if they have different data types then return None

# Examples:
#   if param1=1, param2=2, then concatenate them to give the result="12"
# 	if param1="1", param2="2", then add them as integers to give the result=3
# 	if param1="1", param2=2, then these have different datatypes and the result=None


# Extension:

# write a function to do this.


def stupid_addition(p1, p2):

    if type(p1) == str and type(p2) == str: 
        return int(p1) + int(p2)

    elif type(p1) == int and type(p2) == int: 
        return str(p1) + str(p2)

    else:
        return None

if __name__ == '__main__':

    print('String addition:', stupid_addition('1','2'))
    print('Int addition:',stupid_addition(1,2))
    print('Mixed addition:', stupid_addition('1',2))
