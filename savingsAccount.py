    def __eq__


    def __lt__(self, other):
        """Returns True if name of self is less than name of other or False otherwise"""
        return self.name < other.name






class ShareCell(object):
    """Synchronize readers and writers"""
    
    def __init__(self, data):
        self.data = data
        self.writin = False
        self.okToRead = condition()
        self.okToWrite = condition()
    
    def begin_read(self):
        "Waits until writer is not writting"

account = savingsAccount(name = "ken", balance = 100.00)
cell = ShareCell(account)
print("The account balance is: ", cell.read(lambda account: account(getBalance())))
amount = 200.00
cell.write(lambda account:account.deposit(amount))