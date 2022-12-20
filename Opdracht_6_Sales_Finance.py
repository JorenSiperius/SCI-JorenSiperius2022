## Eerst numpy en numpy_financial downloaden (pip install)
# Numpy toevoegen
import numpy_financial as npf
import numpy as np

# De Present Value van een Cash Flow berekenen
def present_value(cash_flow, discount_rate):
  return cash_flow / (1 + discount_rate)

# De future value van de cashflow berekenen
def future_value(cash_flow, discount_rate):
  return cash_flow * (1 + discount_rate)

# Functie dat de net present value van een serie cash flows berekent
def net_present_value(cash_flows, discount_rate):
  present_values = [present_value(cf, discount_rate) for cf in cash_flows]
  return np.sum(present_values)

# Functie dat en internal rate of return berekent van een serie cash flows
def internal_rate_of_return(cash_flows):
  return npf.irr(cash_flows)

# Definieer een functie die de verdiende rente op een cashflow berekent
def interest(principal, cash_flow):
  return cash_flow - principal

# Definieer een lijst met cashflows
cash_flows = [100, 200, 300]

# Definieer een kortingspercentage
discount_rate = 0.1

# Definieer een startpunt
principal = 1000

# Bereken de contante waarde van elke cashflow
present_values = [present_value(cf, discount_rate) for cf in cash_flows]

# Bereken de toekomstige waarde van elke cashflow
future_values = [future_value(cf, discount_rate) for cf in cash_flows]

# Bereken de netto contante waarde
npv = net_present_value(cash_flows, discount_rate)

# Bereken het interne rendement
irr = internal_rate_of_return(cash_flows)

# Bereken de verdiende rente voor elke cashflow
interests = [interest(principal, cf) for cf in cash_flows]

# Print
print("Present values:", present_values)
print("Future values:", future_values)
print("Net present value:", npv)
print("Internal rate of return:", irr)
print("Interests:", interests)


