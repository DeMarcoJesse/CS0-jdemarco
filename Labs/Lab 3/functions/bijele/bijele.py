ls
'''
Name: Jesse DeMarco
Date: 03/03/2026
Program Description: Kattis problem bijele:
https://open.kattis.com/problems/bijele
Algorithm Steps:
    Input 6 numbers separated by a space
    Set varibles for # pieces there are supposed to be
    Write 6 line, one for each set of pieces, 
        taking the difference between actual pieces and pieces required
'''

def solution(dif1, dif2, dif3, dif4, dif5, dif6):
    print(dif1, dif2, dif3, dif4, dif5, dif6)


king, queen, rooks, bishops, knights, pawns = map(int, input().split())

req_king = 1
req_queen = 1
req_rooks = 2
req_bishops = 2
req_knights = 2
req_pawns = 8

# FIXMEs 3,4 make varibles for remaining pieces (2 knights, 8 pawns)

dif1 = req_king- king
dif2 = req_queen-queen
dif3 = req_rooks-rooks
dif4 = req_bishops-bishops
dif5 = req_knights - knights
dif6 = req_pawns - pawns


solution(dif1, dif2, dif3, dif4, dif5, dif6)



#FIXMEs 5,6: make dif5 and dif6 

#FIXME 7: call solution function passing proper parameters