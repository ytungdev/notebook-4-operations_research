# Linear Programming

- Simple and powerful
- Address a general management problem
    - Allocate **limited resources** among **competing activities** in an **optimal** way

## Linear Programming formulation

- Decision variables
- Objective function
- Constraints

## Examplee

### Background 

- A manufacturer produce 2 product
    - product 1 : use material 1 and 3
    - product 2 : use material 2 and 3
- It owns 3 plants
    - A : material 1
    - B : material 2
    - C : material 3


|                  | Production time per patch (hrs) |           | Production time available (hrs) |
| ---------------- | ------------------------------- | --------- | ------------------------------- |
|                  | Product 1                       | Product 2 |                                 |
| Plant 1          | 1                               | 0         | 4                               |
| Plant 2          | 0                               | 2         | 12                              |
| Plant 3          | 3                               | 2         | 18                              |
| Profit per batch | $3,000                          | $5,000    |                                 |

### Formulation

- Decision variables
    - x : # of batches of Product 1
    - y : # of batches of Product 2
- Objective function
    - Max {3000x + 5000y}
- Constraints
    - Production time
        -     x <= 4  (Plant 1)
        -    2y <= 12 (Plant 2)
        - 3x+2y <= 18 (Plant 3)
    - Nonnegativity
        -     x >= 0
        -     y >= 0

### Graphical Solution

### Simplex algorithm

Start with any one of the solution within feasible region, then change one variable one at a time to optimise objective function. Each iteration select changing varialbe according to greatest rate of change in terms of objective function.

```
Max 
    3x + 5y

s.t. 
    x       <= 4 
    2y      <= 12
    3x+2y   <= 18
    x,y     >= 0
```

1) Adding slack variable to change inequalities to equalities and construct initial tableau
```
Max 
    P - 3x - 5y + 0a + 0b + 0c = 0
s.t. 
    x     + a = 4 
    2y    + b = 12
    3x+2y + c = 18

    x,y,a,b,c >= 0

```
| var | x   | y   | a   | b   | c   | value | R   |
| :-- | :-- | :-- | :-- | :-- | :-- | :---- | :-- |
| a   | 1   | 0   | 1   | 0   | 0   | 4     | R_1 |
| b   | 0   | 2   | 0   | 1   | 0   | 12    | R_2 |
| c   | 3   | 2   | 0   | 0   | 1   | 18    | R_3 |
| P   | -3  | -5  | 0   | 0   | 0   | 0     | R_4 |

2) Find the most negative value in objective function (y) as pivot column and calcualte theta (value/pivot col)

| var | x   | y   | a   | b   | c   | value | R   | theta     |
| :-- | :-- | :-- | :-- | :-- | :-- | :---- | :-- | --------- |
| a   | 1   | 0   | 1   | 0   | 0   | 4     | R_1 | 4/0 = inf |
| b   | 0   | 2   | 0   | 1   | 0   | 12    | R_2 | 12/2=6    |
| c   | 3   | 2   | 0   | 0   | 1   | 18    | R_3 | 18/2=9    |
| P   | -3  | -5  | 0   | 0   | 0   | 0     | R_4 | 0/-5=0    |
