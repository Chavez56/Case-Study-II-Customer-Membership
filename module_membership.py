from tabulate import tabulate

class Membership:
    """
    A class for system of self-service cashier.
    
    Attributes
    ----------
    user_data (dict):
        collection of username and its membership
    
    username (str):
        input name of user

    Methods
    -------
    show_benefit():
        Function to display all membership benefit (table form)

    show_requirements():
        Function to display all requirements to subscribe membership (table form)

    predict_membership(monthly_expense, monthly_income):
        Function to predict membership based on euclidean distance

    show_membership(username):
        Function to show membership based on username

    calculate_price(membership, list_harga_barang):
        Function to calculate final price and discount price based on membership
    
    """

    user_data = {'Sumbul':'Platinum',
                 'Ana':'Gold',
                 'Cahya':'Platinum'
                 }

    def __init__(self,username: str):
        self.username = username.title()

    def show_benefit(self):
        """
        Function to display all membership benefit (table form)

        Parameters
        ----------
        None

        Returns
        -------
        None

        """

        headers = ['Membership','Disount','Another Benefit']
        list_membership = ['Platinum','Gold','Silver']
        list_discount = ['15%','10%','8%']
        list_benefit = ['Benefit Silver + Gold + Voucher Liburan + Cashback max. 30%',
                        'Benefit Silver + Voucher Ojek Online',
                        'Voucher Makanan']
        table_content = [[membership,discount,benefit] for membership,discount,benefit in \
                         zip(list_membership,list_discount,list_benefit)]
        print("------------------------------------------------------------------------------------------")
        print(tabulate(table_content,headers, tablefmt="github",colalign=('center','center','center'),stralign=('center')))
        print("------------------------------------------------------------------------------------------")

    def show_requirements(self):
        """
        Function to display all requirements to subscribe membership (table form)

        Parameters
        ----------
        None

        Returns
        -------
        None
        
        """

        headers = ['Membership','Monthly Expense (juta)','Monthly Income (juta)']
        list_membership = ['Platinum','Gold','Silver']
        list_monthly_expense = [8,6,5]
        list_monthly_income = [15,10,7]
        table_content = [[membership,monthly_expense,monthly_income] for membership,monthly_expense,monthly_income in \
                         zip(list_membership,list_monthly_expense,list_monthly_income)]
        print("---------------------------------------------------------------------")
        print(tabulate(table_content,headers, tablefmt="github",colalign=('center','center','center'),numalign=('center')))
        print("---------------------------------------------------------------------")

    def predict_membership(self,monthly_expense: float|int, monthly_income: float|int):
        """
        Function to predict membership based on euclidean distance

        Parameters
        ----------
        monthly_expense (float/int): total cost for shopping per month
        monthly_income (float/int): total earning per month

        Returns
        -------
        None
        
        """

        self.monthly_expense = monthly_expense
        self.monthly_income = monthly_income

        list_monthly_expense = [8,6,5]
        list_monthly_income = [15,10,7]
        list_membership = ['Platinum','Gold','Silver']

        distance = []
        dict_membership = {}

        for i in range(0,len(list(zip(list_monthly_expense,list_monthly_income)))):
            distance_1 = (self.monthly_expense - list_monthly_expense[i])**2
            distance_2 = (self.monthly_income - list_monthly_income[i])**2
            distance.append(round((distance_1 + distance_2)**(1/2),2))

        for i in range(0,len(list(zip(distance,list_membership)))):
            dict_membership.update({list_membership[i]:distance[i]})

        print(f"Hasil perhitungan Euclidean Distance dari user {self.username} adalah {dict_membership}")

        tier_membership = [key for index,(key,value) in enumerate(dict_membership.items()) if value<=min(list(dict_membership.values()))]

        print()
        print(f"'{tier_membership[0]}'")
        
        Membership.user_data.update({self.username:f"{tier_membership[0]}"})

    def show_membership(self,username: str) -> str:
        """
        Function to show membership based on username

        Parameters
        ----------
        username (str): input username

        Returns
        -------
        None
        
        """

        self.username = username

        if self.username in list(Membership.user_data.keys()):
            return f"{str(Membership.user_data[self.username])}"

        else:
            return f"Username tidak ditemukan"

    def calculate_price(self,membership: str, list_harga_barang: list):
        """
        Function to calculate final price and discount price based on membership

        Parameters
        ----------
        membership (str): input tier membership based on username in user data
        list_harga_barang (list): collection of item price, can be integer/float

        Returns
        -------
        None
        
        """
        
        self.list_harga_barang = list_harga_barang

        self.membership = membership.title()

        list_discount = [15/100,10/100,8/100]

        try:
            if self.username in list(Membership.user_data.keys()):
                
                if self.membership in list(Membership.user_data.values()):
                
                    total_price = sum(self.list_harga_barang)

                    if self.membership == 'Platinum':
                        total_price = total_price - list_discount[0]*total_price
                        print(f"Total belanja yang dibayarkan adalah: Rp {int(total_price)}")

                    elif self.membership == 'Gold':
                        total_price = total_price - list_discount[1]*total_price
                        print(f"Total belanja yang dibayarkan adalah: Rp {int(total_price)}")

                    elif self.membership == 'Silver':
                        total_price = total_price - list_discount[2]*total_price
                        print(f"Total belanja yang dibayarkan adalah: Rp {int(total_price)}")

                elif self.membership not in list(Membership.user_data.values()):
                    print("Membership tidak ditemukan")

            elif self.username not in list(Membership.user_data.keys()):
                print("Username tidak ditemukan")

        except:
            print("Input data anda salah")

        finally:
            print()
            print("Terima kasih!")