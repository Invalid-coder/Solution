"""
Background story:

Imagine, one person is going to invest X $. There are two options:
    • put money on the deposit at any well-known bank and have r % annual return which equals to the interest rate in that country.
    • lend money to a new growing business and have R % annual return (R>r).
Second option brings higher return but involves taking some risk in case of business bankruptcy.

After investigating information about the start-up business and its founders,
the person has figured out that default of that growing company is very unlikely,
so it's really a good opportunity to make such investment to have extra return comparing to the market interest rate.
So, the second option has been chosen.

Investment details:

    1. Interest rate is R % per year.
    2. A borrower should return his debt as fixed payment each month. Monthly payment doesn't
    change each month and represents the sum of two components: part of initial principal and
    interest amount.
    3. Interest amount is calculated on the outstanding principal amount.
    4. Investment duration is N years (it means last refund payment should be done in N years
    after making the investment)
The task:

Develop an application that takes: Agreement date, Calculation date, X, R and N as input data and
calculates Sum of all future interest payments.

Task details:

    • Payments are expected in each 30 days.
    • Calculation date is any date (between Agreement date and date of last refund payment) for
    which user want to make calculation. Code requirements/restrictions:
    • You can use any programming language you familiar with (but APL/C# is a plus)
    • Code must follow the principles of maintainability or SOLID (if an object-oriented language
    is chosen).
    • There should be well defined single-entry point in the code that takes input argument and
    returns the result.
    • Requesting input from the user and business calculations should be structurally separated in
    the code.
    • Business oriented classes or methods must be covered by unit tests.
    • The final solution should be pushed to GitHub repository.
"""

import datetime


class Solution:
    def __init__(self, X, R, N):
        """
          Solution initializer

          :param int X: Investment
          :param int R: Interest rate
          :param int N: Amount of investment years
        """

        self.X = X
        self.R = R
        self.N = N


    def find_sum(self, date1, date2):
        """
            This function finds the sum of all future interest payments.

            Parameters:
                datetime date1: Agreement date
                datetime date2: Calculation date

            Variables:
                float Rm: Monthly interest rate
                date
                int months: Amount of months in N years
                float P: Monthly payment amount
            Returns:
                float: Sum of all future interest payments.

        """

        Rm = self.R / (100 * 12)
        days = date2 - date1
        months = days.days // 30
        P = self.X * Rm / (1 - (1 + Rm) ** (-months))

        return P * months - self.X


def main():
    X = int(input("X = "))
    R = int(input("R = "))
    N = int(input("N = "))
    agreement_date = input("Agreement date (in DD/MM/YYYY) ")
    date1 = datetime.datetime.strptime(agreement_date, "%d/%m/%Y").date()
    calculation_date = input("Calculation date (in DD/MM/YYYY) ")
    date2 = datetime.datetime.strptime(calculation_date, "%d/%m/%Y").date()
    s = Solution(X, R, N)
    print(s.find_sum(date1, date2))


def test():
    X = 20000
    R = 12
    N = 3
    date1 = datetime.datetime.strptime('01/12/2000', "%d/%m/%Y").date()
    date2 = datetime.datetime.strptime('01/10/2003', "%d/%m/%Y").date()
    s = Solution(X, R, N)
    print(s.find_sum(date1, date2))


if __name__ == '__main__':
    main()
