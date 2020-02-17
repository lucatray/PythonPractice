class Zillion:

    def __init__(self, string):
        self.digits = []
        if len(string) == 0:
            raise RuntimeError
        else:
            length = 0
            while length < len(string):
                if string[length] >= '0' and string[length] <= '9':
                    self.digits.append(string[length])
                    length = length + 1
                elif string[length] == ' ' or string[length] == ',':
                    pass
                else:
                    raise RuntimeError





    def increment(self):
        b = len(self.digits) - 1
        while b >= 0:
            if self.digits[b] == '9':
                self.digits[b] = '0'
            elif b == 0:
                if self.digits[0] == '9':
                    self.digits[0] = '1'
                    self.digits.append('0')
                else:
                    self.digits[0] = self.digits[0] + 1


            else:
                self.digits[b] = self.digits[b] + 1
                break

            b = b - 1



    def isZero(self):
        d = 0
        while d <= len(self.digits) - 1:
            if self.digits[d] == 0:
                d += 1
            else:
                return True

        return False




    def toString(self):
        return str(self.digits)



try:
  z = Zillion('')
except RuntimeError:
  print('Empty string')

# It must print 'Empty string' without apostrophes. 2 points.

try:
  z = Zillion(' , ')
except RuntimeError:
  print('No digits in the string')

# It must print 'No digits in the string' without apostrophes. 2 points.

try:
  z = Zillion('1+0')
except RuntimeError:
  print('Non-digit in the string')

# It must print 'Non-digit in the string' without apostrophes. 2 points.

try:
  z = Zillion('0')
except RuntimeError:
  print('This must not be printed')

#  It must print nothing. 2 points.

print(z.isZero())    #  It must print True. 2 points.

try:
  z = Zillion('000000000')
except RuntimeError:
  print('This must not be printed')

#  It must print nothing. 2 points.

print(z.isZero())    #  It must print True. 2 points.

try:
  z = Zillion('000 000 000')
except RuntimeError:
  print('This must not be printed')

#  It must print nothing. 2 points.

print(z.isZero())    #  It must print True. 2 points.

try:
  z = Zillion('997')
except RuntimeError:
  print('This must not be printed')

#  It must print nothing.  2 points.

print(z.isZero())    #  It must print False. 2 points.

print(z.toString())  #  It must print 997. 2 points.

z.increment()

print(z.toString())  #  It must print 998. 2 points.

z.increment()

print(z.toString())  #  It must print 999. 2 points.

z.increment()

print(z.toString())  #  It must print 1000. 2 points.

try:
  z = Zillion('0 9,9 9')
except:
  print('This must not be printed')

#  It must print nothing.  3 points.

z.increment()
print(z.toString())  #  It must print 1000. 2 points.

