#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Rafael Silveira rsilveira@inf.ufpel.edu.br
Analisador Sintático
'''
from analisador_lexico import *
import sys 

pilha=[]

def empilha(token):
	global pilha
	pilha.append(token)
	
def desempilha():
	global pilha
	return pilha.pop()
	

def ShowErroSintatico(regra):
	
	global fileb, linhas, erroLexico
	print "ERRO SINTATICO na regra: ",regra
	#print "linha:",linhas
	#print "coluna:",colunas
  

def S_linha(token):
		print "token no s_linha ",token['nome']
		if S(token):
			token = le_token()
			if token['nome']=="+":
				return True
			else:
				return False
				
		else:
			return False
			
		
			
def S(token):   #ADICIONAR O VAZIO
	print "token no s ",token['nome']
	if PRINT(token):
		return True
	else:
		if READ(token):
			return True
		else:
			if VAR(token):
				return True
			else:
				if IF(token):
					return True
				else:
					return False #vazio
		
		
					
def PRINT(token):
	print "token no PRINT ",token['nome']
	if token['nome']=="PRI":
		token = le_token()
		if E0(token):
			token = le_token()
			if token['nome'] =="PTV":
				token = le_token()
				if S(token):
					return True
				else:
					return False

			else:
				return False
		else:
			return False
			
	else:
		return False
		
def READ(token):
	print "token no READ",token['nome']
	if token['nome']=="REA":
		token = le_token()
		if EVIR(token):
			token = le_token()
			if token['nome'] =="PTV":
				token = le_token()
				if S(token):
					return True
				else:
					return False	
			else:
				return False
		else:
			return False	
	else:
		return False
		
def VAR(token):
	print "token no VAR",token['nome']
	if token['nome']=="VAR":
		token = le_token()
		if token['nome']=="ATR":
			token = le_token()
			if E1(token):
				token = le_token()
				if token['nome']=="PTV":
					token = le_token()
					if S(token):
						return True
					else:
						return False	
				else:
					return False
			else:
				return False
		else:
			return False
	else:
		return False
		
		
		
def E0(token):
	print "token no E0 ",token['nome']
	empilha({'nome':'E0_linha','tipo':'variavel'})
	if E1(token):
		return True
	else:
		return False
		
		
def E0_linha(token):
	print "token no E0_linha ",token['nome']
	E0_ast(token)
		
def E0_ast(token):
	print "token no E0_ast ",token['nome']
	empilha({'nome':'E0_linha','tipo':'variavel'})
	empilha({'nome':'E1','tipo':'variavel'})
	empilha({'nome':'VAR','tipo':'token'})
	TOP = pilha.pop()
	token = le_token()
		if TOP['nome'] == token['nome']:
			return True
			
		else:
			return False
	
		
def EVIR(token):
	print "token no EVIR ",token['nome']
	empilha({'nome':'EVIR_linha','tipo':'variavel'})
	empilha({'nome':'VIR','tipo':'token'})
	TOP =  pilha.pop()
	token = le_token()
		if TOP['nome'] == token['nome']:
			return True
		else:
			return False
	 
def EVIR_linha(token):
	print "token no EVIR_linha ",token['nome']
	EVIR_ast(token)
	
def EVIR_ast(token):
	
	print "token no EVIR_ast ",token['nome']
	empilha({'nome':'EVIR_linha','tipo':'variavel'})
	empilha({'nome':'VAR','tipo':'token'})
	empilha({'nome':'VIR','tipo':'token'})
	TOP = pilha.pop()
	token = le_token()
		
		if TOP['nome'] == token['nome']:
			TOP = pilha.pop()
			token = le_token()
			
			if TOP['nome'] == token['nome']:
				return True
			else: 
				return False
		else:
			return False
					
def E1(token):
	print "token no E1 ",token['nome']
	empilha({'nome':'E1_linha','tipo':'variavel'})
	E2(token)	
		
		
def E1_linha(token):
	print "token no E1_linha ",token['nome']
	
	E1_ast(token)
	
def E1_ast(token):
	print "token no E1_ast ",token['nome']
	
	empilha({'nome':'E1_linha','tipo':'variavel'})
	empilha({'nome':'E2','tipo':'variavel'})
	empilha({'nome':'EQU','tipo':'token'})
	TOP = pilha.pop()
	token = le_token()
		if TOP['nome'] == token['nome']:
			return True
		else: 
			return False
	
def E2(token):
	print "token no E2 ",token['nome']
	empilha({'nome':'E2_linha','tipo':'variavel'})
	E3(token)
	
		
def E2_linha(token):
	print "token no E2_linha ",token['nome']
	E2_ast(token)
	
def E2_ast(token):
	print "token no E2_ast ",token['nome']
	empilha({'nome':'E1_linha','tipo':'variavel'})
	empilha({'nome':'E2','tipo':'variavel'})
	empilha({'nome':'IMP','tipo':'token'})
	TOP = pilha.pop()
	token = le_token()
		if TOP['nome'] == token['nome']:
			return True
		else: 
			return False
		
def E3(token):
	print "token no E3",token['nome']
	empilha({'nome':'E3_linha','tipo':'variavel'})
	E4(token)	
		
def E3_linha(token):
	print "token no E3_linha",token['nome']
	empilha({'nome':'E3','tipo':'variavel'})
	token = le_token()
		if (token['nome'] == "AND") or (token['nome'] == "OR"): 		
			TOP = pilha.pop()
			token = le_token()
			E3(token)
		else :
			return False 
def E4(token):
	print "token no E4",token['nome']
	empilha({'nome':'E3_linha','tipo':'variavel'})
	if (token['nome'] == "PAE"):
		empilha({'nome':'E4_linha','tipo':'variavel'})
		empilha({'nome':'PAD','tipo':'token'})
		empilha({'nome':'E1','tipo':'variavel'})
			
		
def E4_linha(token):
	print "token no E4_linha",token['nome']
	if token['nome']=="NOT":
		token = le_token()
		if E4_linha(token):
			return True
		else:
			return False
	else:
		return False #VAZIOOO

		
def IF(token):
	print "token no IF ",token['nome']
	if token['nome']=="IF":
		token = le_token()
		if E1(token):
			token = le_token()
			if token['nome']=="CHE":
				token = le_token()
				if S(token):
					token = le_token()
					if token['nome']=="CHD":
						token = le_token()
						if ELSE(token):
							return True
						else:
							return False
						
					else:
						return False
					
				else:
					return False
				
			else:
				return False
			
		else:
			return False

	else:
		return False	


def ELSE(token):
	print "token no ELSE ",token['nome']
	if token['nome']=="ELS":
		token = le_token()
		if token['nome']=="CHE":
			token = le_token()
			if S(token):
				token = le_token()
				if token['nome']=="CHD":
					token = le_token()
					if S(token):
						return True

					else:
						return False

				else:
					return False
					
			else:
				return False
				
		else:
			return False
			
	elif S(token):
			return True
		
	else:
		return False			
		
	

def FINAL(token):
	print "token no FINAL",token['nome']
	if token['nome']=="VAR":
		return True
	elif token['nome']=="FAL":
		return True
	elif token['nome']=="TRU":
		return True
	else:
		return False
		
def precisodormir(token):
	TOP = "entrada"
	while TOP != "EOF" or token != "+":
		print pilha
		if pilha:
			TOP = pilha.pop()
			if TOP == "EOF" and token == "+":
				return True
			elif "token" == TOP['tipo']:
				
				if "variavel" == TOP['tipo']:
					desempilha()
					token = le_token()
				else:
					print "erro :("
			else:
				print S_linha(token)
				aux = desempilha()
				if aux['tipo']== "variavel":
					if aux["nome"] == "E0_linha":
						token = le_token;
						E0_linha(token)
						
					elif aux["nome"] == "E1_linha":
						token = le_token;
						E1_linha(token)
						
					elif aux["nome"] == "E2_linha":
						token = le_token;
						E2_linha(token)
						
					elif aux["nome"] == "E3_linha":
						token = le_token;
						E3_linha(token)
					else:
						print "..."
				else:
					print "..."	
		else:
			return False
#parametro = sys.argv[1:]

entrada = "TestFile/test3.txt"
geraLista(entrada) 


token = le_token()
empilha({'nome':'EOF','tipo':'token'})
empilha({'nome':'S_linha','tipo':'variavel'})
precisodormir(token)


				
			
				
			
	 	

		

		



	
