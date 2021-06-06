"""Be posi?ve! Create a func, on to sum up all positive argument inputs. Input 
ranges from 0 to N,where N can be any positive number"""
def positive_sum(*nums):
    return sum([num for num in nums if num>0])
print(positive_sum(-1,2,-3,4,5))