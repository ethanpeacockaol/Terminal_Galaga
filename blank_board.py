# TODO: frame should  have 
# __
#|    at left corner top

#                          __   
#     at right corner top    |

# |       at bottom left corner
#  ---

#         at bottom right corner      | 
#                                  ---



# TODO: add todos to blank_board this should create a board  of ~ pixels padded by the todo in question and when the window is resized adjust frame



import os

rowz, colz = os.popen('stty size', 'r').read().split()
rows = int(rowz)
cols = int(colz)

print(rows, cols)

import numpy as np

x = np.zeros((rows, cols))


# TODO: add quick print from gemini_python NumbersGuessingGame main.py before i delete it
