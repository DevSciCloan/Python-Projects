import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        # Removing resizable
        self.master.resizable(width=False, height=False)
        # Setting the width and height of GUI
        self.master.geometry('{}x{}'.format(680,200))
        self.master.title("Web Page Generator")
        # Instantiating StringVar() for custom_h1 Entry
        self.varCustom = StringVar()
        
        self.custom_h1_lbl = Label(self.master,text='Enter custom text or click the Default HTML page button')
        self.custom_h1_lbl.grid(row=0,column=0, padx=(30,0), pady=(30,0))
        
        self.custom_h1 = Entry(self.master,text=self.varCustom, font=("Helvetica", 16))
        self.custom_h1.grid(row=1,column=0, columnspan=3, padx=(20,0), pady=(20,0), sticky=NSEW)
        
        self.btn_default = Button(self.master, text = "Default HTML Page", width=20, height=2, command=self.defaultHTML)
        self.btn_default.grid(row=2,column=1,padx=(0,0), pady=(30,10), sticky=NE)

        self.btn_custom = Button(self.master, text = "Submit Custom Text", width=20, height=2, command=self.customHTML)
        self.btn_custom.grid(row=2,column=2,padx=(10,0), pady=(30,0), sticky=NE)

    # Creates a new html page and opens it in a new tab in default browser with hard coded h1 text 
    def defaultHTML(self):
        htmlText= "Stay tuned for our amazing summer sale!"
        htmlFile = open('index.html', 'w')
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab('index.html')

    # Creates a new html page and opens it in a new tab in default browser with user input from custom_h1 Entry as the h1 text
    def customHTML(self):
        htmlText = self.custom_h1.get()
        htmlFile = open('index.html', 'w')
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab('index.html')


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
