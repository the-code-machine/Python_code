# IT IS A COLLECTION OF NON REPEATING ELEMENTS
#CHARACTERISTICS
#UNORDERED
#UNINDEXED
#NON-REPEATING ELEMENTS
#UNMUTABLE


#CREATION
Set = {1,3,4,5,"TRUE",True}

#PRINTING THE SET
print(Set)
#print(Set[2]) # throw an error

#SET DOES NOT CONATIN ANY MUTABLE DATA TYPE INSIDE 
#ADDING LIST 
Set_01={1,5,4,6,[1,4,5,]}# throw error
#print(Set_01)
#ADDING DICTIONARY
Set_02={1,4,7,{4:5}}
#print(Set_02)# throw error
#ADDING TUPPLE TO SET
Set_03={1,4,7,8,(1,4,5)}# not throw error tupple is unmutable
print(Set_03)