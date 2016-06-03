#!/usr/bin/env python
#

#DNASeq = 'ATGAAC'
DNASeq = raw_input( "Please enter a DNA sequence : " )
DNASeq = DNASeq.upper() # converts to upper case
DNASeq = DNASeq.replace(" ","") #removes spaces


print( 'Sequence : ' + DNASeq )
print('Cagri is a world champion of programming')

SeqLength = float( len( DNASeq ) )

print( 'Length is ' + str( SeqLength ) )

NumberA = DNASeq.count('A')
NumberC = DNASeq.count('C')
NumberG = DNASeq.count('G')
NumberT = DNASeq.count('T')

print('A content : ' + str( NumberA / SeqLength ) )
print('C content : ' + str( NumberC / SeqLength ) )
print('G content : ' + str( NumberG / SeqLength ) )
print('T content : ' + str( NumberT / SeqLength ) )





