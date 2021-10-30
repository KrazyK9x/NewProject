from main import HelloClass
from third import NameClass as name
# from foldername.filename import classname

if __name__ == "__main__":
    HelloClass = HelloClass()
    HelloClass.CallHello()
    HelloClass.SayGoodbye()
    NameClass = name()
    NameClass.CallName()