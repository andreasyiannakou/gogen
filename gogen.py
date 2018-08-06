# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 15:17:23 2018

@author: Andreas
"""
#-------------------------IMPORT REQUIRED PACKAGES-----------------------------------#
#used for the neighbours DataFrame
import pandas as pd
#floor used to take the integer part of a division (floor = always round down)
from math import floor

#-------------------------DEFINE FUNCTIONS-----------------------------------#
#print the board as a 5x5 array
def print_board(board):
    for i in range(5):
        print(board[(i*5):(i*5)+5])

#finds the set of all letters next to the letter passed in        
def find_neighbours(neighbours, letter):
    ndn = []
    for key, value in neighbours.iterrows():
        if value['Letter1'] == letter:
            if value['Letter2'] != letter:
                ndn.append(value['Letter2'])
        if value['Letter2'] == letter:
            if value['Letter1'] != letter:
                ndn.append(value['Letter1'])
    ndn = list(set(ndn))
    return ndn  

#populates the board with all the letters which have been assigned a space
def populate_board(board, Letters):
    for l in Letters:
        if l.space >= 0:
            board[l.space] = l.name
    return board

#finds all the spaces on the board which are not populated by a letter yet    
def free_spaces(board):
    free_spaces = []
    for i in range(len(board)):
        if board[i] == '':
            free_spaces.append(i)
    return free_spaces

#populates all the spaces that are free and next to neighbours    
def possible_spaces(letter, Letters, board):
    if letter.row > -1:
        return letter.space
    f_spaces = free_spaces(board)
    p_spaces = []
    for space in f_spaces:
        row = floor(space/5)
        col = space % 5
        for l in Letters:
            if l.name in letter.neighbours:
                if (l.row > -1):
                    if (abs(l.row - row) < 2 and abs(l.col - col) < 2):
                        p_spaces.append(space)
                else:
                   p_spaces.append(space)
    most = max(list(map(p_spaces.count, p_spaces)))
    p_spaces = list(set(filter(lambda x: p_spaces.count(x) == most, p_spaces)))
    return p_spaces
 
#trims the possible spaces by removing all the spaces which would allow all neighbours to be next to the letter               
def trim_spaces(letter, board):
    p_spaces = []
    try:
        s_loop = list(letter.possible_spaces)
    except: 
        s_loop = [letter.possible_spaces]
        
    for space in s_loop:
        ok = 0
        row = floor(space/5)
        col = space % 5
        #if first row
        if row == 0:
            #if first column 
            if col == 0:
                if (board[row * 5 + col + 1] == '' or board[row * 5 + col + 1] in letter.neighbours):
                   ok = ok + 1
                if (board[(row + 1) * 5 + col] == '' or board[(row + 1) * 5 + col] in letter.neighbours):
                    ok = ok + 1
                if (board[(row + 1) * 5 + col + 1] == '' or board[(row + 1) * 5 + col + 1] in letter.neighbours):  
                    ok = ok + 1
            #if last column 
            elif col == 4:
                if (board[row * 5 + col - 1] == '' or board[row * 5 + col - 1] in letter.neighbours):
                   ok = ok + 1
                if (board[(row + 1) * 5 + col] == '' or board[(row + 1) * 5 + col] in letter.neighbours):
                    ok = ok + 1
                if (board[(row + 1) * 5 + col - 1] == '' or board[(row + 1) * 5 + col - 1] in letter.neighbours):  
                    ok = ok + 1
            else:
                if (board[row * 5 + col + 1] == '' or board[row * 5 + col + 1] in letter.neighbours):
                   ok = ok + 1
                if (board[(row + 1) * 5 + col] == '' or board[(row + 1) * 5 + col] in letter.neighbours):
                    ok = ok + 1
                if (board[(row + 1) * 5 + col + 1] == '' or board[(row + 1) * 5 + col + 1] in letter.neighbours):                  
                    ok = ok + 1
                if (board[row * 5 + col - 1] == '' or board[row * 5 + col - 1] in letter.neighbours):
                   ok = ok + 1
                if (board[(row + 1) * 5 + col - 1] == '' or board[(row + 1) * 5 + col - 1] in letter.neighbours):  
                   ok = ok + 1
        #last row
        elif row == 4:
            #if first column 
            if col == 0:
                if (board[row * 5 + col + 1] == '' or board[row * 5 + col + 1] in letter.neighbours):
                   ok = ok + 1
                if (board[(row - 1) * 5 + col] == '' or board[(row - 1) * 5 + col] in letter.neighbours):
                    ok = ok + 1
                if (board[(row - 1) * 5 + col + 1] == '' or board[(row - 1) * 5 + col + 1] in letter.neighbours):  
                    ok = ok + 1
            #if last column
            elif col == 4:
                if (board[row * 5 + col - 1] == '' or board[row * 5 + col - 1] in letter.neighbours):
                   ok = ok + 1
                if (board[(row - 1) * 5 + col] == '' or board[(row - 1) * 5 + col] in letter.neighbours):
                    ok = ok + 1
                if (board[(row - 1) * 5 + col - 1] == '' or board[(row - 1) * 5 + col - 1] in letter.neighbours):
                    ok = ok + 1
            else:
                if (board[row * 5 + col + 1] == '' or board[row * 5 + col + 1] in letter.neighbours):
                   ok = ok + 1
                if (board[(row - 1) * 5 + col] == '' or board[(row - 1) * 5 + col] in letter.neighbours):
                    ok = ok + 1
                if (board[(row - 1) * 5 + col + 1] == '' or board[(row - 1) * 5 + col + 1] in letter.neighbours):  
                    ok = ok + 1
                if (board[row * 5 + col - 1] == '' or board[row * 5 + col - 1] in letter.neighbours):
                   ok = ok + 1
                if (board[(row - 1) * 5 + col - 1] == '' or board[(row - 1) * 5 + col - 1] in letter.neighbours):  
                   ok = ok + 1
        else:
            #if first column 
            if col == 0:
                if (board[row * 5 + col + 1] == '' or board[row * 5 + col + 1] in letter.neighbours):
                   ok = ok + 1
                if (board[(row - 1) * 5 + col] == '' or board[(row - 1) * 5 + col] in letter.neighbours):
                    ok = ok + 1
                if (board[(row - 1) * 5 + col + 1] == '' or board[(row - 1) * 5 + col + 1] in letter.neighbours):  
                    ok = ok + 1
                if (board[(row + 1) * 5 + col] == '' or board[(row + 1) * 5 + col] in letter.neighbours):
                    ok = ok + 1
                if (board[(row + 1) * 5 + col + 1] == '' or board[(row + 1) * 5 + col + 1] in letter.neighbours):  
                    ok = ok + 1
            #if last column
            elif col == 4:
                if (board[row * 5 + col - 1] == '' or board[row * 5 + col - 1] in letter.neighbours):
                   ok = ok + 1
                if (board[(row - 1) * 5 + col] == '' or board[(row - 1) * 5 + col] in letter.neighbours):
                    ok = ok + 1
                if (board[(row - 1) * 5 + col - 1] == '' or board[(row - 1) * 5 + col - 1] in letter.neighbours):  
                    ok = ok + 1
                if (board[(row + 1) * 5 + col] == '' or board[(row + 1) * 5 + col] in letter.neighbours):
                    ok = ok + 1
                if (board[(row + 1) * 5 + col - 1] == '' or board[(row + 1) * 5 + col - 1] in letter.neighbours):  
                    ok = ok + 1
            else:
                if (board[row * 5 + col - 1] == '' or board[row * 5 + col - 1] in letter.neighbours):
                   ok = ok + 1
                if (board[(row - 1) * 5 + col] == '' or board[(row - 1) * 5 + col] in letter.neighbours):
                    ok = ok + 1
                if (board[(row - 1) * 5 + col - 1] == '' or board[(row - 1) * 5 + col - 1] in letter.neighbours):  
                    ok = ok + 1
                if (board[(row + 1) * 5 + col] == '' or board[(row + 1) * 5 + col] in letter.neighbours):
                    ok = ok + 1
                if (board[(row + 1) * 5 + col - 1] == '' or board[(row + 1) * 5 + col - 1] in letter.neighbours):  
                    ok = ok + 1
                if (board[row * 5 + col + 1] == '' or board[row * 5 + col + 1] in letter.neighbours):
                    ok = ok + 1
                if (board[(row + 1) * 5 + col + 1] == '' or board[(row + 1) * 5 + col + 1] in letter.neighbours):  
                    ok = ok + 1
                if (board[(row - 1) * 5 + col + 1] == '' or board[(row - 1) * 5 + col - 1] in letter.neighbours):  
                    ok = ok + 1
        #checks the number of usable adjoining spaces is greater than or equal to the number of neighbours             
        if (ok >= letter.ns):
            p_spaces.append(space)
    return p_spaces
        
#-------------------------DEFINE LETTER CLASS-----------------------------------#
class Letter:
    #Initialise the letter object
    def __init__(self, name):
        self.name = name
        self.row = -1
        self.col = -1
        self.space = -1
        self.neighbours = []
        self.ns = -1
        self.possible_spaces = []
    
    #Assign the letter to a space
    def assign_space(self, row, col):
        self.row = row
        self.col = col
        self.space = (row * 5) + col

    #Populate the list of neighbours this letter has    
    def populate_neighbours(self, neighbours):
        self.neighbours = find_neighbours(neighbours, self.name)
        self.ns = len(self.neighbours)
    
    #Populate a list of the squares the letter could go in    
    def populate_possible_spaces(self, Letters, board):
        self.possible_spaces = possible_spaces(self, Letters, board) 
    
    # remove items from the list if they do not have enough space for their neighbours to sit next to them    
    def remove_possible_spaces(self, board):
        self.possible_spaces = trim_spaces(self, board)
        if len(self.possible_spaces) == 1:
            r = self.possible_spaces[0]
            self.row = floor(r/5)
            self.col = r % 5
            self.space = (self.row * 5) + self.col
            

#-------------------------CODE-----------------------------------#
#Create the Letter objects        
A = Letter('A')
B = Letter('B')
C = Letter('C')
D = Letter('D')
E = Letter('E')
F = Letter('F')
G = Letter('G')
H = Letter('H')
I = Letter('I')
J = Letter('J')
K = Letter('K')
L = Letter('L')
M = Letter('M')
N = Letter('N')
O = Letter('O')
P = Letter('P')
Q = Letter('Q')
R = Letter('R')
S = Letter('S')
T = Letter('T')
U = Letter('U')
V = Letter('V')
W = Letter('W')
X = Letter('X')
Y = Letter('Y')

#Assign the initial letters their correct locations in the grid, (0, 0) = first row, first column
X.assign_space(0,0)
W.assign_space(0,2)
K.assign_space(0,4)
M.assign_space(2,0)
F.assign_space(2,2)
N.assign_space(2,4)
Q.assign_space(4,0)
Y.assign_space(4,2)
P.assign_space(4,4)

#Populate the words list        
words = ['BOW', 'BOX', 'DOLE', 'FLOAT', 'HALVE', 'JUT', 'LAMB', 'NECK', 'QUALITY', 'SPRING', 'STILE', 'TRICK']

#Set up and populate the neighbours DataDrame
neighbours = pd.DataFrame(columns=['Letter1', 'Letter2'])
for word in words:
    for i in range(len(word)-1):
        neighbours = neighbours.append({'Letter1': word[i], 'Letter2':word[i+1]}, ignore_index=True)

#Initialise the board        
board = ['','','','','','','','','','','','','','','','','','','','','','','','','']

#Put the letter objects into a list, easier to loop through 
Letters = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y]

for l in Letters:
    l.populate_neighbours(neighbours)
    #Print statements used for checking
    #print('Letter: ' + l.name)
    #print(l.ns, l.neighbours)

#remove variables no longer required
del words, word, neighbours
    
#populate the baord with the initial letters
board = populate_board(board, Letters)    
    
# loop through 16 times as initally there are 16 free spaces in the grid, so will take at most 16 loops
for i in range(4):
    for l in Letters:
            if (l.space == -1):
                l.populate_possible_spaces(Letters, board)
                #Print statements used for checking
                #print('Letter: ' + l.name)
                #print(l.possible_spaces)
                l.remove_possible_spaces(board)
                #Print statement used for checking
                #print(l.possible_spaces)
                #populate the baord with the letters
                board = populate_board(board, Letters)  

#remove i as no longer required
del i
                
#Print the final board
print_board(board)
