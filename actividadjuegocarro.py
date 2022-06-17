from tkinter import *
from tkinter import messagebox

class JuegoCoche:
    
    def __init__(self, root):
        self.f1 = 1
        self.f2 = 1
        self.f3 = 1
        self.root = root
        self.vel = 50
        self.x1 = 0 
        self.y1 = 0
        self.x2 = 0 
        self.y2 = 0
        self.k = ""
        self.widgets()
        self.muros()
        self.root.title("Juego de carro chocon")
        
        
    def widgets(self):
        self.lienzo = Canvas(self.root, width = 300, height = 600 , bg = "white")
        self.lienzo.pack()
        botonizq = Button(self.root, text = "Izquierda", command = lambda:self.lienzo.coords(self.carrito, 0,520,54,600))
        botonvel = Button(self.root, text = "Velocidad", command = self.Velocidad)
        botonder = Button(self.root, text = "Derecha", command = lambda:self.lienzo.coords(self.carrito, 250,520,300,600))
        botonizq.pack(side = "left", ipadx = "30", ipady = "8")
        botonvel.pack(side = "left", ipadx = "30", ipady = "8")
        botonder.pack(side = "right", ipadx = "30", ipady = "8")
        self.muro1 = self.lienzo.create_rectangle(150,270,300,300, fill = "black")
        self.muro2 = self.lienzo.create_rectangle(0,0,150,30, fill = "black")
        self.muro3 = self.lienzo.create_rectangle(150,-270,300,-240, fill = "black")
        self.carrito = self.lienzo.create_rectangle(250, 520, 300, 600, fill = "blue")
        
        
        
    def muros(self):
        self.poscarrito = self.carrito
        self.posmuro1 = self.muro1
        self.posmuro2 = self.muro2
        self.posmuro3 = self.muro3
        ac,bc,cc,self.dc = self.lienzo.coords(self.poscarrito)
        a,b,c,self.d = self.lienzo.coords(self.posmuro1)
        a2,b2,c2,self.d2 = self.lienzo.coords(self.posmuro2)
        a3,b3,c3,self.d3 = self.lienzo.coords(self.posmuro3)
        self.lienzo.coords(self.muro1, a,b + 5,c,self.d + 5)
        self.lienzo.coords(self.muro2,a2,b2 + 5,c2,self.d2 + 5)
        self.lienzo.coords(self.muro3,a3,b3 + 5,c3,self.d3 + 5)
        
        self.Choque(self.d,a,c,bc,cc)
        self.Choque(self.d2,a2,c2,bc,cc)
        self.Choque(self.d3,a3,c3,bc,cc)
        self.Choque(self.d,a,c,bc,ac)
        self.Choque(self.d2,a2,c2,bc,ac)
        self.Choque(self.d3,a3,c3,bc,ac)
        
        
        if self.d >= 600 and self.f1 == 1:
            self.lienzo.coords(self.muro1,150, -270, 300, -240)
            self.f1 = 0
        elif self.d2 >= 600 and self.f2 == 1:
            self.lienzo.coords(self.muro2,0,-270,150,-240)
            self.f2 = 0
        elif self.d3 >= 600 and self.f3 == 1:
            self.lienzo.coords(self.muro3,150,-270,300,-240)
            self.f3 = 0
        if self.d >= 600 and self.f1 == 0:
            self.lienzo.coords(self.muro1,0, -270, 150, -240)
            self.f1 =1
        elif self.d2 >= 600 and self.f2 == 0:
            self.lienzo.coords(self.muro2,150,-270,300,-240)
            self.f2 = 1
        elif self.d3 >= 600 and self.f3 == 0:
            self.lienzo.coords(self.muro3,0,-270,150,-240)
            self.f3 = 1
             
            
        self.root.after(self.vel, self.muros)  
    
    def Velocidad(self):
        self.vel = self.vel - 5   
        if self.vel == 5:
            self.vel = 50
    
        
    def Choque(self,x,y,z,h,g):
        
        if x == h:
            
            if y == g:
                messagebox.showinfo("AYYYYY", "PERDISTE TONTO")
                if messagebox.askyesno("juego", "quieres intentarlo otra vez?"):
                    self.lienzo.coords(self.muro1,150, 270, 300, 300)
                    self.lienzo.coords(self.muro2,0, 0, 150, 30)
                    self.lienzo.coords(self.muro3,150, -270, 300, -240)
                    self.vel = 50
                else:
                    self.root.quit()
            elif z == g:
                messagebox.showinfo("AYYYYY", "PERDISTE TONTO")
                if messagebox.askyesno("juego", "quieres intentarlo otra vez?"):
                    self.lienzo.coords(self.muro1,150, 270, 300, 300)
                    self.lienzo.coords(self.muro2,0, 0, 150, 30)
                    self.lienzo.coords(self.muro3,150, -270, 300, -240)
                    self.vel = 50
                else:
                    self.root.quit()
               
                
                
root = Tk()
app = JuegoCoche(root)
root.mainloop()
