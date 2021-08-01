from datetime import date
import re
import sys

class Record:
    """Represent a record."""
    def __init__(self, category, name, amount, date):
        # 1. Define the formal parameters so that a Record can be instantiated
        #    by calling Record('meal', 'breakfast', -50).
        # 2. Initialize the attributes from the parameters. The attribute
        #    names should start with an underscore (e.g. self._amount)
        self._category = category
        self._name = name
        self._amount = amount
        self._date = date

    @property
    def category(self):
        return self._category

    @property
    def name(self):
        return self._name

    @property
    def amount(self):
        return self._amount

    @property
    def date(self):
        return self._date

    # Define getter methods for each attribute with @property decorator.
    # Example usage:
    # >>> record = Record('meal', 'breakfast', -50)
    # >>> record.amount
    # -50

class Records:
    """Maintain a list of all the 'Record's and the initial amount of money."""
    def __init__(self):
        """initialize the item list and money, open the file (if existed) and check the data correctness.
        """
        # 1. Read from 'records.txt' or prompt for initial amount of money.
        # 2. Initialize the attributes (self._records and self._initial_money)
        #    from the file or user input.
        try:
            with open('record.txt') as fh:
                line1=fh.readline()
                if line1 == '':
                     raise ValueError
                deposit=int(line1)
                my_list_read=fh.readlines() #['A a 1','B b 2','C c 3']
                my_list=[]
                for i in my_list_read:
                    item = i.split()
                    if len(item) != 4:
                        raise ValueError 
                    record = Record(item[0], item[1], int(item[2]), item[3])
                    my_list.append(record) #[('A','a',1),('B','b',2),('C', c',3)]
                print('Welcome back! ')
        except (FileNotFoundError, ValueError) as error:
            if isinstance(error, ValueError):
                    print(f'Invalid format in records.txt. Deleting the contents.\n')
            try:
                deposit = int(input('How much money do you have? '))
            except ValueError:
                sys.stderr.write('Invalid value for money. Set to 0 by default. ')
                deposit=0
            my_list=[] #[('breakfast', -50),( lunch -70), dinner -100, salary 3500]  
        
        self._initial_money = deposit
        self._records = my_list

    def add(self, recordString, categories):
        """add item to item list,format :"category item money."
        """
        # 1. Define the formal parameter so that a string input by the user
        #    representing a record can be passed in.
        # 2. Convert the string into a Record instance.
        # 3. Check if the category is valid. For this step, the predefined
        #    categories have to be passed in through the parameter.
        # 4. Add the Record into self._records if the category is valid.
        try:
            ErrorType=0
            item=recordString.split()#['breakfast', -50]
            if len(item) != 3 and len(item) != 4:
                ErrorType=1
                raise ValueError
            if len(item) == 3:
                todayString = date.today().isoformat()
                if categories.is_category_valid(item[0]) == 'yes':
                    record = Record(item[0], item[1], int(item[2]), todayString)
                    self._records.append(record) #[('a',1),('b',2),('c',3)]
                else:
                    ErrorType=2
                    raise ValueError
            elif len(item) == 4:
                if categories.is_category_valid(item[1]) == 'yes':
                    try:
                        date.fromisoformat(item[0])
                        record = Record(item[1], item[2], int(item[3]), item[0])
                        self._records.append(record) #[('a',1),('b',2),('c',3)]
                    except:
                        ErrorType=3
                        raise ValueError
                else:
                    ErrorType=2
                    raise ValueError
            
        except ValueError:
            if ErrorType == 1:
                sys.stderr.write('The format of a record should be like this: breakfast -50.\nFail to add a record.\n')
            elif ErrorType == 2:
                sys.stderr.write('The specified category is not in the category list.\nYou can check the category list by command "view categories".\nFail to add a record.')
            elif ErrorType == 3:
                sys.stderr.write('The format of date should be YYYY-MM-DD.\nFail to add a record.\n')
            else:
                sys.stderr.write('Invalid value for money.\nFail to add a record.\n')

    def view(self):
        """view existing content in item list, also calculate the money you left.
        """
        # 1. Print all the records and report the balance.
        if len(self._records) == 0:
            print("Here's your expense and income records: ")
            print('Date       Category        Description          Amount')
            print('========== =============== ==================== ======')
            print('empty, please add new record')
            print('=============== ==================== ======')
            print('Now you have %d dollars.'% self._initial_money)

        else:    
            print("Here's your expense and income records: ")
            print('Date       Category        Description          Amount')
            print('========== =============== ==================== ======')
            for record in self._records:
                num_of_space=11-len(record.date)
                space0=' '*num_of_space
                num_of_space=16-len(record.category)
                space=' '*num_of_space
                num_of_space2=21-len(record.name)
                space2=' '*num_of_space2
                print(record.date+space0+record.category+space+record.name+space2+str(record.amount)) 
            print('========== =============== ==================== ======')
            new_deposit=self._initial_money+sum(record.amount for record in self._records)
            print('Now you have %d dollars.'%new_deposit)

    def delete(self, del_item):
        """you can delete any item on the item list, just provide the item name and its order.
        """
        # 1. Define the formal parameter.
        # 2. Delete the specified record from self._records.
        find_or_not=False
        if len(self._records) <= 1:
            sys.stderr.write('Invalid format. Fail to delete a record.\n') 
        else:
            order = int(input('please give order of the record in the table. ' ))
            enumerate_my_list = enumerate(self._records,1) #[(1, ('meal', 'breakfast', -50)), (2, ('drink', 'coffee', -100))]
            for enumerate_tuple in enumerate_my_list: #for (1, ('meal', 'breakfast', -50)) in [(1, ('meal', 'breakfast', -50)), (2, ('drink', 'coffee', -100))]
                if del_item == enumerate_tuple[1].name: 
                    if order == enumerate_tuple[0]: #check order
                        self._records[order-1:order] = []
                        find_or_not = True
                        break
            if find_or_not == False: 
                sys.stderr.write("There's no record with "+del_item+'. Fail to delete a record.\n')

    def find(self, sub_category_list):
        """find and show the items belongs to specific category.
        """
        # 1. Define the formal parameter to accept a non-nested list
        #    (returned from find_subcategories)
        # 2. Print the records whose category is in the list passed in
        #    and report the total amount of money of the listed records.
        filter_list=list(filter(lambda record: record.category in sub_category_list, self._records))
        return filter_list
        # print(f'''Here's your expense and income records under category ({', '.join(sub_category_list)}):''')
        # print('Date       Category        Description          Amount')
        # print('========== =============== ==================== ======')
        # for record in filter_list:
        #     num_of_space=11-len(record.date)
        #     space0=' '*num_of_space
        #     num_of_space=16-len(record.category)
        #     space=' '*num_of_space
        #     num_of_space2=21-len(record.name)
        #     space2=' '*num_of_space2
        #     print(record.date+space0+record.category+space+record.name+space2+str(record.amount)) 
        # print('========== =============== ==================== ======')
        # total_filter_amount = sum([record.amount for my_tuple in filter_list])
        # print(f'The total amount above is {total_filter_amount}')

    def save(self):
        """save the changes you do this time before exit.
        """
        # 1. Write the initial money and all the records to 'records.txt'.
        my_list_write=[]
        for record in self._records:#('A','a',1) in [('A','a',1),('B','b',2)]
            item_str=record.category+' '+record.name+' '+str(record.amount)+' '+record.date+'\n' #'A a 1'
            my_list_write.append(item_str) #['A a 1','B b 2','c 3']
        with open('record.txt','w') as fh:
            fh.write(str(self._initial_money))
            fh.write('\n')
            fh.writelines(my_list_write) 

    def getRecords(self):
        return self._records

    def setRecords(self, records):
        self._records = records
