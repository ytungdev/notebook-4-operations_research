'''

## Input format


#### Equation

Max 
    P - 3x - 5y + 0a + 0b + 0c = 0
s.t. 
    x     + a = 4 
    2y    + b = 12
    3x+2y + c = 18

    x,y,a,b,c >= 0

#### Tableau

| x   | y   | a   | b   | c   | P   | value | R   |
| :-- | :-- | :-- | :-- | :-- | --- | :---- | :-- |
| 1   | 0   | 1   | 0   | 0   | 0   | 4     | R_1 |
| 0   | 2   | 0   | 1   | 0   | 0   | 12    | R_2 |
| 3   | 2   | 0   | 0   | 1   | 0   | 18    | R_3 |
| -3  | -5  | 0   | 0   | 0   | 1   | 0     | R_4 |


#### Input

var = [x,y,a,b,c,P,val]
tbl = [
    [1,0,1,0,0,0,4],
    [0,2,0,1,0,0,12],
    [3,2,0,0,1,0,18],
    [-3,-5,0,0,0,1,0]
]

OR

var = [x,y,P,val]
tbl = [
    [1,0,0,4],
    [0,2,0,12],
    [3,2,0,18],
    [-3,-5,1,0]
]
'''

class Simplex:

    def __init__(self, tbl) -> None:
        self.tbl = tbl
        self.theta = [0 for i in tbl[:-1]]
        self.pivot_c = None
        self.pivot_r = None
        self.final_tbl = None
        self.result = (None, None, None)

    def find_pivot_c(self):
        max_c = 0
        for i in range(len(self.tbl[-1])):
            if self.tbl[-1][i] >= 0:
                continue
            else:
                if self.tbl[-1][i] <= self.tbl[-1][max_c]:
                    max_c = i
        self.pivot_c = max_c
        return max_c

    def find_pivot_r(self):
        for i in range(len(self.tbl[:-1])):
            if self.tbl[i][self.pivot_c] == 0:
                self.theta[i] = float('inf')
            else:
                self.theta[i] = float(self.tbl[i][-1]) / self.tbl[i][self.pivot_c]
        self.pivot_r = self.theta.index(min(self.theta))
        return self.pivot_r
    
    def row_operation(self):
        
        pivot_e = self.tbl[self.pivot_r][self.pivot_c]
        
        # R_pivot -> R_pivot / pivot_element
        self.tbl[self.pivot_r] = list(map(lambda x:x/pivot_e, self.tbl[self.pivot_r]))
                    
        # R_n -> R_n - i * R_pivot
        for i in range(len(self.tbl)):
            if i == self.pivot_r:
                continue
            if self.tbl[i][self.pivot_c] == 0:
                continue
            multi = self.tbl[i][self.pivot_c]
            for j in range(len(self.tbl[i])):
                self.tbl[i][j] = self.tbl[i][j] - multi * self.tbl[self.pivot_r][j]
        


    def solve(self)->None:
        while min(self.tbl[-1][0:2]) < 0:
            self.find_pivot_c()
            self.find_pivot_r()
            self.row_operation()
        
        final_tbl = []
        for i in range(len(self.tbl)):
            final_tbl.append([self.tbl[i][0],self.tbl[i][1],self.tbl[i][-2],self.tbl[i][-1]])

        self.final_tbl = final_tbl

        x,y,P = -1,-1,-1
        for r in final_tbl:
            # find x
            if r[0] == 1 and r[1] == 0:
                x = r[-1]

            # find y
            if r[0] == 0 and r[1] == 1:
                y = r[-1]

            # find P
            if r[0] == 0 and r[1] == 0 and r[2] == 1:
                P = r[-1]

        print('Initial tableau :')
        print(*self.tbl, sep='\n')

        print('Final tableau :')
        print(*self.final_tbl, sep='\n')

        print(f'P is maximiseed at {P} when x={x} and y={y}')
        result = (P,x,y)
        self.result = result
        return result

if __name__ == '__main__':
    
    var1 = ['x','y','a','b','c','P','val']
    tbl1 = [
        [1,0,1,0,0,0,4],
        [0,2,0,1,0,0,12],
        [3,2,0,0,1,0,18],
        [-3,-5,0,0,0,1,0]
    ]

    var2 = ['x','y','P','val']
    tbl2 = [
        [1,1.5,0,750],
        [2,3,0,1500],
        [2,1,0,1000],
        [-50,-40,1,0]
    ]
    s = Simplex(tbl2)
    s.solve()
