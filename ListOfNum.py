#Write a program that takes a list of numbers and changes one element and replaces it with another number and removes another element and adds it to another list and displays it in another list.
class mylist:
    def __init__(self, n):
        self.__list = []
        self.size = n
        for i in range(n):
            self.__list.append(0)

    def changesize(self):
        self.size = len(self.__list)

    def set(self, n, x):
        self.__list[n] = x

    def show(self):
        print(self.__list)

    def append(self, x):
        self.__list.append(x)
        self.changesize()

    def delete(self, i):
        del self.__list[i]
        self.changesize()

    def add(self, m2):
        l = mylist(self.size)
        for i in range(self.size):
            l.set(i, self.__list[i] + m2.__list[i])
        return l


A = mylist(5)
A.set(2, 7)
A.set(3, 8)
print('A:')
print(type(A))

print('B:')
B = mylist(5)
print(type(B))
B.set(2, 7)
B.set(4, 8)
B.show()

print('C:')
C =A.add(B)
print(type(C))
C.show()
