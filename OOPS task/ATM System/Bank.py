class BankAccount:
    bank_name="State Bank of India"
    total_accounts=0
    interest_rate=4.0
    MIN_BALANCE=500
    _next_account_number=1001
    def __init__(self,holder_name,account_type,initial_deposit,pin):
        self.holder_name=holder_name
        self._account_number=BankAccount._next_account_number
        self._next_account_number+=1
        self._account_type=account_type
        if initial_deposit>=BankAccount.MIN_BALANCE:
            self.__balance=initial_deposit
        else:
            raise ValueError(f"Blocked (below min): Minimum balance should be 500")
        self.__pin=pin
        BankAccount.total_accounts+=1
    @property
    def account_number(self):
        return self._account_number
    @property
    def balance(self):
        return self.__balance
    def deposit(self,amount):
        if amount==0:
            raise ValueError(f"Blocked (Zero): Deposit amount cannot be zero")
        elif amount<0:
            raise ValueError(f"Blocked (negative): Deposit amount must be positive")
        else:
            self.__balance+=amount
            print(f"Deposit {amount} -> {self.__balance}")
    def withdraw(self,amount,pin):
        if(BankAccount.__verify_pin(pin)):
            if amount>self.__balance or self.__balance-amount<500:
                raise ValueError("Blocked (below min):Insufficient funds. Minimum balance 500 must remain")
            elif amount<=0:
                raise ValueError("Blocked (negative): Withdraw amount must be positive")
            elif amount<self.__balance:
                self.__balance-=amount
            else:
                raise TypeError("Amount must be positive number")
        else:
            raise ValueError("Blocked (wrong PIN): Incorrect PIN")
    def __verify_pin(self,pin):
        if self.__pin==pin:
            return True
        else:
            return False
    def change_pin(self,old_pin,new_pin):
        if(BankAccount.__verify_pin(old_pin)):
            if len(str(new_pin))==4 and isinstance(new_pin,int):
                self.__pin=new_pin
                print("PIN changed successfully")
            else:
                raise ValueError("Blocked (Wrong PIN):PIN must be a 4 digit number")
        else:
            raise ValueError("Blocked (Wrong PIN):Incorrect PIN")
    def add_annual_interest(self):
        self.interest_rate+=self.__balance*self.interest_rate/100
        return self.interest_rate
    @classmethod
    def get_total_accounts(cls):
        return BankAccount.total_accounts
    @staticmethod
    def is_valid_amount(amount):
        if amount>0:
            return True
        return False
    def __str__(self):
        return f"Account [{self._account_number}] {self.holder_name} | {self._account_type} | Rs.{self.__balance}"
    