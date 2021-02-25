# -*- coding: utf-8 -*-
"""
Spyder Editor
Author: Antonio Cardona Costa (toniccibz@gmail.com)
Dev: 2020-2021

Combat Simulator for "Anima: Beyond Fantasy" rpg system

ChangeLog:
    v.0.3
        · Fixed attack fumble
        · Fixed % of damage shown
        
FEATURES:
    · BASIC COMBAT MANAGEMENT
    · D100 / D20 SIMULATOR
    · COMBOS MANAGEMENT
    · COMBAT SITUATION
    · ABSOLUTE DEFENSE
    · COUNTER MANAGEMENT
    · FUMBLES MANAGEMENT
    · CRITICAL DAMAGE MANAGEMENT
---------------
TO DO:
    · AÑADIR VARIABLE FIJA A TIRADA DE DADO
    · ADD COMBAT TACTICS (p.90 Core Exxet)
        + derribo
        + Inutilizar
        + Desarmar
        + Presa
        + Inconsciencia
        + Ataque con critico secundario
        + Ataque en area
        + Engatillar
        + ataque asesino
    · ADD DEFENSE TACTICS (p.91 Core Exxet)
        + Apartar
        + Resistir el golpe
        + Parada sin armas
        + Daño no letal
    · ADD BREKEAGE MECHANICS
    · ADD RANGED COMBAT
    · ADD MAGIC CASTING MECHANICS
    · GET IN ACCOUNT MASTERIES (IMPROVE FUMBLE)
"""

from enum import Enum
from random import randint
#import Characters.BaseChara as CharacterSheet

class zonasApuntado(Enum):
    """Enum para determinar penalizador de apuntado"""
    NADA = 0
    CUELLO = 1
    CABEZA = 2
    CODO  = 3
    CORAZON = 4
    INGLE = 5
    PIE = 6
    MANO = 7
    RODILLA = 8
    ABDOMEN = 9
    BRAZO = 10
    MUSLO = 11
    PANTORRILLA = 12
    TORSO = 13
    OJO = 14
    MUÑECA = 15
    HOMBRO = 16

class Combat_situation(Enum):
    """Enum para determinar la situación de combate"""
    #                ATK, PARRY, FLEE, TURN, PHISIC_ACTION
    NONE = 0
    FLANKED = 1     #-10,   -30,  -30,    -,             -  #FLANCO
    BACK_ATTACK = 2 #-30,   -80,  -80,    -,             -  #ESPALDA
    SURPRISE = 3    # NA,   -90,  -90,   NA,           -90  #SORPRESA
    PART_BLIND = 4  #-30,   -30,  -15,    -,           -30  #CEGUERA PARCIAL
    FULL_BLIND = 5  #-100,  -80,  -80,    -,           -90  #CEGUERA ABSOLUTA
    HIGH_GROUND = 6 #+20,     -,    -,    -,             -  #POSICION SUPERIOR
    DOWN = 7
    MINR_PARA = 8
    PART_PARA = 9
    FULL_PARA = 10
    THREATENED = 11
    LEVITATE = 12
    FLIGHT_7_14 = 13
    FLIGHT_PLUS_15 = 14
    CHARGING = 15
    DRAWING = 16
    REDUCED_SPACE = 17
    AGAINST_SMALL = 18
    AGAINST_DIMINUTE = 19


class CombatSimulator:
    """Clase principal del programa"""
    def __init__(self):
        #
        self.mostrarTodosValoresHAHD = True
        # Class variables
        self.bonoContra = 0
        self.situacionCombate = 0
        self.ataqueApuntado = False
        self.penalizadorApuntado = 0 # Negativo
        self.numAtaquesEncadenados = 0
        self.penalizadorArmaSecundaria = 0
        self.penalizadorEncadenados = 0
        self.accion = 0
        self.HA = 0 # attacker skill
        self.HD = 0 # defenders skill
        self.attack_roll = 0
        self.defense_roll = 0
        self.penalizadorDefensas = 0
        self.modificadorDefensaTotal = 30
        self.defense_no = 0 # cuantas defensas ha hecho antes +1
        self.aditional_defenses = 0 # cuantas defensas adicionales tiene sin penalizador
        # Modificadores situacion combate
        self.setted_atk_modifier = 0
        self.setted_def_modifier = 0
        self.setted_parry_modifier = 0
        self.setted_flee_modifier = 0
        #
        self.TA = 0
        self.contraataque = False
        self.pifiaAlAtacar = False
        self.critico = False
        self.SerAcumulacion = False
        self.defensaTotal = False
        self.rangedAttack = False
        self.porcentajeDaño = 0
        self.baseWeapDamage = 0
        self.bonoFuerza = 0
        self.dañoFinal = 0
        self.total_atk = 0
        self.total_def = 0
        self.dadoCritico = 0
        self.RFdefensor = 0
        self.dadoResistencia = 0
        self.resultadoCritico = 0
        self.negativosAtacante = 0 # Negativo
        self.negativosDefensor = 0 # negativo
        self.nivelPifiaAtaque = 0
        self.Resultado = 0
        # rango
        self.playerStr = 0
        self.wpnRange = 0
        self.effectiveRange = 0
        self.maxRange = 0
        self.targetDistance = 0

    @staticmethod
    def checkEntero(valorSTR):
        """
        Comprueba si el valor pasado es entero 
        o una combinatoria de dado + modificador.
        """
        try:
            int(valorSTR)
            return True
        except ValueError:
            try:
                texto = valorSTR.split('+')
                if (texto[0] != 'd100') or (texto[1] == ''):
                    print("Valor invalido")
            except ValueError:
                print("Valor no convertible a int")
            return False

    def porcentajeDeDaño(self):
        """Calcula el porcentaje del daño que inflije un arma."""
        self.porcentajeDaño = self.Resultado - self.TA*10
        self.porcentajeDaño = self.redondeaAbajo(self.porcentajeDaño)
        print(self.porcentajeDaño, "% daño del arma.")

    @staticmethod
    def obtenerBoolInput(message):
        """Permite mostrar un mensaje y obtener un input tipo bool"""
        validation = False
        valReturn = False
        while not validation:
            var = input(message)
            if var in ('y', 'Y', 'S', 's'):
                valReturn = True
                validation = True
            elif var in ('n', 'N'):
                valReturn = False
                validation = True
            else:
                print("Valor invalido, intenta de nuevo. (Usa: y, Y, s, S, n o N)\n")
        return valReturn

    def tiradaAbierta(self, dificultad):
        """Gestiona las repetición en tiradas abiertas"""
        resultadoAbierta = self.diceRoll("d100")
        print("Resultado abierta: ", resultadoAbierta)
        if resultadoAbierta >= dificultad:
            print("Nueva Abierta!")
            resultadoAbierta = resultadoAbierta + self.tiradaAbierta(dificultad+1)
        return resultadoAbierta

    def obtenerIntInput(self, message):
        """Permite preguntar al usuario y obtener un int"""
        validation = False
        while not validation:
            var = input(message)
            # Gestion de dados
            if var == "d100":
                # Tirada de dado
                dice = self.diceRoll(var)
                print("Lanzado dado d100, resultado: ", dice)
                # Tiradas abiertas
                if dice > 90:
                    aplica = self.obtenerBoolInput("Tirada abierta! ¿aplica?")
                    if aplica:
                        dice = dice + self.tiradaAbierta(91)
                # Gestion de resultado
                if dice > 380:
                    inhumano = self.obtenerBoolInput("¿Es inhumano?\n")
                    if not inhumano:
                        dice = 380
                    else:
                        if dice > 440:
                            zen = self.obtenerBoolInput("¿Es Zen?\n")
                            if not zen:
                                dice = 440
                # Pifias
                if dice < 4:
                    print("Resultado dado:", dice, "Pifia!")
                validation = True
                return dice
            else:
                if self.checkEntero(var):
                    validation = True
                else:
                    txt = var.split("+")
                    #print(txt)
                    if txt[0] == 'd100':
                        mod = txt[1]
                        if self.checkEntero(mod):
                            # Tirada de dado
                            dice = self.diceRoll(txt[0])
                            #print("Lanzado dado d100, resultado: ", dice)
                            # Tiradas abiertas
                            if dice > 90:
                                aplica = self.obtenerBoolInput("Tirada abierta! ¿aplica?")
                                if aplica:
                                    dice = dice + self.tiradaAbierta(91)
                            # Añadir el modificador
                            modificador = int(txt[1])
                            #print("modificador leido: ", modificador)
                            totalTirada = dice + modificador
                            # Gestion de resultado
                            if totalTirada > 380:
                                inhumano = self.obtenerBoolInput("¿Es inhumano?\n")
                                if not inhumano:
                                    totalTirada = 380
                                else:
                                    if totalTirada > 440:
                                        zen = self.obtenerBoolInput("¿Es Zen?\n")
                                        if not zen:
                                            totalTirada = 440
                            validation = True
                            print("Resultado = ", totalTirada, "(",dice,"+",modificador,")")
                            return totalTirada
                    # Si no es entero no pasa nada
        return int(var)

    @classmethod
    def redondeaAbajo(self, valor):
        """Redondea hacia abajo el valor sobre base 10."""
        val = valor - (valor % 10)
        return val

    def elegirSituacionAtaqueRango(self):
        print("Modificadores de ATAQUE A DISTANCIA")
        print("----------------------------")
        print(" # SITUACION            HA")
        print(" 0  No aplica ningun modificador")
        print(" 1  Movimiento activo       -10")
        print(" 2  Corriendo (max TM)      -50")
        print(" 3  Escasa visibilidad      -20")
        print(" 4  Blanco en cobertura     -40")
        print(" 5  Cambiar blanco          -10")
        print(" 6  Velocidad blanco > 8    -20")
        print(" 7  Velocidad blanco = 10   -40")
        print(" 8  Velocidad blanco > 10   -60")
        print(" 9  Ha defendido este turno -40")
        print(" 10 Fuera rango efectivo    -30")
        print(" 11 Blanco grande           +30")
        print(" 12 Apuntar 1 turno         +10")
        print(" 13 Apuntar 2 turnos        +20")
        print(" 14 Apuntar 3 turnos        +30")
        print(" 15 A bocajarro             +30")
        seleccion = -1
        while (seleccion < 1 or seleccion > 15):
            seleccion = self.obtenerIntInput("Selecciona el número valido (0-15)\n")
            self.situacionCombate = seleccion
        # Consecuencias
        if seleccion == 1:
            self.setted_atk_modifier = self.setted_atk_modifier - 10
        elif seleccion == 2:
            self.setted_atk_modifier = self.setted_atk_modifier - 50
        elif seleccion == 3:
            self.setted_atk_modifier = self.setted_atk_modifier - 20
        elif seleccion == 4:
            self.setted_atk_modifier = self.setted_atk_modifier - 40
        elif seleccion == 5:
            self.setted_atk_modifier = self.setted_atk_modifier - 10
        elif seleccion == 6:
            self.setted_atk_modifier = self.setted_atk_modifier - 20
        elif seleccion == 7:
            self.setted_atk_modifier = self.setted_atk_modifier - 40
        elif seleccion == 8:
            self.setted_atk_modifier = self.setted_atk_modifier - 60
        elif seleccion == 9:
            self.setted_atk_modifier = self.setted_atk_modifier - 40
        elif seleccion == 10:
            self.setted_atk_modifier = self.setted_atk_modifier - 30
        elif seleccion == 11:
            self.setted_atk_modifier = self.setted_atk_modifier + 30
        elif seleccion == 12:
            self.setted_atk_modifier = self.setted_atk_modifier + 10
        elif seleccion == 13:
            self.setted_atk_modifier = self.setted_atk_modifier + 20
        elif seleccion == 14:
            self.setted_atk_modifier = self.setted_atk_modifier + 30
        elif seleccion == 15:
            self.setted_atk_modifier = self.setted_atk_modifier + 30
        else:
            print("Selección invalida, no se aplican modificadores")

    def elegirSituacionCombate(self):
        print("Selecciona situación combate")
        print("----------------------------")
        print(" # SITUACION            HA   HD   HE TURN  Accion")
        print(" 0 No aplica ningun modificador")
        print(" 1 Flanco              -10  -30  -30    -     -")
        print(" 2 Espalda             -30  -80  -80    -     -")
        print(" 3 Sorpresa             NA  -90  -90   NA   -90")
        print(" 4 Ceguera parcial     -30  -30  -15    -   -30")
        print(" 5 Ceguera absoluta   -100  -80  -80    -   -90")
        print(" 6 Posición superior   +20    -    -    -     -")
        print(" 7 Derribado           -30  -30  -30   -10  -30")
        print(" 8 Parálisis menor     -20  -20  -40   -20  -40")
        print(" 9 Parálisis parcial   -80  -80  -80   -30  -60")
        print("10 Parálisis completa -200 -200 -200  -100 -200")
        print("11 Amenazado           -20 -120 -120   -50 -100")
        print("12 Levitando           -20  -20  -40     -  -60")
        print("13 Vuelo tipo 7 a 14   +10  +10  +10   +10    -")
        print("14 Vuelo 15 o mayor    +15  +10  +20   +10    -")
        print("15 Cargando            +10  -10  -20     -    -")
        print("16 Desenfundar         -25  -25    -     -  -25")
        print("17 Espacio reducido    -40  Esp. -40  Esp.  -20")
        print("18 Adversario pequeño  -10    -    -     -    -")
        print("19 Adversario diminuto -20  -10    -     -    -")
        seleccion = -1
        while (seleccion < 0 or seleccion > 19):
            seleccion = self.obtenerIntInput("Selecciona el número valido (0-19)\n")
            self.situacionCombate = seleccion

        # Consecuencias
        if seleccion == 1:
            self.setted_atk_modifier = self.setted_atk_modifier - 10
            self.setted_parry_modifier = self.setted_parry_modifier - 30
            self.setted_flee_modifier = self.setted_flee_modifier - 30
        elif seleccion == 2:
            self.setted_atk_modifier = self.setted_atk_modifier - 30
            self.setted_parry_modifier = self.setted_parry_modifier - 80
            self.setted_flee_modifier = self.setted_flee_modifier - 80
        elif seleccion == 3:
            self.setted_atk_modifier = self.setted_atk_modifier - 0
            self.setted_parry_modifier = self.setted_parry_modifier - 90
            self.setted_flee_modifier = self.setted_flee_modifier - 90
        elif seleccion == 4: # Ceguera parcial
            self.setted_atk_modifier = self.setted_atk_modifier - 30
            self.setted_parry_modifier = self.setted_parry_modifier - 30
            self.setted_flee_modifier = self.setted_flee_modifier - 15
        elif seleccion == 5: # Ceguera absoluta
            self.setted_atk_modifier = self.setted_atk_modifier - 100
            self.setted_parry_modifier = self.setted_parry_modifier - 80
            self.setted_flee_modifier = self.setted_flee_modifier - 80
        elif seleccion == 6: # Posicion superior
            self.setted_atk_modifier = self.setted_atk_modifier + 20
        elif seleccion == 7: # Derribado
            self.setted_atk_modifier = self.setted_atk_modifier - 30
            self.setted_parry_modifier = self.setted_parry_modifier - 30
            self.setted_flee_modifier = self.setted_flee_modifier - 30
        elif seleccion == 8: # Paralisis Menor
            self.setted_atk_modifier = self.setted_atk_modifier - 20
            self.setted_parry_modifier = self.setted_parry_modifier -20
            self.setted_flee_modifier = self.setted_flee_modifier - 40
        elif seleccion == 9: # Paralisis Parcial
            self.setted_atk_modifier = self.setted_atk_modifier - 80
            self.setted_parry_modifier = self.setted_parry_modifier - 80
            self.setted_flee_modifier = self.setted_flee_modifier - 80
        elif seleccion == 10: # Paralisis Completa
            self.setted_atk_modifier = self.setted_atk_modifier - 200
            self.setted_parry_modifier = self.setted_parry_modifier -200
            self.setted_flee_modifier = self.setted_flee_modifier - 200
        elif seleccion == 11: # Amenazado
            self.setted_atk_modifier = self.setted_atk_modifier - 20
            self.setted_parry_modifier = self.setted_parry_modifier - 120
            self.setted_flee_modifier = self.setted_flee_modifier - 120
        elif seleccion == 12: # Levitando
            self.setted_atk_modifier = self.setted_atk_modifier - 20
            self.setted_parry_modifier = self.setted_parry_modifier - 20
            self.setted_flee_modifier = self.setted_flee_modifier - 40
        elif seleccion == 13: # Vuelo 4 a 14
            self.setted_atk_modifier = self.setted_atk_modifier + 10
            self.setted_parry_modifier = self.setted_parry_modifier + 10
            self.setted_flee_modifier = self.setted_flee_modifier + 10
        elif seleccion == 14: # vuelo >= 15
            self.setted_atk_modifier = self.setted_atk_modifier + 15
            self.setted_parry_modifier = self.setted_parry_modifier + 10
            self.setted_flee_modifier = self.setted_flee_modifier + 20
        elif seleccion == 15: # Cargando
            self.setted_atk_modifier = self.setted_atk_modifier + 10
            self.setted_parry_modifier = self.setted_parry_modifier - 10
            self.setted_flee_modifier = self.setted_flee_modifier - 20
        elif seleccion == 16: # Desenfundar
            self.setted_atk_modifier = self.setted_atk_modifier - 25
            self.setted_parry_modifier = self.setted_parry_modifier - 25
        elif seleccion == 17: # Espacio Reducido
            self.setted_atk_modifier = self.setted_atk_modifier - 40
            self.setted_flee_modifier = self.setted_flee_modifier - 40
        elif seleccion == 18: # adversario pequeño
            self.setted_atk_modifier = self.setted_atk_modifier - 10
        elif seleccion == 19: #adversario diminuro
            self.setted_atk_modifier = self.setted_atk_modifier - 20
            self.setted_parry_modifier = self.setted_parry_modifier -10
        else:
            print("No se aplican modificadores.")

    def localizarCritico(self):
        localizacion = self.obtenerIntInput("¿Resultado dado localizar critico?\n")
        if  0 < localizacion < 11:
            print("Impacto en costillas.")
        elif 10 < localizacion < 21:
            print("Impacto en Hombro.")
        elif 20 < localizacion < 31:
            print("Impacto en Estomago.")
        elif 30 < localizacion < 41:
            print("Impacto en Riñones.")
        elif 40 < localizacion < 49:
            print("Impacto en pecho.")
        elif 48 < localizacion < 51:
            print("Impacto en CORAZON.")
        elif 50 < localizacion < 55:
            print("Impacto en antebrazo superior derecho.")
        elif 54 < localizacion < 59:
            print("Impacto en antebrazo inferior derecho.")
        elif 58 < localizacion < 61:
            print("Impacto en mano derecha.")
        elif 60 < localizacion < 65:
            print("Impacto en antebrazo superior izquierdo.")
        elif 64 < localizacion < 69:
            print("Impacto en antebrazo superior izquierdo.")
        elif 68 < localizacion < 71:
            print("Impacto en mano izquierda.")
        elif 70 < localizacion < 75:
            print("Impacto en muslo derecho.")
        elif 74 < localizacion < 79:
            print("Impacto en pantorrila derecha.")
        elif 78 < localizacion < 81:
            print("Impacto en pie derecho.")
        elif 80 < localizacion < 85:
            print("Impacto en muslo izquierdo.")
        elif 84 < localizacion < 89:
            print("Impacto en pantorrilla izquierda.")
        elif 88 < localizacion < 91:
            print("Impacto en pie izquierdo.")
        elif 90 < localizacion < 101:
            print("Impacto en CABEZA.")

    def seleccionarAtaqueApuntado(self):
        """Gestión de penalizador por ataque apuntado"""
        print("Selecciona donde apunta el ataque")
        print("----------------------------")
        print(" # Localizacion  Penalizador")
        print(" 1 Cuello        -80")
        print(" 2 Cabeza        -60")
        print(" 3 Codo          -60")
        print(" 4 Corazón       -60")
        print(" 5 Ingle         -60")
        print(" 6 Pie           -50")
        print(" 7 Mano          -40")
        print(" 8 Rodilla       -40")
        print(" 9 Abdomen       -20")
        print("10 Brazo         -20")
        print("11 Muslo         -20")
        print("12 Pantorrilla   -10")
        print("13 Torso         -10")
        print("14 Ojo          -100")
        print("15 Muñeca        -40")
        print("16 Hombro        -30")
        seleccion = -1
        while (seleccion < 0 or seleccion > 16):
            seleccion = self.obtenerIntInput("Selecciona el número valido (1-16)\n")

        if seleccion == 1:
            self.penalizadorApuntado = -80
        elif seleccion == 2:
            self.penalizadorApuntado = -60
        elif seleccion == 3:
            self.penalizadorApuntado = -60
        elif seleccion == 4:
            self.penalizadorApuntado = -60
        elif seleccion == 5:
            self.penalizadorApuntado = -60
        elif seleccion == 6:
            self.penalizadorApuntado = -50
        elif seleccion == 7:
            self.penalizadorApuntado = -40
        elif seleccion == 8:
            self.penalizadorApuntado = -40
        elif seleccion == 9:
            self.penalizadorApuntado = -20
        elif seleccion == 10:
            self.penalizadorApuntado = -20
        elif seleccion == 11:
            self.penalizadorApuntado = -20
        elif seleccion == 12:
            self.penalizadorApuntado = -10
        elif seleccion == 13:
            self.penalizadorApuntado = -10
        elif seleccion == 14:
            self.penalizadorApuntado = -100
        elif seleccion == 15:
            self.penalizadorApuntado = -40
        elif seleccion == 16:
            self.penalizadorApuntado = -30
        else:
            print("Valor seleccion invalido, aplicado 0 penalizador\n")
            self.penalizadorApuntado = 0

    @classmethod
    def getTamInput(self):
        """Determina el tamaño del arma."""
        valido = False
        valDevuelto = 0
        while not valido:
            valor = input("¿Tamaño del arma? (P, p, M, m, G, g)\n")
            if valor in ('P','p'):
                valido = True
                valDevuelto = 1
            elif valor in ('M', 'm'):
                valido = True
                valDevuelto = 2
            elif valor in ('G','g'):
                valido = True
                valDevuelto = 3
            else:
                print("Tamaño invalido, usa (P,p,M,m,G,g)\n")
        return valDevuelto

    def calcularAtaqueArmaSecundaria(self):
        # Penalizador dos armas
        self.penalizadorArmaSecundaria = 0
        dualWield = self.obtenerBoolInput("¿Ataque con arma secundaria?\n")
        if dualWield:
            ambidestria = self.obtenerBoolInput("¿Es ambidiestro?\n")
            if ambidestria:
                self.penalizadorArmaSecundaria = -10
            else:
                self.penalizadorArmaSecundaria = -40
        else:
            self.penalizadorArmaSecundaria = 0

        cambiaObjetivo = self.obtenerBoolInput("¿Cambia de objetivo? (-25 atk)\n")
        if cambiaObjetivo:
            self.SerAcumulacion = self.obtenerBoolInput("¿Defensor es ser de acumulacion?\n")
            if not self.SerAcumulacion:
                self.HD = self.obtenerIntInput("¿Habilidad defensa/esquiva?\n")
            self.defense_no = self.obtenerIntInput("¿Defensa número..? (defensas realizadas en este turno + 1)\n")
        else:
            self.defense_no = self.defense_no + 1
        self.attack_roll = self.obtenerIntInput("¿Resultado dado ataque?\n")
        self.defense_roll = self.obtenerIntInput("¿Resultado dado defensa?\n")
        self.TA = self.obtenerIntInput("¿Tipo Armadura contra el ataque?\n")
        # Calcular resultado combat0e
        self.calcularResultadoAtaque()
        self.calcularResultadoDefensa()
        if cambiaObjetivo:
            self.Resultado = self.total_atk - self.total_def - 25
        else:
            self.Resultado = self.total_atk - self.total_def
        print("")
        print("RESULTADO DEL COMBATE")
        print("--------------------------------")
        print("Habilidad ataque final: ", self.total_atk)
        print("Habilidad defensa final: ", self.total_def)
        print("Resultado Combate: ", self.Resultado)
        self.gestionResultadoCombate()

    def calcularResultadoAtaque(self):
        # Número de acción este turno
        penalizadorAccion = ((self.accion - 1) * -25)

        # Modificador situacion combate
        if self.mostrarTodosValoresHAHD:
            print("RESULTADO ATAQUE")
            print("-------------------")
            print(self.HA, ": HA")
            print(self.attack_roll, ": D100")
            print(self.penalizadorEncadenados, ": Penalizador encadenados")
            print(penalizadorAccion, ": Penalizador acción")
            print(self.penalizadorArmaSecundaria, ": Pen Arma secundaria")
            print(self.penalizadorApuntado, ": Pen Apuntado")
            print(self.setted_atk_modifier, ": Modificador ataque definido.")
            print(self.bonoContra, ": Bono contraataque.")
            print(self.negativosAtacante, ": negativos del atacante")
        self.total_atk = self.HA + self.attack_roll + self.penalizadorEncadenados + penalizadorAccion + self.penalizadorArmaSecundaria + self.penalizadorApuntado + self.setted_atk_modifier + self.bonoContra + self.negativosAtacante

    def setRangeByStrength(self):
        if self.strength == 3:
            print("Distancia efectiva -30 m")
            self.effectiveRange = self.effectiveRange - 30
        elif self.strength == 4:
            print("Distancia efectiva -10 m")
            self.effectiveRange = self.effectiveRange - 10
        elif self.strength == 5 or self.strength ==  6:
            print("Distancia efectiva sin modificar.")
        elif self.strength == 7:
            print("Distancia efectiva +10 m")
            self.effectiveRange = self.effectiveRange + 10
        elif self.strength == 8:
            print("Distancia efectiva +20 m")
            self.effectiveRange = self.effectiveRange + 20
        elif self.strength == 9:
            print("Distancia efectiva +30 m")
            self.effectiveRange = self.effectiveRange + 30
        elif self.strength == 10:
            print("Distancia efectiva +50 m")
            self.effectiveRange = self.effectiveRange + 50
        elif self.strength == 11:
            print("Distancia efectiva +100 m si el arma es calidad +5 (+50m de lo contrario)")
            refinement = self.obtenerBoolInput("¿El arma es +5 o superior?")
            if refinement:
                self.effectiveRange = self.effectiveRange + 100
            else:
                self.effectiveRange = self.effectiveRange + 50
        elif self.strength == 12:
            print("Distancia efectiva +250 m si el arma es calidad +10 (+50m de lo contrario)")
            refinement = self.obtenerBoolInput("¿El arma es +10 o superior?")
            if refinement:
                self.effectiveRange = self.effectiveRange + 250
            else:
                refinement5 = self.obtenerBoolInput("¿El arma es +5?")
                if refinement5:
                    self.effectiveRange = self.effectiveRange + 100
                else:
                    self.effectiveRange = self.effectiveRange + 50
        elif self.strength == 13:
            print("Distancia efectiva +500 m si el arma es calidad +10 (+50m de lo contrario)")
            refinement = self.obtenerBoolInput("¿El arma es +10 o superior?")
            if refinement:
                self.effectiveRange = self.effectiveRange + 500
            else:
                refinement5 = self.obtenerBoolInput("¿El arma es +5?")
                if refinement5:
                    self.effectiveRange = self.effectiveRange + 100
                else:
                    self.effectiveRange = self.effectiveRange + 50
        elif self.strength == 14:
            print("Distancia efectiva +1000 m si el arma es calidad +15 (+50m de lo contrario)")
            refinement15 = self.obtenerBoolInput("¿El arma es +15 o superior?")
            if refinement15:
                self.effectiveRange = self.effectiveRange + 1000
            else:
                refinement10 = self.obtenerBoolInput("¿El arma es +10?")
                if refinement10:
                    self.effectiveRange = self.effectiveRange + 500
                else:
                    refinement5 = self.obtenerBoolInput("¿El arma es +5?")
                    if refinement5:
                        self.effectiveRange = self.effectiveRange + 100
                    else:
                        self.effectiveRange = self.effectiveRange + 50
        elif self.strength == 15:
            print("Distancia efectiva +5000 m si el arma es calidad +15 (+50m de lo contrario)")
            refinement = self.obtenerBoolInput("¿El arma es +15 o superior?")
            if refinement:
                self.effectiveRange = self.effectiveRange + 5000
            else:
                refinement10 = self.obtenerBoolInput("¿El arma es +10?")
                if refinement10:
                    self.effectiveRange = self.effectiveRange + 500
                else:
                    refinement5 = self.obtenerBoolInput("¿El arma es +5?")
                    if refinement5:
                        self.effectiveRange = self.effectiveRange + 100
                    else:
                        self.effectiveRange = self.effectiveRange + 50
        elif self.strength >= 16:
            print("Distancia efectiva +10.000 m si el arma es calidad +20 (+50m de lo contrario)")
            refinement20 = self.obtenerBoolInput("¿El arma es +20 o superior?")
            if refinement20:
                self.effectiveRange = self.effectiveRange + 10000
            else:
                refinement15 = self.obtenerBoolInput("¿El arma es +15 o superior?")
                if refinement15:
                    self.effectiveRange = self.effectiveRange + 5000
                else:
                    refinement10 = self.obtenerBoolInput("¿El arma es +10?")
                    if refinement10:
                        self.effectiveRange = self.effectiveRange + 500
                    else:
                        refinement5 = self.obtenerBoolInput("¿El arma es +5?")
                        if refinement5:
                            self.effectiveRange = self.effectiveRange + 100
                        else:
                            self.effectiveRange = self.effectiveRange + 50

    def establecerVariablesAtacante(self):
        self.accion = self.obtenerIntInput("¿Acción del turno? 2a = -25, 3a = -50\n")
        
        self.rangedAttack = self.obtenerBoolInput("¿Es un ataque a distancia?")
        #self.ataqueEncadenado = self.obtenerBoolInput("¿Ataque encadenado?\n")
        self.numAtaquesEncadenados = self.obtenerIntInput("¿Numero de ataques que realizara con arma primaria?\n")
        self.HA = self.obtenerIntInput("¿Habilidad ataque?\n")
        
        # Ojo si da pifia
        self.attack_roll = self.obtenerIntInput("¿Resultado dado ataque?\n")
        self.gestionPifiaAtaque(self.attack_roll)
        
        if not self.pifiaAlAtacar:
            # Situacion combate
            if self.situacionCombate != 0:
                sufreSituacion = self.obtenerBoolInput("¿Atacante sufre situacion combate?\n")
                if not sufreSituacion:
                    self.setted_atk_modifier = 0
            # Ataque de rango
            if self.rangedAttack:
                self.wpnRange = self.obtenerIntInput("¿Rango del arma? p.77 CE")
                fireType = self.obtenerBoolInput("¿Es arma de fuego?")
                if (fireType):
                    self.effectiveRange = self.wpnRange
                    self.maxRange = self.wpnRange * 2
                else:
                    self.playerStr = self.obtenerIntInput("¿Fuerza del jugador?")
                    self.setRangeByStrength()
                    self.maxRange = self.effectiveRange * 2
                print("Rango efectivo: ", self.effectiveRange, ", Rango Máx:", self.maxRange)    
                self.targetDistance = self.obtenerIntInput("¿Distancia al objetivo?")
                
                # 
                if self.effectiveRange < self.targetDistance < self.maxRange:
                    print("El objetivo esta fuera del rango efectivo. Daño x 0.5")
                    # TO DO.
                if self.targetDistance > self.maxRange:
                    print("El ataque no puede alcanzar al objetivo.")
                    # TO DO.
                self.elegirSituacionAtaqueRango()

            # Ataque apuntado?
            self.penalizadorApuntado = 0
            self.ataqueApuntado = self.obtenerBoolInput("¿Ataque apuntado?\n")
            if self.ataqueApuntado:
                self.seleccionarAtaqueApuntado()
            else:
                self.penalizadorApuntado = 0

            # Ataques encadenados
            self.penalizadorEncadenados = 0
            if self.numAtaquesEncadenados > 1:
                tam = self.getTamInput()
                if tam == 1:
                    penalizadorTamaño = -20
                elif tam == 2:
                    penalizadorTamaño = -30
                elif tam == 3:
                    penalizadorTamaño = -40
                else:
                    print("Error - Tamaño arma invalido\n")
                self.penalizadorEncadenados = penalizadorTamaño * (self.numAtaquesEncadenados-1) # Por cada ataque ADICIONAL expande el penalizador
                print("Cada golpe será penalizado con un ", penalizadorTamaño)
            else:
                self.penalizadorEncadenados = 0

    def establecerVariablesDefensor(self):
        """Todo lo relacionado con la habilidad de defensa"""
        # Acumulacion
        self.SerAcumulacion = self.obtenerBoolInput("¿Defensor es ser de acumulacion?\n")
        if not self.SerAcumulacion:
            self.HD = self.obtenerIntInput("¿Habilidad defensa/esquiva?\n")
            self.defense_roll = self.obtenerIntInput("¿Resultado dado defensa?\n")
            self.gestionPifiaDefensa(self.defense_roll)

        # defensa total?
        self.defensaTotal = self.obtenerBoolInput("¿Defensa total? (perderá acción por un +30)\n")
        if self.defensaTotal:
            self.modificadorDefensaTotal = 30
        else:
            self.modificadorDefensaTotal = 0

        # Situacion combate (setted def modifier)
        if self.situacionCombate != 0:
            sufreSituacion = self.obtenerBoolInput("¿Defensor sufre situacion combate?\n")
            if not sufreSituacion:
                self.setted_def_modifier = 0
            else:
                bloqueoOesquiva = self.obtenerBoolInput("¿Usa bloqueo (Y) o esquiva (N)?\n")
                if bloqueoOesquiva:
                    self.setted_def_modifier = self.setted_parry_modifier
                else:
                    self.setted_def_modifier = self.setted_flee_modifier

        # defensas realizadas
        #self.aditional_defenses = self.obtenerIntInput("¿Cuantas defensas adicionales tiene el defensor?\n")
        self.penalizadorDefensas = 0
        defensasPenalizadas = 0
        self.defense_no = self.obtenerIntInput("¿Defensa número..? (defensas realizadas en este turno + 1)\n")
        # defensas penalizadas
        if self.defense_no > 1:
            self.aditional_defenses = self.obtenerIntInput("¿Cuantas defensas adicionales tiene el defensor?\n")
            defensasPenalizadas = self.defense_no - self.aditional_defenses
        # Calculo penalizador
        if defensasPenalizadas < 2: # 1a defensa no penalizada
            self.penalizadorDefensas = 0
        elif defensasPenalizadas == 2:
            self.penalizadorDefensas = -30
            print("Penalizador por falta de defensas: -30")
        elif defensasPenalizadas == 3:
            self.penalizadorDefensas = -50
            print("Penalizador por falta de defensas: -50")
        elif defensasPenalizadas == 4:
            self.penalizadorDefensas = -70
            print("Penalizador por falta de defensas: -70")
        else:
            self.penalizadorDefensas = -90
            print("Penalizador por falta de defensas: -90")

        # TA
        self.TA = self.obtenerIntInput("¿Tipo Armadura contra el ataque?\n")

    def calcularResultadoDefensa(self):
        if self.mostrarTodosValoresHAHD:
            print("RESULTADO DEFENSA")
            print("-------------------")
            print(self.HD, ": Habilidad Defensa")
            print(self.defense_roll, ": D100")
            print(self.setted_def_modifier, ": Modificador defensa establecido")
            print(self.penalizadorDefensas, ": Penalizador defensas adicionales")
            print(self.negativosDefensor, ": Negativos del defensor")
            print(self.modificadorDefensaTotal, ": Modificador defensa total.")
        self.total_def = self.HD + self.defense_roll + self.setted_def_modifier + self.penalizadorDefensas + self.negativosDefensor + self.modificadorDefensaTotal

    @classmethod
    def diceRoll(self, dice):
        """Permite lanzar dados de 10 y 100 caras"""
        result = 0
        if dice == "d10":
            result = randint(1, 10)
        elif dice == "d100":
            result = randint(1, 100)
        return result

    def gestionPifiaAtaque(self, dado):
        """Que ocurre cuando aparece una pifia en ataque"""
        if dado < 4:
            print("Pifia al ataque: Sufre contraataque con un bonus equivalente al nivel de pifia\n")
            print("Si nivel pifia > 80, ocurrirán otras consecuencias como golpear a compañeros, perder arma, etc.\n")
            self.nivelPifiaAtaque = self.obtenerIntInput("¿Nivel de pifia?\n")
            self.pifiaAlAtacar = True

    def gestionPifiaDefensa(self,dado):
        """Que ocurre cuando aparece una pifia en defensa"""
        if dado < 4:
            print("Pifia al defender: Se resta el nivel de pifia a la habilidad de defensa.\n")
            print("El DJ puede elegir más consecuencias.")
            penalizador = self.obtenerIntInput("¿Nivel de pifia?\n")
            print("Nivel pifia defensa: ", penalizador)
            self.defense_roll = self.defense_roll - penalizador

    def gestionCritico(self):
        self.dadoCritico = self.obtenerIntInput("¿Resultado dado crítico?\n")
        self.RFdefensor = self.obtenerIntInput("¿RF del defensor?\n")
        self.dadoResistencia = self.obtenerIntInput("¿Resultado dado resistencia defensor?\n")
        self.resultadoCritico = self.dañoFinal + self.dadoCritico - self.RFdefensor - self.dadoResistencia + self.negativosDefensor - self.negativosAtacante
        print("Resultado critico: ", self.resultadoCritico)
        if self.resultadoCritico < 0:
            print("No tiene efectos negativos para el defensor.")
        elif self.resultadoCritico >= 0 and self.resultadoCritico < 50:
            print("Penalizador a toda acción = -", self.resultadoCritico)
            print("Penalizador se reduce 5 por turno hasta desaparecer.")
        elif self.resultadoCritico >= 50 and self.resultadoCritico <= 100:
            print("Penalizador a toda acción = -", self.resultadoCritico)
            print("Penalizador se reduce 5 por turno hasta la mitad.")
            if self.SerAcumulacion:
                print("La criatura de acumulacion pierde la acción este turno.")
            self.localizarCritico()
        elif self.resultadoCritico >= 101 and self.resultadoCritico <= 150:
            print("Penalizador a toda acción = -", self.resultadoCritico)
            print("Penalizador se reduce 5 por turno hasta la mitad.")
            print("El miembro donde se reciba daño queda destruido o amputado.")
            print("Si alcanza corazón o cabeza, el defensor muere.")
            self.localizarCritico()
        elif self.resultadoCritico >= 101 and self.resultadoCritico <= 150:
            print("Penalizador a toda acción = -", self.resultadoCritico)
            print("Penalizador se reduce 5 por turno hasta la mitad.")
            print("El miembro donde se reciba daño queda destruido o amputado.")
            print("Si alcanza corazón o cabeza, el defensor muere.")
            self.localizarCritico()
            print("El defensor queda inconsciente y morirá en CON turnos si no recibe atención.")
        else:
            print("Valor de resultado critico invalido:", self.resultadoCritico)

    def gestionResultadoCombate(self):
        if self.Resultado > 0 and not self.pifiaAlAtacar:
            print("TA defensor: ", self.TA)
            if self.TA >= 0 and self.TA < 3:  # TA = 0, TA = 1, TA = 2
                if self.Resultado < 30:
                    print("Fin ataque. Le toca pero no le hace daño. Defensor pierde acción este turno.")
                else:
                    self.porcentajeDeDaño()
                    print("Porcentaje daño: ", self.porcentajeDaño, "%")
                    self.baseWeapDamage = self.obtenerIntInput("¿Daño base del arma?\n")
                    self.bonoFuerza = self.obtenerIntInput("¿Bono de fuerza?\n")
                    self.dañoFinal = self.baseWeapDamage * (self.porcentajeDaño / 100)
                    self.dañoFinal = int(self.dañoFinal)
                    print("Daño infligido: ", self.dañoFinal)
                    vidaDef = self.obtenerIntInput("¿Vida del defensor?\n")
                    porcentajeAlHP = (100/vidaDef) * self.dañoFinal
                    vidaTrasDaño = vidaDef - self.dañoFinal
                    print("Vida restante: ", vidaTrasDaño, "PV (Daño recibido: ", porcentajeAlHP, "%)")
                    self.critico = self.obtenerBoolInput("¿Es crítico?\n")
            elif self.TA >= 3:
                TAabsorb = (self.TA - 3) * 10 + 20
                if self.Resultado < 30 + TAabsorb:
                    print("Fin ataque. Le toca pero no le hace daño. Defensor pierde acción este turno.")
                else:
                    self.porcentajeDeDaño()
                    self.baseWeapDamage = self.obtenerIntInput("¿Daño base del arma?\n")
                    self.bonoFuerza = self.obtenerIntInput("¿Bono de fuerza?\n")
                    self.dañoFinal = self.baseWeapDamage * (self.porcentajeDaño / 100)
                    print("Daño infligido: ", self.dañoFinal)
                    self.critico = self.obtenerBoolInput("¿Es crítico?\n")
        else:
            # Rama contraataque
            if not self.defensaTotal:
                self.contraataque = self.obtenerBoolInput("¿Contraatacar?")
                if self.contraataque:
                    if self.pifiaAlAtacar:
                        self.secuenciaSimple(self.nivelPifiaAtaque)
                    else:
                        self.secuenciaSimple(self.redondeaAbajo(self.Resultado * -1) / 2)
                else:
                    print("Fin ataque. El defensor puede actuar en su turno.")
            else:
                if not self.SerAcumulacion:
                    print("No recibe daño, pero pierde turno con defensa total.")
                else:
                    print("No recibe daño ni pierde acción.")
        # Rama crítico
        if self.critico:
            # implementar
            self.gestionCritico()
        else:
            print("")
        print("Fin del asalto.")

    def resetStats(self):
        print("Reset variables (bool).")
        self.rangedAttack = False
        self.contraataque = False
        self.pifiaAlAtacar = False
        self.critico = False
        self.SerAcumulacion = False
        self.defensaTotal = False
        self.penalizadorArmaSecundaria = 0
        self.setted_atk_modifier = 0
        self.setted_parry_modifier = 0
        self.setted_flee_modifier = 0
        self.setted_def_modifier = 0

    def secuenciaSimple(self, counterBonus = 0):
        self.resetStats()
        self.bonoContra = counterBonus
        self.elegirSituacionCombate()
        # VARIABLES ATACANTE
        self.establecerVariablesAtacante()
        if not self.pifiaAlAtacar:
            # VARIABLES DEFENSOR
            self.establecerVariablesDefensor()
            # Calcular resultado combate
            self.calcularResultadoAtaque()
            self.calcularResultadoDefensa()
            self.Resultado = self.total_atk - self.total_def
            print("")
            print("RESULTADO DEL COMBATE")
            print("--------------------------------")
            print("Habilidad ataque final: ", self.total_atk)
            print("Habilidad defensa final: ", self.total_def)
            print("Resultado Combate: ", self.Resultado)
            # Calculo consecuencias combate
            self.gestionResultadoCombate()

        # Si ataque encadenado
        ataquesRealizados = 1
        if self.numAtaquesEncadenados > 1 and not self.contraataque and not self.pifiaAlAtacar:
            siguienteAtaque = self.obtenerBoolInput("¿seguir con los siguiente ataques con arma principal?\n")
            if siguienteAtaque:
                while ataquesRealizados < self.numAtaquesEncadenados and not self.contraataque:
                    print("Siguiente Ataque")
                    self.resetStats()
                    cambiaObjetivo = self.obtenerBoolInput("¿Cambia de objetivo? (-25 atk)\n")
                    if cambiaObjetivo:
                        self.SerAcumulacion = self.obtenerBoolInput("¿Defensor es ser de acumulacion?\n")
                        if not self.SerAcumulacion:
                            self.HD = self.obtenerIntInput("¿Habilidad defensa/esquiva?\n")
                        self.defense_no = self.obtenerIntInput("¿Defensa número..? (defensas realizadas en este turno + 1)\n")
                    else:
                        self.defense_no = self.defense_no + 1
                    self.attack_roll = self.obtenerIntInput("¿Resultado dado ataque?\n")
                    if self.attack_roll < 4:
                        self.gestionPifiaAtaque(self.attack_roll)
                    self.defense_roll = self.obtenerIntInput("¿Resultado dado defensa?\n")
                    if self.defense_roll < 4:
                        self.gestionPifiaDefensa(self.defense_roll)
                    self.TA = self.obtenerIntInput("¿Tipo Armadura contra el ataque?\n")
                    # Calcular resultado combat0e
                    self.calcularResultadoAtaque()
                    self.calcularResultadoDefensa()
                    if cambiaObjetivo:
                        self.Resultado = self.total_atk - self.total_def - 25
                    else:
                        self.Resultado = self.total_atk - self.total_def
                    print("")
                    print("RESULTADO DEL ATAQUE")
                    print("--------------------------------")
                    print("Habilidad ataque final: ", self.total_atk)
                    print("Habilidad defensa final: ", self.total_def)
                    print("Resultado Combate: ", self.Resultado)

                    # Calculo consecuencias combate
                    self.gestionResultadoCombate()
                    ataquesRealizados += 1

        # Gestion de ataque con arma secundaria
        if not self.contraataque and not self.pifiaAlAtacar:
            self.calcularAtaqueArmaSecundaria()

        if self.pifiaAlAtacar:
            print("Contraataque debido a pifia")
            self.secuenciaSimple(self.nivelPifiaAtaque)
        else:
            # REPETIR TODO EL PROCESO
            repetir = self.obtenerBoolInput("¿Iniciar otro turno?\n")
            if repetir:
                self.secuenciaSimple()
            else:
                print("Fin programa.")

    def run(self):
        print("-ANIMA: COMBAT SIMULATOR")
        print("Para un sistema farragoso y pesado, un simulador cutre.")
        self.secuenciaSimple(0)

if __name__ == "__main__":
    combatSim = CombatSimulator()
    combatSim.run()
   