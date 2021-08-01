import sys
from pyrecord import Records
from pyrecord import Record
from pycategory import Categories
import tkinter as tk
import tkinter.ttk as ttk

# categories = Categories()
# records = Records()

# while True:
#     command = input('\nWhat do you want to do (add / view / delete / view categories / find / exit)? ')
#     if command == 'add':
#         record = input('Add an expense or income record with category, description, and amount (separate by spaces):')
#         records.add(record, categories)
#     elif command == 'view':
#         records.view()
#     elif command == 'delete':
#         delete_record = input("Which record do you want to delete? ")
#         records.delete(delete_record)
#     elif command == 'view categories':
#         categories.view()
#     elif command == 'find':
#         category = input('Which category do you want to find? ')
#         target_categories = categories.find_subcategories(category)
#         records.find(target_categories)
#     elif command == 'exit':
#         records.save()
#         break
#     else:
#         sys.stderr.write('Invalid command. Try again.\n')

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self._master = master

        self._categories = Categories()
        self._records = Records()

        self._label1 = tk.Label(self._master, text="Catogory:", font=("Calibri", 12))
        self._label1.place(x=10, y=10)

        self._moneyLabel = tk.Label(self._master, text="Your money:  ", font=("Calibri", 14, 'bold'))
        self._moneyLabel.place(x=565, y=37)

        self._categoriesList = ['All']
        self._categoriesList.extend(self._categories.find_subcategories('expense'))
        self._categoriesList.extend(self._categories.find_subcategories('income'))
        self._select = ttk.Combobox(self._master, values=self._categoriesList, font=("Calibri", 12))
        self._select.place(x=10, y=40, width=200)
        self._select.bind("<<ComboboxSelected>>", lambda event:self.firstCategoreListSelected(event))
        self._select.current(0)

        self._deleteButton = tk.Button(self._master, text='Delete Record', command=self.deleteRecord)
        self._deleteButton.place(x=720, y=268, width=100)

        self._myentry = tk.Entry(self._master, font=("Calibri", 12))
        self._myentry.place(x=10, y=310, width=700)

        self._addButton = tk.Button(self._master, text='Add Record', command=self.addRecord)
        self._addButton.place(x=720, y=310, width=100)

        self._listboxHeader = tk.Listbox(self._master, font=("consolas", 12), height=1)
        self._listboxHeader.insert(0, "Date           Category            Name                     Amount    ")
        self.disable_item(0)
        self._listboxHeader.place(x=10, y=70, width=700)

        self._listbox = tk.Listbox(self._master, font=("consolas", 12), height=10)
        self._listbox.place(x=10, y=90, width=700)
        
        self._scrollbar = tk.Scrollbar(self._listbox, orient="vertical")
        self._scrollbar.config(command=self._listbox.yview)
        self._scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

        self._listbox.config(yscrollcommand=self._scrollbar.set)
        # self._listbox.bind("<<ListboxSelect>>", lambda event:self.selected(event))

        self.updateListbox(self._select.get())

        self._master.protocol("WM_DELETE_WINDOW", self.on_closing)


    def on_closing(self):
        self._records.save()
        self._master.destroy()

    def disable_item(self,index):
        self._listboxHeader.itemconfig(index, fg="gray")
        self._listboxHeader.bind("<<ListboxSelect>>", lambda event, index=index: self.noSelection(event, index))

    def noSelection(self, event, index):
        if len(self._listboxHeader.curselection()) > 0 and self._listboxHeader.curselection()[0] == index:
            self._listboxHeader.selection_clear(index)

    # def selected(self, event):
    #     if len(self._listbox.curselection()) > 0 and self._listbox.curselection()[0] >= 0 and self._listbox.curselection()[0] < len(self._records.getRecords()):
    #         print(self._listbox.get(self._listbox.curselection()[0]))

    def firstCategoreListSelected(self, event):
        self.updateListbox(self._select.get())
        
    def addRecord(self):
        self._records.add(self._myentry.get(), self._categories)
        self.updateListbox(self._select.get())

    def deleteRecord(self):
        # print(self._listbox.get(self._listbox.curselection()[0]))
        if len(self._listbox.curselection()) > 0 and self._listbox.curselection()[0] >= 0 and self._listbox.curselection()[0] < len(self._records.getRecords()):
            records = self._records.getRecords()
            selected_record = self._listbox.get(self._listbox.curselection()[0]).split()
            for i, record in enumerate(self._records.getRecords()): #for (1, ('meal', 'breakfast', -50)) in [(1, ('meal', 'breakfast', -50)), (2, ('drink', 'coffee', -100))]
                if selected_record[0] == record.date and selected_record[1] == record.category and selected_record[2] == record.name and selected_record[3] == str(record.amount): 
                    records[i:i+1] = []
                    self._records.setRecords(records)
                    break
            self.updateListbox(self._select.get())

    def updateListbox(self, category):
        target_categories = []
        if(category == 'All'):
            target_categories = self._categories.find_subcategories('expense')
            target_categories.extend(self._categories.find_subcategories('income'))
        else:
            target_categories = self._categories.find_subcategories(category)
        target_records = self._records.find(target_categories)
        target_records.sort(key=lambda x: x.date, reverse=True)
        self._listbox.delete(0, tk.END)
        for i, record in enumerate(target_records):
            num_of_space=15-len(record.date)
            space0=' '*num_of_space
            num_of_space=20-len(record.category)
            space=' '*num_of_space
            num_of_space2=25-len(record.name)
            space2=' '*num_of_space2
            space3=' '*(10-len(str(record.amount)))
            self._listbox.insert(i, record.date+space0+record.category+space+record.name+space2+str(record.amount)+space3)
        money=sum(record.amount for record in target_records)
        self._moneyLabel['text'] = "Your money:  " + str(money)


root = tk.Tk()
root.title("PyMoney")
root.geometry("830x400")

app = Application(master=root)
app.mainloop()

