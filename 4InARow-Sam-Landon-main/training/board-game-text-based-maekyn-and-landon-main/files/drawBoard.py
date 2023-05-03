from termcolor import colored

from colorama import init
init(autoreset = True)

class Board:
    
    def __init__(self,board):
        self.board = board
        
    def __str__(self):
        
        out = ""
    
        for row in range(6):
            out += " █   █   █   █   █   █   █   █ \n"    
            for column in range(7):
                out+= " █ "
                if self.board[row][column]=="x":
                    out+= colored("█","red")
                elif self.board[row][column]=="o":
                    out+= colored("█","blue")
                else:
                    out+= " "
            out+=" █\n"
            out+=" █   █   █   █   █   █   █   █ \n"
            out+=" █████████████████████████████ \n"
        out+= " █                           █ \n"
        
        return out