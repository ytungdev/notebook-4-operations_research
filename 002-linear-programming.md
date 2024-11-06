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