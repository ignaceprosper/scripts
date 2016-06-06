#!/usr/bin/env python
# env va chercher python ou qu'il se trouve

DNASeq = 'ATGAACaTcacacga GacatcA CtcaTCaTCAcGcGcA'
#DNASeq = raw_input( "Please enter a DNA sequence : " )
DNASeq = DNASeq.replace(" ","")
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

print('A content : {:.2}'.format( NumberA / SeqLength ) )
print('C content : {:.2}'.format( NumberC / SeqLength ) )
print('G content : {:.2}'.format( NumberG / SeqLength ) )
print('T content : {:.2}'.format( NumberT / SeqLength ) )

TotalStrong = NumberG + NumberC
TotalWeak = NumberA + NumberT

if SeqLength <= 14:
	MeltTemp = ( 4 * TotalStrong ) + ( 2 * TotalWeak )
else:
	MeltTemp = 64.9 + 41 * (TotalStrong - 16.4) / SeqLength

print( 'Melting temperature : {}'.format( MeltTemp ) )

