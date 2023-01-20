def bisection(fun,a,b,tol):
   """
   Carries out the bisection to
   ascertain the roots of a function

   Inputs:
   fun   Function to calculate root for
   a     Left bracket
   b     Right bracket
   tol   Tolerance

   Outputs
   n     Number of iterations
   c     Root of function fun
   """
   # Evaluate f(a) and f(b)
   f_a = fun(a)
   f_b = fun(b)
   # Initialise counter
   n = 0 
   # Continue the bisection method
   c = (a + b)/2

   while abs(fun(c)) >= tol:
      if fun(c)*fun(a) > 0:
         a = c
      else:
         b = c
      c = (a + b)/2
      n+=1
      
   return n, c 



