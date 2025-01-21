'''
Author: Aidan Kiser
Version: 5 November 2024
'''

import random
import traceback 
import json

def divide(v1, v2):
   # if v1.isnumeric() and v2.isnumeric():
   #    v1 = float(v1)
   #    # print('Before conversion:', v2)
   #    v2 = float(v2) 
   #    # print('After conversion:', v2)
   #    if v2 != 0:
   #       return v1 / v2 
   #    else: 
   #       # pass 
   #       return "Division by zero error."
   # else: 
   #    return "One of the input is invalid."

   if v2 == 0:
      raise ValueError("Can't divide by 0 homie")
   return v1 / v2

def fuzzValues(val1, val2):
   if not isinstance(val1, (int, float)) or not isinstance(val2, (int, float)):
      raise TypeError("That input type won't work homie")

   if abs(val1) == float('inf') or abs(val2) == float('inf'):
      raise OverflowError("Overflow or underflow error fam")
   
   res = divide(val1, val2)
   if isinstance(res, float) and round(res, 5) != res:
      raise ArithmeticError("Precision was lost, man")
   return res  

def simpleFuzzer(): 
   error_values = [
      # Error 1: Division by 0 (Line 23)
      (1, 0),

      # Error 2: Invalid input type (Line 28)
      ("word", 5),

      # Error 3: Overflow or underflow (Line 31)
      (float('inf'), 2),

      # Error 4: Loss of precision (Line 35)
      (0.1, 3),

      # Error 5: Rounding error
      (2, 6),
      
      # Error 6: Exception wasn't handled
      (None, 20),

      # Error 7: Invalid operation
      (1, "aye"),

      # Error 8:
      ("❤️ 💔 💌 💕 💞 💓 💗 💖 💘 💝 💟 💜 💛 💚 💙", 9),

      # Error 9:
      ("¯\\_(ツ)_/¯", 21),

      # Error 10:
      ("⒯⒣⒠ ⒬⒰⒤⒞⒦ ⒝⒭⒪⒲⒩ ⒡⒪⒳ ⒥⒰⒨⒫⒮ ⒪⒱⒠⒭ ⒯⒣⒠ ⒧⒜⒵⒴ ⒟⒪⒢", 28)
   ]
   
   for val1, val2 in error_values:
      try:
         fuzzValues(val1, val2)
      except Exception as exc:
         traceback.print_exc();



if __name__=='__main__':
    simpleFuzzer()
