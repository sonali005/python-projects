"""_summary_
Author: MAK
Date: 31st Jan
Version: 1
Purpose: This program is aimed to provide areas of different
geometric shapes

"""


piValue= 3.14

def circle_area(radius):
    """
    _summary_

    Args:
        radius (_int_): _Variable_

    Returns:
        _type_: __int__
        
    """
    return piValue * radius ** 2
  
  
def pentagon(radius):
      return piValue * radius

#my main function starts below
def main():
      '''  This is a multiline comment structure
      I am right now in main() function'''
      area = circle_area(10)
      print(area)
      print(__doc__)
      print(circle_area.__doc__)
      
      
main()
