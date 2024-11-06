'''
max
    P = 20a + 10b
s.t
    a + b <= 40
    4a + b <= 100
    a,b >= 0

    a   +   b   +   i   = 40
    4a  +   b   +   j   = 100
    -20a -10b   +   P   = 0

    
    
tableau
    [a, b, i, j, P, v]
'''

class Simplex:
    tbl = [
        [1,1,1,0,0,40],
        [4,1,0,1,0,100],
    ]

    obj = [-20,-10,0,0,1,0]

    theta = [0,0]

    def iter(self):
        if min(self.obj[:-1]) >= 0:
            return self.tbl
        
        # find pivot_c by finding most negative column in obj fx
        pivot_c = self.obj.index(min(self.obj))

        # find pivot_r by finding min non-negative theta
        for i in range(len(self.tbl)):
            self.theta[i] = self.tbl[i][-1] / self.tbl[i][pivot_c]

        pivot_r = self.theta.index(min(x for x in self.theta if x >= 0))

        # perform Gaussian-like elimination with pivot element pivot_v
        pivot_v = self.tbl[pivot_r][pivot_c]
        for i in range(len(self.tbl[pivot_r])):
            self.tbl[pivot_r][i] = self.tbl[pivot_r][i] / pivot_v

        print(self.tbl)


s = Simplex().iter()