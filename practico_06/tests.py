# Implementar los casos de prueba descriptos.

import unittest

from practico_05.ejercicio_01 import Socio
from practico_06.capa_negocio import NegocioSocio, LongitudInvalida , MaximoAlcanzado , DniRepetido


class TestsNegocio(unittest.TestCase):

    def setUp(self):
        super(TestsNegocio, self).setUp()
        self.ns = NegocioSocio()

    def tearDown(self):
        super(TestsNegocio, self).tearDown()
        self.ns.datos.borrar_todos()

    def test_alta(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)

        # post-condiciones: 1 socio registrado
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 1)

    def test_regla_1(self):
        #pre-condicion: socio existente
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)
        self.assertTrue(exito)

        #ejecuto la logica (true)
        valido = Socio(dni= 38250500, nombre='Carlos', apellido='Arias')
        self.assertTrue(self.ns.regla_1(valido))

        # Excepcion manejada , DNI repetido
        repetido = Socio(dni= 38250500 , nombre='Pedro', apellido = 'Nuñez')    
        self.assertRaises(DniRepetido , self.ns.regla_1 , repetido)

    def test_regla_2_nombre_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='J', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_nombre_mayor_15(self):
        #valida regla
        valido = Socio(dni=789456123, nombre='Fabricio', apellido='Fontanelli')
        self.assertTrue(self.ns.regla_2(valido))
        
        # nombre mayor a 15 caracteres
        invalido = Socio(dni= 789456123 , nombre='Fabricio Emanuel Pablo', apellido ='Fontanelli')
        self.assertRaises(LongitudInvalida, self.ns.regla_2 , invalido )

    def test_regla_2_apellido_menor_3(self):
        #valida regla
        valido = Socio(dni=456123789, nombre='German', apellido='Fontanelli')
        self.assertTrue(self.ns.regla_2(valido))
        
        # apellido menor a 3 caracteres
        invalido = Socio(dni= 456123789 , nombre='German', apellido ='Re')
        self.assertRaises(LongitudInvalida, self.ns.regla_2 , invalido )

    def test_regla_2_apellido_mayor_15(self):
        #valida regla
        valido = Socio(dni=753159456, nombre='Damian', apellido='Garcia')
        self.assertTrue(self.ns.regla_2(valido))
        
        # apellido apellido mayor a 15
        invalido = Socio(dni= 753159456 , nombre='Damian', apellido ='Garcia Perez Moreno')
        self.assertRaises(LongitudInvalida, self.ns.regla_2 , invalido )

    def test_regla_3(self):
        #precondicion : doy de alta 200 socios
        for i in range(0, 200):
            socio = Socio(dni=i, nombre='Juan', apellido='Perez')
            self.ns.alta(socio)
        
        #igual
        self.assertEqual(len(self.ns.todos()), 200)
        #excepcion
        with self.assertRaises(MaximoAlcanzado):
            self.ns.regla_3()


    def test_baja(self):
        #precondicion : 1 socio registrado
        socio = Socio(dni=789456123, nombre='Fabricio', apellido='Fontanelli')
        exitoAlta = self.ns.alta(socio)
        self.assertTrue(exitoAlta)
        self.assertEqual(len(self.ns.todos()),1)

        #ejecuto logica
        exitoBaja = self.ns.baja(socio.id)

        #postcondiciones : 1 socio dado de baja
        self.assertTrue(exitoBaja)
        self.assertEqual(len(self.ns.todos()),0)

    def test_buscar(self):
        #precondicion : 1 socio existente
        socio = Socio(dni=789456123, nombre='Fabricio', apellido='Fontanelli')
        exitoAlta = self.ns.alta(socio)
        self.assertTrue(exitoAlta)
        self.assertEqual(len(self.ns.todos()),1)

        #ejecuto la logica - busco el socio
        socioBuscado = self.ns.buscar(socio.id)

        #postcondiciones - encontre el socio
        self.assertEqual(socio , socioBuscado)

        #Doy de baja el socio
        self.ns.baja(socio.id)

        #postcondiciones - no se encontro el socio
        self.assertFalse(self.ns.buscar(socio.id))

    def test_buscar_dni(self):
        #precondicion : 1 socio existente
        socio = Socio(dni=789456123, nombre='Fabricio', apellido='Fontanelli')
        exitoAlta = self.ns.alta(socio)
        self.assertTrue(exitoAlta)
        self.assertEqual(len(self.ns.todos()),1)

         #ejecuto la logica - busco el socio
        socioBuscado = self.ns.buscar_dni(socio.dni)

        #postcondiciones - encontre el socio
        self.assertEqual(socio,socioBuscado)

        #doy de baja el socio
        self.ns.baja(socio.id)

        #postcondiciones - no encuentro el socio
        self.assertFalse(self.ns.buscar_dni(socio.dni))

    def test_todos(self):
        #precondiciones : no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0 )

        #doy de alta socios y valido que los de de alta bien
        socio1 = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito1 = self.ns.alta(socio1)
        self.assertTrue(exito1)
        socio2 = Socio(dni=78945612, nombre='Damian', apellido='Rios')
        exito2 = self.ns.alta(socio2)
        self.assertTrue(exito2)
        socio3 = Socio(dni=45612378, nombre='John', apellido='Sosa')
        exito3 = self.ns.alta(socio3)
        self.assertTrue(exito3)

        #ejecuto la logica 
        listaSocios = self.ns.todos()

        #postcondiciones - tengo 3 socios cargados

        self.assertEqual(len(listaSocios),3)

    def test_modificacion(self):
        #precondiciones - cargo un socio asi puedo modificar
        socio= Socio(dni= 12345678 , nombre = 'Fabricio', apellido = 'Villa')
        exitoAlta = self.ns.alta(socio)
        self.assertTrue(exitoAlta)

        #ejecuto la logica , realizo modificaciones a la instancia 
        socio.nombre = "Sebastian"
        socio.apellido = "Perez"
        socio.dni = 45612378
        #ejecuto la logica 
        exitoModificacion= self.ns.modificacion(socio)
        #postcondicion : socio modificado
        self.assertTrue(exitoModificacion)

        #busco el socio
        socioEncontrado = self.ns.buscar_dni(45612378)
        #compruebo si coincide con la modificacion
        self.assertEqual(socioEncontrado.nombre , "Sebastian")
        self.assertEqual(socioEncontrado.apellido,"Perez")

