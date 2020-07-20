from tkinter import*
from tkinter import ttk
stack = []


root = Tk()
root.title("Calculator")
root.config(bg = 'gray', relief = FLAT)
root.geometry("450x610")
root.resizable(0,0)
var1 = StringVar()
var2 = StringVar()
entry =Frame(root)
entry1 = Entry(entry, font=("Aria", 20), borderwidth=0, relief=FLAT, justify=RIGHT,textvariable = var1,width=30)
entry2 = Entry(entry, font=("Aria", 20), borderwidth=0, relief=FLAT, justify=RIGHT,textvariable = var2,width=30)
entry1.pack(expand ='true')
entry2.pack(expand = 'true')
entry.pack()

def input(a):
    lastpos = len(stack) - 1
    if a.isnumeric():
        tmp = 0
        if(len(stack)==0 or not stack[lastpos].isnumeric() ):
            stack.append(a)
        elif stack[lastpos].isnumeric():
            tmp = int(stack.pop())
            stack.append(str(int(a)+(tmp*10)))
    elif a == 'd':
        stack.pop()
        
    elif a == 'ac':
        var2.set('0')
        stack.clear()
    elif a == '=':
        var2.set(eval(str("".join(stack))))
        var1.set(str("".join(stack)))
        #print(eval(str("".join(stack))))
        #stack.clear()
        pass
    else:
        stack.append(a)
    print(stack)
    var1.set(str("".join(stack)))
    if a=='=':
        stack.clear()


        
    
keys = Frame(root)
keys.config(bg = 'red')
keys.pack()
def keyboard():
    
    key0   = Button(keys, text = ' 0 ',font = ('Aria' ,20),bd = 0 ,padx=30,pady=30 ,fg = 'black',bg = 'white', activeforeground ='white',activebackground = 'black',relief = FLAT, command = lambda:input('0'))
    key0.grid(row = 5,column = 1,sticky = N+W+E+S)
    
    key1   = Button(keys, text = ' 1 ',font = ('Aria' ,20),bd = 0 ,padx=30,pady=30 ,fg = 'black',bg = 'white', activeforeground ='white',activebackground = 'black',relief = FLAT,command = lambda:input('1'))
    key1.grid(row = 4,column = 0,sticky = N+W+E+S)
    
    key2   = Button(keys, text = ' 2 ',font = ('Aria' ,20),bd = 0 ,padx=30,pady=30 ,fg = 'black',bg = 'white', activeforeground ='white',activebackground = 'black',relief = FLAT,command = lambda:input('2'))
    key2.grid(row = 4,column = 1,sticky = N+W+E+S)
    
    key3   = Button(keys, text = ' 3 ',font = ('Aria' ,20),bd = 0 ,padx=30,pady=30 ,fg = 'black',bg = 'white', activeforeground ='white',activebackground = 'black',relief = FLAT,command = lambda:input('3'))
    key3.grid(row = 4,column = 2,sticky = N+W+E+S)
    
    key4   = Button(keys, text = ' 4 ',font = ('Aria' ,20),bd = 0 ,padx=30,pady=30 ,fg = 'black',bg = 'white', activeforeground ='white',activebackground = 'black',relief = FLAT,command = lambda:input('4'))
    key4.grid(row = 3,column = 0,sticky = N+W+E+S)
    
    key5   = Button(keys, text = ' 5 ',font = ('Aria' ,20),bd = 0 ,padx=30,pady=30 ,fg = 'black',bg = 'white', activeforeground ='white',activebackground = 'black',relief = FLAT,command = lambda:input('5'))
    key5.grid(row = 3,column = 1,sticky = N+W+E+S)
    
    key6   = Button(keys, text = ' 6 ',font = ('Aria' ,20),bd = 0 ,padx=30,pady=30 ,fg = 'black',bg = 'white', activeforeground ='white',activebackground = 'black',relief = FLAT,command = lambda:input('6'))
    key6.grid(row = 3,column = 2,sticky = N+W+E+S)
    
    key7   = Button(keys, text = ' 7 ',font = ('Aria' ,20),bd = 0 ,padx=30,pady=30 ,fg = 'black',bg = 'white', activeforeground ='white',activebackground = 'black',relief = FLAT,command = lambda:input('7'))
    key7.grid(row = 2,column = 0,sticky = N+W+E+S)
    
    key8   = Button(keys, text = ' 8 ',font = ('Aria' ,20),bd = 0 ,padx=30,pady=30 ,fg = 'black',bg = 'white', activeforeground ='white',activebackground = 'black',relief = FLAT,command = lambda:input('8'))
    key8.grid(row = 2,column = 1,sticky = N+W+E+S)
    
    key9   = Button(keys, text = ' 9 ',font = ('Aria' ,20),bd = 0 ,padx=30,pady=30 ,fg = 'black',bg = 'white', activeforeground ='white',activebackground = 'black',relief = FLAT,command = lambda:input('9'))
    key9.grid(row = 2,column = 2,sticky = N+W+E+S)
    
    delkey = Button(keys, text = 'del',font = ('Aria' ,20),bd = 0 ,padx=30,pady=30 ,fg = 'black',bg = 'white', activeforeground ='red',activebackground = 'black',relief = FLAT,command = lambda:input('d'))
    delkey.grid(row = 5,column = 0,sticky = N+W+E+S)
    
    keyplus= Button(keys, text = ' + ' ,font = ('Aria' ,20),bd = 0,padx=30,pady=30 ,fg = 'black',bg = 'orange', activeforeground ='white',activebackground = 'black',relief = FLAT,command = lambda:input('+'))
    keyplus.grid(row = 5,column = 3,sticky = N+W+E+S)

    keyminu= Button(keys, text = ' - ' ,font = ('Aria' ,20),bd = 0,padx=30,pady=30 ,fg = 'black',bg = 'orange', activeforeground ='white',activebackground = 'black',relief = FLAT,command = lambda:input('-'))
    keyminu.grid(row = 4,column = 3,sticky = N+W+E+S)

    keyinto= Button(keys, text = ' * ' ,font = ('Aria' ,20),bd = 0,padx=30,pady=30 ,fg = 'black',bg = 'orange', activeforeground ='white',activebackground = 'black',relief = FLAT,command = lambda:input('*'))
    keyinto.grid(row = 3,column = 3,sticky = N+W+E+S)

    keydivi= Button(keys, text = ' / ' ,font = ('Aria' ,20),bd = 0,padx=30,pady=30 ,fg = 'black',bg = 'orange', activeforeground ='white',activebackground = 'black',relief = FLAT,command = lambda:input('/'))
    keydivi.grid(row = 2,column = 3,sticky = N+W+E+S)

    keypowe= Button(keys, text = ' ^ ' ,font = ('Aria' ,20),bd = 0,padx=30,pady=30 ,fg = 'black',bg = 'orange', activeforeground ='white',activebackground = 'black',relief = FLAT,command = lambda:input('**'))
    keypowe.grid(row = 1,column = 3,sticky = N+W+E+S)

    
    keylbrc= Button(keys, text = ' ) ' ,font = ('Aria' ,20),bd = 0,padx=30,pady=30 ,fg = 'black',bg = 'orange', activeforeground ='white',activebackground = 'black',relief = FLAT,command = lambda:input(')'))
    keylbrc.grid(row = 1,column = 2,sticky = N+W+E+S)

    keyrbrc= Button(keys, text = ' ( ' ,font = ('Aria' ,20),padx=30,pady=30 ,fg = 'black',bg = 'orange', activeforeground ='white',activebackground = 'black',relief = FLAT,command = lambda:input('('))
    keyrbrc.grid(row = 1,column = 1,sticky = N+W+E+S)

    keyequa= Button(keys, text = ' = ' ,font = ('Aria' ,20),bd = 0,padx=30,pady=30 ,fg = 'black',bg = 'green', activeforeground ='white',activebackground = 'black',relief = FLAT,command = lambda:input('='))
    keyequa.grid(row = 5,column = 2,sticky = N+W+E+S)
    keyrac = Button(keys, text = 'AC ' ,font = ('Aria' ,20),bd = 0,padx=30,pady=30 ,fg = 'black',bg = 'red', activeforeground ='white',activebackground = 'black',relief = FLAT,command = lambda:input('ac'))
    keyrac.grid(row = 1,column = 0,sticky = N+W+E+S)

    '''display1 = Entry(root, font=("Aria", 16), borderwidth=0, relief=FLAT, justify=RIGHT)
    display1.grid(row = 0 , column = 0,columnspan = 5,sticky = N+W+E+S)
    
    display2 = Entry(root, font=("Sans", 20), borderwidth=0, relief=FLAT, justify=RIGHT)
    display2.grid(row = 1 , column = 0,columnspan = 5,sticky = N+W+E+S)
    display2.insert(0, "0")
       '''

keyboard()    
root.mainloop()