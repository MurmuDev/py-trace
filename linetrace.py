import sys
import inspect

#global line data
line_set = set()
line_dict = {}


class Color():
    #add your color(s) here
    CBLACK  = '\33[30m'
    CRED    = '\33[31m'
    CGREEN  = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE   = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE  = '\33[36m'
    CWHITE  = '\33[37m'

    CBLACKBG  = '\33[40m'
    CREDBG    = '\33[41m'
    CGREENBG  = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG   = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG  = '\33[46m'
    CWHITEBG  = '\33[47m'

    CEND = '\033[0m'

class CodeHeat():

    #create a mapping of frequency_atleast : color
    heat = {
         1: Color.CVIOLETBG,
         2: Color.CREDBG
    }

    def getColor(freq):
        color = CodeHeat.heat.get(freq,"none")
        while color == "none":
            freq -= 1
            color = CodeHeat.heat.get(freq,"none")
        return color





#context manager for tracing
class Tracer(object):

    def __init__(self,func):
        self.func = func

    def __enter__(self):
        sys.settrace(self.func)
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        sys.settrace(None)
        #write_dict()
        print_colored()

#function for printing the code
def print_colored():
    with open('./linetrace.py') as fp:
        line = fp.readline()
        lineno = 1

        while lineno<=startline+1:
            lineno +=1
            line = fp.readline()

        while line and lineno<endline:
            if lineno in line_set:
                #change output color here
                print(CodeHeat.getColor(line_dict[lineno]),line.rstrip(),Color.CEND)
            else:
                print(line.rstrip())
            line = fp.readline()
            lineno += 1

# get current line no
def getCurrentLine():
    return inspect.currentframe().f_back.f_lineno

x = getCurrentLine()


# function to trace the code
def trace_func(frame,event,arg):
        #co = frame.f_code
        ignoreLength = 0
        #func_name = co.co_name #get function name of current stack
        func_lineno = frame.f_lineno-ignoreLength
        caller_lineno = frame.f_back.f_lineno-ignoreLength  #get info about the previos frame
        if event == 'line':
            if func_lineno>startline and caller_lineno> startline:
                line_set.add(func_lineno)
                line_set.add(caller_lineno)
                line_dict[func_lineno] = line_dict.get(func_lineno,0)+1
                line_dict[caller_lineno] = 1
        return trace_func


startline = getCurrentLine()
def Trace():
    #insert proper python code within the Tracer() body
    global startline
    startline = getCurrentLine()
    with Tracer(trace_func):
    # ADD YOUR WHOLE CODE AFTER THIS LINE
        class A:
             x=''
             y=''

             def getx(self):
                return self.x

             def method1(f):
                 return None

             def gety(self):
                return self.y

             def __init__(self,x, y):
                self.x = x
                self.y = y


        def method1(x,y):
            return(y)

        p = A(9,2)
        s = method1(2,3)
        y =  A(1,2)
        z = A(3,4)
        method1(x,y)

# ADD YOUR WHOLE CODE BEFORE THIS LINE
endline = getCurrentLine()
Trace()
