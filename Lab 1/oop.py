from numpy import true_divide

def gcd(f,g):
    r=f%g
    while(r!=0):
        f=g
        g=r
        r=f%g
    return g
class Number:
    """
    Basic class for numbers. Rational and Integer will based on it.
    """

    __slots__ = ()

    def floor(self):
        raise NotImplementedError('%s needs .floor() method' %
            (self.__class__.__name__))

    def ceiling(self):
        raise NotImplementedError('%s needs .ceiling() method' %
            (self.__class__.__name__))

    def __add__(self, other):
        raise NotImplementedError('%s needs .__add__() method' %
            (self.__class__.__name__))

    def __sub__(self, other):
        raise NotImplementedError('%s needs .__sub__() method' %
            (self.__class__.__name__))

    def __mul__(self, other):
        raise NotImplementedError('%s needs .__mul__() method' %
            (self.__class__.__name__))

    def __truediv__(self, other):
        raise NotImplementedError('%s needs .__truediv__() method' %
            (self.__class__.__name__))

class Rational(Number):
    # 你不需要关心的部分
    
    p = int()
    q = int()
    def __repr__(self):
        if self.p!=0:
            return str(self.p) + " / " + str(self.q)
        else:
            return str(0)

    __str__ = __repr__

    # 下面是你需要关心的部分
    def __init__(self, p, q):
        if q==0:
            raise  ValueError("Oops,denominator must not be 0!")
        self.p = p
        self.q = q

    def _simplify(self):
        # 请在此处完成你的代码，使得这个函数可以完成约分
        a=gcd(self.p,self.q)
        self.q=self.q//a
        self.p=self.p//a
        return self

    def __add__(self, other):
        return Rational(self.p * other.q + self.q * other.p, self.q * other.q)._simplify()
    
    def __sub__(self, other):
        return Rational(self.p * other.q - self.q * other.p, self.q * other.q)._simplify()
    
    def __mul__(self, other):
        return Rational(self.p*other.p,self.q*other.q)._simplify()

    def __truediv__(self, other):
        return Rational(self.p*other.q,self.q*other.p)._simplify()
    
    def __eq__(self, other):
        return  self.q*other.p==self.p*other.q

    def __lt__(self,other):
        return self.p/self.q < other.p/other.q
    
    def __gt__(self,other):
        return self.p/self.q > other.p/other.q

    def __le__(self,other):
        return self.p/self.q <= other.p/other.q
    
        
        
class Integer(Rational):
    p = int()
    q = 1
    
    def __repr__(self):
        return str(self.p)

    __str__ = __repr__

    # 下面是你需要关心的部分
    def __init__(self, p):
        self.p = p
        self.q = 1

# a = Rational(1, 2)
# b = Rational(3, 4)
# c = Integer(3)
# print(a + b)
# print(a / b)
# d = Rational(0, 0)
# e = Rational(0,10)
# print(e)
# f = Rational(0, 1000)
# print(e == f)