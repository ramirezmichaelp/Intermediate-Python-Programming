#michael phillip Ramirez
from lab03 import power
from lab03 import integerDivision
from lab03 import collectVowels
from lab03 import reverseString
from lab03 import removeSubString


def test_power_base_cases():
    assert power(2,0)==1
    assert power(66,0)==1
    assert power(128,0)==1

def test_power_zero_computation_property():
    assert power(0,10)==0
    assert power(0,2)==0
    assert power(0,4)==0
    
def test_power_non_zero_computation():
    assert power(2,5)==2**5
    assert power(7,7)==7**7
    assert power(100,7)==100**7
    assert power(2,4)==2**4

    
    
    
    

def test_base_case_integerDivision():   
    assert integerDivision(1,2) ==0
    assert integerDivision(9,10)==0
    assert integerDivision(75,76)==0
 

def test_integerDivision_zero_computation_property():
    assert integerDivision(0,4)==0
    assert integerDivision(0,66)==0
    assert integerDivision(0,125)==0

    
def test_integerDivison_non_zero_computation():
    assert integerDivision(75,4)==75//4
    assert integerDivision(125,5)==125//5
    
    

    
    

def test_collectVowels_base_cases(): 
    assert collectVowels("")== []
    
def test_collectVowels_list_ouput_empty():
    assert collectVowels("123456 7 bcd")== []
    assert collectVowels("B c d f g k")== []
    assert collectVowels("BBBBBBBBBBBB")== []
    assert collectVowels("7542   25")==[]
      
    
def test_collectVowels_list_ouput_non_empty():
    assert collectVowels("This Is A Sentence")== ['i', 'I', 'A', 'e', 'e', 'e']
    assert collectVowels("abc123ABC")== ["a","A"]
    assert collectVowels("abcdeFE")== ["a","e","E"]
    assert collectVowels("In the night,dance")==["I","e","i","a","e"]    
    
    
 



def test_base_cases_reserseString():
    assert reverseString("") == ""
        
def test_reverseString_string_no_mutation():
    assert reverseString("racecar")=="racecar"
    assert reverseString("111")=="111"
    assert reverseString("aba")=="aba"
    assert reverseString("T")=="T"
    
    
def test_reverseString_string_mutuations():
    assert reverseString("012345 6 78 9")=="9 87 6 543210"
    assert reverseString("CMPSC9") == "9CSPMC"
    assert reverseString("abcdf") == "fdcba"
    assert reverseString(" king ") == " gnik "
    


def test_base_cases_removeSubString_(): 
    assert removeSubString("abc","")=="abc"
    assert removeSubString("1","01")=="1"
    assert removeSubString("111","1111")=="111"
    
    
def test_removeSubString_string_mutuations():
    assert removeSubString("kiss me", " ")=="kissme"
    assert removeSubString("4565456545", "45")=="6565"
    
def test_removeSubstring_string_no_mutation():
    assert removeSubString("42423522", "21")=="42423522"
    assert removeSubString("tiberius", "re")=="tiberius"    
       
    