# Approximate Equivalent Resistor


### Brute force 
Time complexity: 2^k^n


## Simplified problem: Only one resistor type 
How well can we do when k=1?

### Brute force: 
2^n, since n-1 operations needed, and 2 possible operations (+ and //)


### Stern-Brocot tree & Calkin-Wilf tree:

Divide the target resistance r_t by the value of the one resistor r_0

Find the position of the closest value to r_t/r_0 within the first n levels of the Stern-Brocot tree 

Find the path to this value in the Calkin-Wilf tree



Can structure result as a binary tree!









