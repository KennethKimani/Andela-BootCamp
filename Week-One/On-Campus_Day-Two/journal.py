import datetime

class Journal():
    #user id is zero and increments with every new user created
    user_id=0


    def __init__(self, user_name=raw_input("please enter username: ")):
       self.user_name= user_name
       self.journal_dict = {}
       self.journal_entries = list()
       self.journal = ""

    def create_journal(self):
        '''
        Creates a new journal if it does not already exists
        '''
        self.journal = raw_input("Enter the Journal Title:")
        if self.journal not in self.journal_entries:
           self.journal_entries.append(self.journal)

        else:
            self.create_journal(self)
            print "\n The Journal title already exist, create a new one \n"

    def create_entry(self):
        self.key = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.entry = raw_input("Enter journal entry: ")
        self.journal_dict.update({self.key : self.entry})

    def list_journal_entries(self):
        """Show a list of jornal entries"""
        if len(self.journal_dict) == 0:
            print "\n Sorry you have no journal entries \n"
        else:
            print "\n"
            for key, value in sorted(self.journal_dict.items()):
                print key + " => " + value

    def get_last(self):
        if len(self.journal_dict) == 0:
            print "\n Sorry you have no journal entries \n"
        else:
            lastKey = sorted(self.journal_dict.keys())[-1]
            lastValue = sorted(self.journal_dict.values())[-1]
            lastval = self.journal_dict.get(lastKey, -1)
            print "\n last item in Journal: " + str(lastKey) + ":" + str(lastval)+ "\n"
          
    def delete_journal_entry(self):
        #print "Function to be added later"
        entry_key = raw_input("Enter Journal Entry to delete: ")

        if entry_key in self.journal_dict:
            del self.journal_dict[entry_key]
            print "Delete completed successfully"
        else:
            print "Delete not successful. Key not found"

            
ken = Journal()

menu = {}
menu['1'] = "Create  Journal."
menu['2'] = "Create  Journal Entry."
menu['3'] = "List All Journal Entries"
menu['4'] = "Show Last Journal Entry"
menu['5'] = "Delete Journal Entry"
menu['6'] = "Exit"
while True:
    options = menu.keys()
    options.sort()
    print "\n"
    for entry in options:
        print entry, menu[entry]

    selection = raw_input("Please Select:")
    if selection == '1':

        ken.create_journal()
    elif selection == '2':

        ken.create_entry()
    elif selection == '3':

        ken.list_journal_entries()
    elif selection == '4':

        ken.get_last()
    elif selection == '5':

        ken.delete_journal_entry()
    elif selection == '6':
        break
    else:
        print "Unknown Option Selected!"
