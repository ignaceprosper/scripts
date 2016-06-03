#!/usr/bin/env python
#

DNASeq = 'ATGAAC'

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





