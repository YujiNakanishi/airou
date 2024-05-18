import struct
import sys
import math


"""
/*****************************/
setString
/*****************************/
Type : function
Process : remove "\n", "\t" and " " from string.
Input : original_str
	original_str -> <str> string
Output : <str>
"""
def setString(original_str):
	original_str = original_str.replace("\n", "")
	original_str = original_str.replace("\t", "")
	original_str = original_str.replace("\x00", "")
	return original_str.replace(" ", "")


"""
/*****************************/
bwrite
/*****************************/
Type : function
Process : write string by binary format.
Input : b, S, file
	b -> <int> number of byte.
	S -> <str>
	file -> <file class>
Output : None
"""
def bwrite(b, S, file):
	for s in S:
		file.write(struct.pack("c", s.encode()))
	file.write(struct.pack("x"*(b-len(S))))

"""
/*****************************/
forceASCII
/*****************************/
Type : function
Process : replace non ASCII characters to "x".
Input : S
	S -> <str>
Output : <str>
"""
def forceASCII(S):
	S2 = ""
	for s in S:
		if ord(s) <= 127:
			S2 += s
		else:
			S2 += "x"
	return S2

"""
/*****************************/
IDString
/*****************************/
Type : function
Process : create ID string from number like 000num.
Input : num, ids
	num -> <int> ID number
	length -> <int> length of ID
Output : <str>
"""
def IDString(num, length):

	if num == 0:
		idstr = "0"*length

	else:
		if  math.floor(math.log10(num))+1 > length:
			print("Error@Assistant.IDSTR")
			print("ids should be larger more")
			sys.exit()
		else:
			idstr = "0"*(length-math.floor(math.log10(num))-1)+str(num)

	return idstr