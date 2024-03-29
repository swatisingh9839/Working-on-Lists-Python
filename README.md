# Working-on-Lists-Python
Write a function smooth(a, n) that takes in a list of integers a and a non-negative integer n. The function should create a return a new list r where ri = (ai-n + ai-n-1 + ai-n-2 + ... + ai-1 + ai + ai+1 + ... + ai+n-1 + ai+n) / (2*n + 1)  that is, the mean value of ai and its 2n surrounding numbers.  If n = 1 the result will be as in the exercise (smooth(a)) above, at least for the inner elements.  For the points close to the corners with very low indexes and very high indexes the interval [i-n:i+n] might be outside the range of the list. In that case, we can choose one of two strategies(You need to do both of them to pass this assignment):  

Same breadth (2n+1) should be used in the smoothing operation, but in the elements where index goes below 0 the first value (that is, the one at index 0) should be used, and for elements where the index is too big the last value should be used. We can look at it as extending the lists in both directions with the corner elements.

Only elements that exist in the array should be used, so the mean value is created using fewer elements. Example: The code
