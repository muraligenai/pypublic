class FirstClass:
    x=1000;
    y=0;
 #   print('x :', x)

    def firstFun(self, a, b):
        x = a
        y = b
        z = x + y
        print('local x: ', x)
        print('local y: ', y)
        print ('z: ', z)

    def secFun(self, i, j):
        print('Class x: ', self.x)
        print('Class y: ', self.y)
    '''    
        self.x = i
        self.y = j
        z1 = self.x + self.y
        print('z1: ', z1)
    '''

class callClass:

    fc = FirstClass()
    print('x :', fc.x)
    print('y :', fc.y)

    fc.firstFun(2000, 3000)
    fc.secFun(10, 20)
