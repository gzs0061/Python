__author__ = 'Ella Seaman'
# Program that counts from one digit up to another digit
# Input num, high
# Output num
#

# Function Boolean valid (String num)
#   Declare Boolean num
#   val_num = is num a valid integer?
#   Return val_num
# End Function
def val_num_int(num):
    try:
        val = int(num)
        val_num = True
    except ValueError:
        val_num = False
    return val_num
#
# Module let_count()
#   Declare String num
#   Declare Boolean val_num
#
#   Display "How high do you want to count?"
#   val_num = val_num_int(num)
#   Input num
#   While not val_num:
#        high = input("Please enter an integer")
#        val_high = val_high_int(high)
#        val_num = val_num_int(num)
#    int_num = int(num)
#    Return int_num
# End Function
def lets_count():
    num = input("What digit would you like to count from? ")
    val_num = val_num_int(num)
    while not val_num:
        num = input("Please enter an integer")
        val_num = val_num_int(num)
    int_num = int(num)
    return int_num

#
# Module how_high()
#   Declare String high
#   Declare Boolean val_high
#
#   Display "How high do you want to count?"
#   val_high = val_high_int(high)
#   Input high
#   While not val_high:
#        high = input("Please enter an integer")
#        val_high = val_high_int(high)
#    high_int = int(high)
#    Return high_int
# End Function
def how_high():
    high = input("How high do you want to count? ")
    val_high = val_num_int(high)
    while not val_high:
        high = input("Please enter an integer")
        val_high = val_num_int(high)
    high_int = int(high)
    return high_int


# Module counting(Integer num, Integer high)
#   Declare Integer num
#   Declare Integer high
#
#
#   While num < high:
#       Display num
#       num = num + 1
#   End while
# End Module
def counting(num, high):
    while num < high+1:
        print(num)
        num = num + 1

# Module main()
#   num = lets_count()
#   high = how_high()
#   counting(num, high)
def main():
    num = lets_count()
    high = how_high()
    counting(num, high)

main()









