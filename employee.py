"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Contract:
    def __init__(self, type, hours, hourly_rate, contracts, commission_amount, bonus_amount):
        self.type = type
        self.hours = hours
        self.hourly_rate = hourly_rate
        self.contracts = contracts
        self.commission_amount = commission_amount
        self.bonus_amount = bonus_amount

    def get_pay(self):
        if self.type == "salary":
            return self.monthly_salary
        elif self.type == "hourly":
            return self.hours * self.hourly_rate
        else:
            raise ValueError("Invalid contract type")

    def __str__(self):
        if self.type == "salary":
            return f"{self.name} works on a monthly salary of {self.monthly_salary}. Their total pay is {self.monthly_salary}."
        elif self.type == "hourly":
            return f"{self.name} works on a contract of {self.hours} hours at {self.hourly_rate}/hour. Their total pay is {self.pay}."
        else:
            return "Invalid contract type"

class Commission:
    def __init__(self, type, amount, contracts):
        self.type = type
        self.amount = amount
        self.contracts = contracts

    def get_commission(self):
        if self.type == "bonus":
            return self.amount
        elif self.type == "contract":
            return self.amount * self.contracts
        else:
            raise ValueError("Invalid commission type")

    def __str__(self):
        if self.type == "bonus":
            return f"{self.name} receives a bonus commission of {self.amount}. Their total commission is {self.get_commission()}."
        elif self.type == "contract":
            return f"{self.name} receives a commission for {self.contracts} contract(s) at {self.amount}/contract. Their total commission is {self.get_commission()}."
        else:
            return "Invalid commission type"

class Employee:
    def __init__(self, name, contract, commission):
        self.name = name
        self.contract = contract
        self.commission = commission

    def get_pay(self):
        total_pay = self.contract.get_pay()
        total_commission = self.commission.get_commission()
        total_earnings = total_pay + total_commission

        return total_earnings

    def __str__(self):
        return f"{self.name}'s pay is calculated as follows: {self.contract} {self.commission}"

if __name__ == "__main__":
    # Billie
    billie_contract = Contract("salary", 4000)
    billie_commission = Commission("bonus", 0)
    billie = Employee("Billie", billie_contract, billie_commission)
    print(billie)

    # Charlie
    charlie_contract = Contract("hourly", 100, 25)
    charlie_commission = Commission("bonus", 0)
    charlie = Employee("Charlie", charlie_contract, charlie_commission)
    print(charlie)

    # Renee
    renee_contract = Contract("salary", 3000)
    renee_commission = Commission("contract", 200, 4)
    renee = Employee("Renee", renee_contract, renee_commission)
    print(renee)

    # Jan
    jan_contract = Contract("hourly", 150, 25)
    jan_commission = Commission("contract", 220, 3)
    jan = Employee("Jan", jan_contract, jan_commission)
    print(jan)

    # Robbie
    robbie_contract = Contract("salary", 2000)
    robbie_commission = Commission("bonus", 1500)
    robbie = Employee("Robbie", robbie_contract, robbie_commission)
    print(robbie)
