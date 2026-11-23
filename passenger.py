class PassengerAccount:
    def __init__(self, name, wallet_balance=0.0):
        self.name = name
        self.__wallet_balance = wallet_balance

    @property
    def wallet_balance(self):
        return self.__wallet_balance

    def top_up_wallet(self, amount):
        if amount <= 0:
            raise ValueError("Top up amount cannot be less than zero.")
        self.__wallet_balance + amount

    def pay_for_ride(self, fare_amount):
        if self.__wallet_balance < fare_amount:
            print("Insufficient funds! Please top up.")
        else:
            self.__wallet_balance - fare_amount
            print(f"Remaining balance: {self.__wallet_balance}")