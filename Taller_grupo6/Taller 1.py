import time     # Python library for calculating running time

def function(x):
  """
  Given an input x, it returns the value of f(x), 
  where f is a polynomial function of degree 4. 
  """
  A = 1
  B = 30
  C = 15
  D = 34
  E = 540
  return -(A*(x**4)) + (B*(x**3)) + (C*(x**2)) + ( D * x) + E

def bisection(a,b):
    '''
    It receives an interval [a,b] and returns the value c, 
    for which function(c) equals aproximately 0. 
    Which is to say, the point (c,0) is a root of the function
    '''
    f_a = function(a)              # Compute f(a)
    f_b = function(b)              # Compute f(b)
    c = (b+a)/2                    # Find c (the middle value of the interval)
    f_c = function(c)              # Compute f(c)
    if f_a * f_b < 0:              # If f(a) and f(b)'s signs differ, the process can continue
      while abs(f_c) >= 0.0001:    # Execute the numeric method with a precisión of 0.0001
        c = (b+a)/2                # Update c (the middle value of the interval)
        f_c = function(c)          # Update f(c)
        if f_c * f_a < 0:          # If f(a) and f(c)'s signs differ, the interval is redefined as [a,c].
          b = c
        elif f_c * f_b < 0:        # If f(b) and f(c)'s signs differ, the interval is redefined as [c,b].
          a = c
        else:                      # If f(c) = 0, it means c is a root, so its value gets returned
          return c
      return c                     # When the c is within the tolerance range, it gets returned as the found root
    elif f_a * f_b > 0:            # If f(a) and f(b)'s signs are the same, it's not certain whether a root can be found
      return "Not certain"              
    else:
      if f_a  == 0:                # Si f(a) = 0, it means a is a root, so its value gets returned
        return a
      else:                        # If f(b) = 0, it means b is a root, so its value gets returned
        return b

a = 0                     # Lower bound for the interval
b = 1000                  # Upper bound for the interval

t_0  = time.time()        # Initial time
root = bisection(a,b)     # Calculate the root of function(x) between the interval [0,1000]  
t_1  = time.time()        # Final time

print("Given interval: [" + str(a) + ", " + str(b) + "]")
print("Found root:     x =", round(root,5))
print("Execution time:", round(t_1-t_0,8) , "sec")