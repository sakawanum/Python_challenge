Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def f(x):
	"""
        xを2乗して出力する。
        :param x:int.
        :return :xを2乗する。
        """
	return x ** 2
　　　　print(x)
SyntaxError: invalid character in identifier
>>> def f(x):
	"""
        xを2乗して出力する。
        :param x:int.
        :return :xを2乗する。
        """
	return x ** 2
        print(x)
        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> def f(x):
	"""
        xを2乗して出力する。
        :param x:int.
        :return :xを2乗する。
        """
	return x ** 2
    print(x)
    
SyntaxError: unindent does not match any outer indentation level
>>> def f(x):
	"""
        xを2乗して出力する。
        :param x:int.
        :return :xを2乗する。
        """
	return x ** 2

>>> f(2)
4
>>> f(4)
16
>>> def mojiretu(string):
	"""
        受け取った文字列を出力する。
        :param :string.
        :return :文字列を返す。
        """
	return ("string")

>>> mojiretu(ggg)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    mojiretu(ggg)
NameError: name 'ggg' is not defined
>>> def mojiretu(string):
	"""
        受け取った文字列を出力する。
        :param :string.
        :return :文字列を返す。
        """
	print ("string")

	
>>> mojiretu(ggg)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    mojiretu(ggg)
NameError: name 'ggg' is not defined
>>> def mojiretu(string):
	"""
        受け取った文字列を出力する。
        :param :string.
        :return :文字列を返す。
        """
	return (string)

>>> mojiretu(kjk)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    mojiretu(kjk)
NameError: name 'kjk' is not defined
>>> def mojiretu(string):
	"""
        受け取った文字列を出力する。
        :param :string.
        :return :文字列を返す。
        """
	print("string")

	
>>> mojiretu(ggg)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    mojiretu(ggg)
NameError: name 'ggg' is not defined
>>> def mojiretu(string):
	"""
        受け取った文字列を出力する。
        :param :string.
        :return :文字列を返す。
        """
	print (string)

	
>>> mojiretu(ggg)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    mojiretu(ggg)
NameError: name 'ggg' is not defined
>>> def mojiretu(string):
	"""
        受け取った文字列を出力する。
        :param :string.
        :return :文字列を返す。
        """
	print(string)

	
>>> mojiretu("ggg")
ggg
>>> def mojiretu(string):
	"""
        受け取った文字列を出力する。
        :param :string.
        :print :文字列を返す。
        """
	print("string")

	
>>> mojiretu("fff")
string
>>> mojiretu(7)
string
>>> def mojiretu(string):
	"""
        受け取った文字列を出力する。
        :param :string.
        :print :文字列を返す。
        """
	print(string)

	
>>> mojiretu("hana")
hana
>>> 
