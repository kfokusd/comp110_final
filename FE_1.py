import math
import matplotlib.pyplot as pp

# Function: process_expenses()
# - One parameter, filename (csv format)
# - This function returns a 2-items tuple: 1st item is a dictionary, and 2nd item is a dictionary of dictionary
# - 1st Dictionary:
# - >>Read the csv file and create a dictionary with key of the "Category" field in the csv file
# - >>The values of the dictionary is the total "Amount" for such "Category"
# - 2nd Dictionary: (Dictionary of a Dictionary)
# - >>First level of Dictionary: Key is "Properties", and Values is a "2nd level dictionary"
# - >>2nd level dictionary: Key is "Category", and Values is the total "Amount" for such "Category"
#
def process_expenses(filename):
    # TODO: Implement the function
# End of process_expenses()


##
# Please do NOT change the following code.
# You MUST implement process_expenses() in order to run this code without error
##
(dict, dictpropcat) = process_expenses("FE_1.csv")
print("\n\nBased on Categories")
for i in dict:
    print("{:30s}: ${:.2f}".format(i, dict[i]))


print("\n\n\nBased on Properties and Categories")
for i in dictpropcat:
    print([i])
    nSum = 0.0
    for k in dictpropcat[i]:
        print("    {:30s}: ${:.2f}".format(k, dictpropcat[i][k]))
        nSum += dictpropcat[i][k]
    print("    {:>30s}: ${:.2f}".format("TOTAL:", nSum))


pp.bar( dict.keys(), dict.values() )
pp.xticks(rotation=45)
pp.show()


# Expected Output:
#Based on Categories
#Fee                           : $1852.00
#Appliance Supplies            : $517.33
#Utilities                     : $4397.92
#HOA                           : $30146.00
#Insurance                     : $2959.86
#Permits & License             : $472.00
#Legal & Prof. Fees            : $1938.00
#Cleaning & Maintenance        : $1176.87
#Repairs - Plumbing            : $3692.10
#Property Taxes                : $19695.89
#Refund (Deposit)              : $4251.27
#Repairs - Misc                : $1802.47
#Advertising                   : $219.99
#Repairs - A/C                 : $290.00
#Return of Capital             : $25000.00
#Remodeling                    : $333.26
#
#
#
#Based on Properties and Categories
#['DelMar']
#    Fee                           : $1852.00
#    HOA                           : $3310.00
#    Permits & License             : $59.00
#    Insurance                     : $687.86
#    Utilities                     : $224.69
#    Property Taxes                : $1584.48
#    Repairs - Plumbing            : $250.00
#    Repairs - Misc                : $115.00
#                            TOTAL:: $8083.03
#['Alva']
#    Appliance Supplies            : $84.28
#    Utilities                     : $1534.15
#    HOA                           : $3240.00
#    Insurance                     : $241.00
#    Legal & Prof. Fees            : $1658.00
#    Property Taxes                : $1716.10
#    Return of Capital             : $3125.00
#    Repairs - Plumbing            : $260.00
#                            TOTAL:: $11858.53
#['Alta']
#    HOA                           : $2986.00
#    Permits & License             : $59.00
#    Appliance Supplies            : $4.30
#    Property Taxes                : $1523.72
#    Insurance                     : $334.00
#    Return of Capital             : $3125.00
#    Repairs - Misc                : $130.29
#                            TOTAL:: $8162.31
#['TorreyHighland']
#    HOA                           : $2980.00
#    Insurance                     : $276.00
#    Permits & License             : $59.00
#    Utilities                     : $1123.79
#    Appliance Supplies            : $397.53
#    Property Taxes                : $3026.80
#    Cleaning & Maintenance        : $6.44
#    Legal & Prof. Fees            : $245.00
#    Refund (Deposit)              : $1942.74
#    Repairs - Misc                : $1091.91
#    Return of Capital             : $3125.00
#    Repairs - Plumbing            : $1161.27
#                            TOTAL:: $15435.48
#['Campo']
#    HOA                           : $2980.00
#    Insurance                     : $276.00
#    Permits & License             : $59.00
#    Utilities                     : $656.50
#    Repairs - Plumbing            : $481.46
#    Property Taxes                : $3418.01
#    Advertising                   : $219.99
#    Appliance Supplies            : $31.22
#    Repairs - Misc                : $5.27
#    Return of Capital             : $3125.00
#    Refund (Deposit)              : $2308.53
#    Remodeling                    : $333.26
#                            TOTAL:: $13894.24
#['Poway']
#    HOA                           : $2980.00
#    Insurance                     : $276.00
#    Permits & License             : $59.00
#    Utilities                     : $858.79
#    Property Taxes                : $3408.55
#    Repairs - Misc                : $460.00
#    Return of Capital             : $3125.00
#    Legal & Prof. Fees            : $35.00
#    Cleaning & Maintenance        : $325.43
#                            TOTAL:: $11527.77
#['SpringBrook']
#    HOA                           : $3655.00
#    Permits & License             : $59.00
#    Cleaning & Maintenance        : $845.00
#    Property Taxes                : $1754.37
#    Repairs - Plumbing            : $60.00
#    Return of Capital             : $3125.00
#                            TOTAL:: $9498.37
#['SabreSpring']
#    HOA                           : $3655.00
#    Insurance                     : $595.00
#    Permits & License             : $59.00
#    Property Taxes                : $1616.03
#    Repairs - Plumbing            : $394.38
#    Repairs - A/C                 : $290.00
#    Return of Capital             : $3125.00
#                            TOTAL:: $9734.41
#['Heatherton']
#    HOA                           : $4360.00
#    Insurance                     : $274.00
#    Permits & License             : $59.00
#    Property Taxes                : $1647.83
#    Return of Capital             : $3125.00
#    Repairs - Plumbing            : $1084.99
#                            TOTAL:: $10550.82