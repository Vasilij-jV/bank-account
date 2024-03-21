# -*- config: utf8 -*-

import threading


class BankAccount:

    def __init__(self):
        self.account_balance = 0
        self.lock = threading.Lock()

    def account_replenishment(self, amount):
        with self.lock:
            self.account_balance += amount
            print(f'Deposited {amount}, new balance is {self.account_balance}')

    def account_withdrawal(self, amount):
        with self.lock:
            if self.account_balance >= amount:
                self.account_balance -= amount
                print(f"Withdrew {amount}, new balance is {self.account_balance}")
            else:
                print("Insufficient funds")


def replenishment_of_accounts(account, amount):
    for _ in range(30):
        account.account_replenishment(amount)


def withdrawal_from_accounts(account, amount):
    for _ in range(30):
        account.account_withdrawal(amount)


example_account = BankAccount()

replenishment_thread = threading.Thread(target=replenishment_of_accounts, args=(example_account, 100))
withdrawal_thread = threading.Thread(target=withdrawal_from_accounts, args=(example_account, 150))

replenishment_thread.start()
withdrawal_thread.start()

replenishment_thread.join()
withdrawal_thread.join()

