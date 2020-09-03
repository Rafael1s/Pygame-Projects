import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog

class dialogGame():
    
    def __init__(self, game):
        
        self.game = game
        
    def readFileDialog(self):
 
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename()
        
        print('file_path: ', file_path)
        
        words_of_path = file_path.split('/')
        file_name = words_of_path[-1]
        
        self.game.update_title('Game of life,   pattern file:   ' + file_name)
                
        self.read(file_path)   
        
        return file_name

    def read(self, file):
        try:
           inputedFile = open(file, "r")
        except IOError:
           print("No such file")
           return
        
        self.game.sprites.empty()
        self.game.cells = []
        self.game.createGrid()
        self.game.time_start = 0
        self.game.runGame = False
        
        for line in inputedFile:
            words = line.split(',')
            ## pos = [int(words[0]), int(words[1])]
            num = int(words[2])
            
            for cell in self.game.cells:
                if cell.num == num:
                    cell.live()
                    cell.image.fill(cell.color)
            
            
    def saveFileDialog(self): 
        
        root = tk.Tk()
        root.withdraw()

        save_text_as = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        
        print('file_path: ', save_text_as)
        
        if save_text_as:
           self.save(save_text_as)
        else:
           print('error: No file open') 
        
    def save(self, outputFile):

        for cell in self.game.cells:
            if cell.alive:
                pos = cell.rect.topleft
                col = pos[0]
                row = pos[1]
                num = cell.num
                
                line = str(col) + ', ' + str(row) + ', ' +  str(num) + '\n'
                outputFile.write(line)
                                
        outputFile.close()
        

    def getValue(self):
    
         ## app_window = tk.Tk()
         root = tk.Tk()
         root.withdraw()
         
         ## fps - frame per second
         answer = simpledialog.askstring("Insert", prompt = "Insert fps [2,40]:") ## , minvalue="2", maxvalue="20")

         try:
             value = int(answer) 
         except ValueError:  
             print('input error: ', answer)
             return -1
         
         if 1 < value < 41:  
            return value   
         else:
            return -1  
        
        
        
        
        
        
        