class Bank:
    bank_information="Bank_details :"
    def __init__(self,bname,baddr,bcode,bifsc):
        self.bank_name=bname
        self.bank_addr=baddr
        self.branch_code=bcode
        self.branch_IFSC=bifsc
    def bank(self):
        print(Bank.bank_information)
    def display_bank(self):
        print("Enter the bank name :",self.bank_name)
        print("Enter the bank address :",self.bank_addr)
        print("Enter the branch code :",self.branch_code)
        print("Enter the IFSC code :",self.branch_IFSC)
b1=Bank("SBI bank","Bhadgaon",424105,"SBIN0000")
b2=Bank("ICICI bank","Pachora",90767,"IC567898")
print("~"*40)
b1.bank()
print("*"*40)
b1.display_bank()
print("~"*40)
b2.display_bank()
