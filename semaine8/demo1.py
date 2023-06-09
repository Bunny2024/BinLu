class Site:
    def __init__(self, name, url):
        self.name = name       # public
        self.__url = url   # private
 
    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)
 
    def __foo(self):          
        print('This is private.')
 
    def foo(self):           
        print('This is public.')
        self.__foo()
 
x = Site('runoob', 'www.runoob.com')
x.who()        # true
x.foo()        # true
x.__foo()      # false