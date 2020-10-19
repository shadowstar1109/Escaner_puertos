#!/usr/bin/python
#Echo por Shadow town 
#Version 1.0
#Modulos
import socket
from socket import *
#Funcion Principal
if __name__ == '__main__':
    equipo = raw_input('Ingresa El Dominio o Ip Que Deseas Escanear: ')
    IP_equipo = gethostbyname(equipo)
    #Escaneo 
    print 'comenzando el escaneo en la ip ', ipequipo;
   #Rango De Puertos Que Deseamos Escanear
    for puertos in range(10,500)
      #Socket
      cliente = socket(AF_INET, SOCK_STREAM)
      #Guardar Informacion En La Variable
      resultado = cliente.connect_ex((ipequipo, puertos))
      #Resultado = 0 Imprime en pantalla el numero de puerto con su respectivo estado  
      if (resultado == 0):
       print 'puerto %d: Abierto' %(puertos) 
      #Cerramos La Conexión Para Que Se Analice El Siguiente Puerto
       cliente.close()
