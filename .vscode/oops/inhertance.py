class parent:
    def display(self):
        print("parent")
class child(parent):
    def show(self):
        print("child")

c1=child()
c1.show()
c1.display()


#multi-level inhertance

class main:
    def read(self):
        print("gran")

class sub_main(main):
    def writting(self):
        print("parent")

class lower_main(sub_main):
    print("child")


obj=lower_main()
obj.writting()
obj.read()


#herichical inhertance


