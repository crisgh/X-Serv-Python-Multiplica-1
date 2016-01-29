#! /usr/bin/python
#-*- coding: utf-8 -*-
numeros = range(1,11)
for elemento1 in numeros:
    print "/nTabla del ",str(elemento1)
    print "------------"
    for elemento2 in numeros:
        print str(elemento1) + " por " + str(elemento2) + " = " + str(elemento1*elemento2)
