#Michael Ramirez

from Stack import Stack
from lab04 import solveMaze

def test_unilateral_success():
    north = [
['+','+','+','+','+','+'],
['+',' ','G',' ','+ ',' '],
['+',' ',' ',' ','+','+'],
['+',' ',' ','+',' ','+'],
['+',' ',' ',' ',' ','+'],
['+','+','+','+','+','+'] ]
    assert solveMaze(north,4,2)==True
    assert north==[
['+','+','+','+','+','+'],
['+',' ','G',' ','+ ',' '],
['+',' ',3  ,' ','+','+'],
['+',' ',2  ,'+',' ','+'],
['+',' ',1  ,' ',' ','+'],
['+','+','+','+','+','+'] ]
    east = [
['+','+','+','+','+','+'],
['+','+','+','+','+',' '],
['+',' ',' ',' ','G','+'],
['+',' ',' ',' ',' ','+'],
['+',' ',' ',' ',' ','+'],
['+','+','+','+','+','+'] ]
        
    assert solveMaze(east,2,1)==True
    assert east == [
['+','+','+','+','+','+'],
['+','+','+','+','+',' '],
['+',  1,  2,  3,'G','+'],
['+',' ',' ',' ',' ','+'],
['+',' ',' ',' ',' ','+'],
['+','+','+','+','+','+'] ]
    south = [
['+','+','+','+','+','+'],
['+',' ','+',' ','+ ',' '],
['+',' ','+',' ','+','+'],
['+',' ','+',' ','+','+'],
['+',' ','+','G','+','+'],
['+','+','+','+','+','+'] ]
    assert solveMaze(south,1,3)==True
    assert south == [
['+','+','+','+','+','+'],
['+',' ','+',  1,'+ ',' '],
['+',' ','+',  2,'+','+'],
['+',' ','+',  3,'+','+'],
['+',' ','+','G','+','+'],
['+','+','+','+','+','+'] ]
    west = [
['+','+','+','+','+','+'],
['+','G',' ',' ',' ','+'],
['+','+','+','+','+','+'] ]
    assert solveMaze(west,1,4)==True
    assert west == [
['+','+','+','+','+','+'],
['+','G',  3,  2,  1,'+'],
['+','+','+','+','+','+'] ]
    
def test_180_success():
    maze180A=[
['+','+','+','+','+','+'],
['+','G',' ',' ',' ','+'],
['+','+','+','+','+','+']]
    assert solveMaze(maze180A,1,2)==True
    assert maze180A==[
['+','+','+','+','+','+'],
['+','G',  1,  2,  3,'+'],
['+','+','+','+','+','+']]
    maze180B=[
['+','+','+'],
['+',' ','+'],
['+',' ','+'],
['+',' ','+'],
['+',' ','+'],
['+','G','+'],
['+','+','+']]
    assert solveMaze(maze180B,3,1)==True
    assert maze180B==[
['+','+','+'],
['+',  3,'+'],
['+',  2,'+'],
['+',  1,'+'],
['+',  4,'+'],
['+','G','+'],
['+','+','+']]

def test_no_escape():
    esc_A=[
['+','+','+'],
['+',' ','+'],
['+',' ','+'],
['+',' ','+'],
['+','+','+'],
['+','G','+'],
['+','+','+']]
    assert solveMaze(esc_A,3,1)== False
    assert esc_A==[
['+','+','+'],
['+',  3,'+'],
['+',  2,'+'],
['+',  1,'+'],
['+','+','+'],
['+','G','+'],
['+','+','+']]
    esc_B = [
['+','+','+','+','+','+'],
['+','+','G',' ','+ ',' '],
['+',' ','+',' ','+','+'],
['+',' ',' ','+',' ','+'],
['+',' ',' ',' ','+','+'],
['+','+','+','+','+','+'] ]
    assert solveMaze(esc_B,2,1)==False
    assert esc_B == [
['+','+','+','+','+','+'],
['+','+','G',' ','+ ',' '],
['+',  1,'+',' ','+','+'],
['+',  2,  3,'+',' ','+'],
['+',  6,  4,  5,'+','+'],
['+','+','+','+','+','+'] ]


        
    
    
    