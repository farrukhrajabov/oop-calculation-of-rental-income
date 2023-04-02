class RentalProperty():
    def __init__(self, house_price, rent_monthly, taxes, mortgage, maintaince_costs, hoa, downpayment, closing_costs, other_costs):
        self.house_price = house_price
        self.rent_monthly = rent_monthly
        self.taxes = taxes
        self.mortgage = mortgage
        self.maintaince_costs = maintaince_costs
        self.hoa = hoa
        self.downpayment = downpayment
        self.closing_costs = closing_costs
        self.other_costs = other_costs
    # Rent income
    def incomeRent(self):
        return self.rent_monthly + 0
    
    # Creating a function to return the sum of the monthly expenses 
    def expensesMonthly(self):
        return self.taxes + self.mortgage + self.maintaince_costs + self.hoa 
    
    # Creating a function to return the sum of the initial investments
    def investmentsInitial(self):
        return  self.downpayment + self.closing_costs + self.other_costs 

    # Calculating ROI   
    def calculateRoi(self):
        cash_flow_monthly = self.incomeRent() - self.expensesMonthly()
        print("\nMonthly cashflow amount is: ", cash_flow_monthly)
        cash_flow_annually = cash_flow_monthly * 12
        print("\nThe annual cashflow amount is: ", cash_flow_annually)
        investments_net = self.investmentsInitial()
        print("The initial investment amount is: ", investments_net)
        roi = (cash_flow_annually / investments_net) * 100
        return roi
           
# Inputs from users
house_price =float(input("What is the price the house that you purchased? \n ")) 
rent_monthly = float(input("\nEnter the amount of your monthly rental income:\n ")) 
taxes = float(input("\nWhat is your property tax amount monthly?\n "))
mortgage = float(input("\nWhat is your monthly mortgage amount?\n "))
maintaince_costs = float(input("\nEnter your monthly maintaince costs:\n "))
other_costs = float(input("\nEnter your monthly any other costs:\n "))
hoa = float(input("\nEnter your hoa fee:\n "))
downpayment = float(input("\nEnter your downpayment amount:\n "))
closing_costs = float(input("\nEnter your closing costs:\n "))
other_costs = float(input("\nEnter any other costs:\n "))

property_rental = RentalProperty(house_price, rent_monthly, taxes, mortgage, maintaince_costs, hoa, downpayment, closing_costs, other_costs)
roi_rental = property_rental.calculateRoi()

print(f"\nThe property ROI is: {roi_rental} % ")








    






         
          


