# -*- coding: utf-8 -*-

# Code Written by Bokko
# TCC-Bokko
# 
# Anima Beyond Fantasy
# Character Generator

from enum import Enum
from random import randint
from random import shuffle

import sys
import os
sys.path.append('../')

class armorLocation(Enum):
    NONE = 0
    SHIRT = 1
    BREAST = 2
    COMPLETE = 3
    HEAD = 4

class facialHair(Enum):
    SHAVED = 0
    HAIRLESS = 1
    FULL_GOATEE = 2
    MOUSTAGE = 3
    SHORT_BEARD = 4
    LONG_BEARD = 5
    CHINESE_MOUSTAGE = 6
    CHIN_GOATEE = 7
    BURNS = 8
    BURN_TO_CHIN = 9

class hairStyle(Enum):
    # MAN EXCLUSIVE
    BOLD = 0
    MOHAWK = 1
    RECEIDING = 2
    # SHARED
    SHAVEN = 3
    SHORT = 4
    MANE = 5
    LONG = 6
    VERY_LONG = 7
    SHORT_CURLY = 8
    MANE_CURLY = 9
    LONG_CURLY = 10
    VERY_LONG_CURLY = 11
    SHAGGY = 12
    MANE_SHAGGY = 13
    LONG_SHAGGY = 14
    VERY_LONG_SHAGGY = 15
    PONYTAIL = 16
    MILITAR = 17
    MONK = 18
    BOWL = 19
    SIDE_SHAVED = 20
    AFRO = 21
    FEATHERED = 22 # Mane with wings
    SPIKED = 23
    SAMURAI = 24
    # WOMAN EXCLUSIVE
    SINGLE_BUN = 25
    DOUBLE_BUNS = 26
    TWIN_TAILS = 27
    BOB = 28
    ANGLED_BOB = 29
    PIXIE_BOB = 30  # Long on one side
    PIG_TAILS = 31 # Short twin tails
    CURLY_CROP = 32
    
class countries(Enum):
    #OLD CONTINENT
    ABEL = 0
    ILMORA = 1
    HELENIA = 2
    DALABORN = 3
    ALBERIA = 4
    GALGADOS = 5
    ARLAN = 6
    KANON = 7
    TOGARINI = 8
    REMO = 9
    BELLAFONTE = 10
    GOLDAR = 11
    HAUFMAN = 12
    HENDELL = 13
    MOTH = 14
    DWANHOLF = 15
    GABRIEL = 16
    PHAION = 17
    DOMINIO = 18
    ARGOS = 19
    KUSHISTAN = 20
    ESTIGIA = 21
    SALAZAR = 22
    NANWE = 23
    LUCRECIO = 24
    KASHMIR = 25
    BAHO = 26
    LANNET = 27
    SHIVAT = 28
    # EURAKIA
    MANTERRA = 29
    CORINIA = 30
    ARABAL = 31
    PRISTINA = 32
    YGDRAMAR = 33
    ELCIA = 34
    ESPHERIA = 35
    ITZI = 36
    DAFNE = 37
    BEKENT = 38
    INDEPENDENTZONE = 39
    # INTERREIGN
    HEINLEIN = 40
    DRAVENOR = 41
    THERESIA = 42
    DELORAN = 43
    # MINOR
    #SANTAMARIANNES =
    FOLKIA = 44
    NEOCHRONIA = 45
    MAGNAPRATORUM = 46
     
class organizations(Enum):
    NONE = 0
    YEHUDA = 1
    SAMAEL = 2
    INQUISITION = 3
    CHURCH = 4
    TOLRAUKO = 5
    BLACKSUN = 6
    WISSENSCHAFT = 7
    SELENE = 8
    MAGUS = 9
    LESJAEGER = 10
    SKYORDER = 11
    EMPERORSHAND = 12
    SETHBROTHERHOOD = 13
    BARAKAH = 14
    BELASARIUS = 15
    ORDEROFMIGUEL = 16
    PROVIDENCEENTERPRISE = 17
    CONSORTIUM = 18 # CONSORCE
    WALKERS = 19 # CAMINANTES
    GUILD = 20  # COFRADIA
    
class etnicities(Enum):
    #OLD CONTINENT
    ASHER = 0
    AION = 1
    TAYAHAR = 2
    ZINNER = 3
    RYUAN = 4
    NORNE = 5
    VILDIAN = 6
    DAEVAR = 7
    KWA = 8
    CELSUS = 9
    #EURAKIA
    DRAVADO = 10
    BASANO = 11
    SULEM = 12
    ACHI = 13
    ERUK = 14
    ROMAN = 15

class hairEyeColor(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2
    YELLOW = 3
    BROWN = 4
    BLACK = 5
    WHITE = 6
    ASH = 7
    ORANGE = 8
    PINK = 9
    TURQUOISE = 10
    PURPLE = 11
    LIGHT_GREEN = 12
    GOLD = 13
    GARNET = 14
    SILVER = 15
    COPPER = 16
    HONEY = 17
    PEACH = 18
    BEIGE = 19
    HETEROCROMATIC = 20    

class armorType(Enum):
    NONE = 0
    SOFT = 1
    HARD = 2

class weaponType(Enum):
    NONE = 0
    TWO_HANDED = 1      # DOS MANOS
    ONE_OR_TWO_HANDED = 2  # UNA O DOS MANOS
    THROWABLE = 3       # LANZABLE
    COMPLEX = 4         # COMPLEJA
    GRAB = 5            # PRESA
    ACCURATE = 6        # PRECISA
    WEAPON_GRAB = 7     # TRABA EL ARMA
    EXOTIC = 8          # EXOTICA
    REACH = 9           # PROYECTIL (ARMA)
    AMMO = 10           # MUNICION

class weaponCritType(Enum):
    NONE = 0
    CUT = 1  # FILO
    IMP = 2  # IMPACT - CONTUNDENTE
    THR = 3  # THRUST - PENETRANTE
    HEA = 4  # HEAT - CALOR
    COL = 5  # COLD - FRIO
    ELE = 6  # ELECTRIC - ELECTRICO
    ENE = 7  # ENERGY - ENERGIA 

class categoryType(Enum):
    NONE = 0        # Placeholder for multiclassing
    WARRIOR = 1     # GUERRERO
    ACROBAT = 2     # GUERRERO ACROBATA
    PALADIN = 3
    DARK_PALADIN = 4    # PALADIN OSCURO
    WEAPON_MASTER = 5   # MAESTRO DE ARMAS
    TECHNICIAN = 6  # TECNICISTA
    TAO = 7
    EXPLORER = 8    # EXPLORADOR
    SHADOW = 9      # SOMBRA
    THIEF = 10      # LADRON
    ASSASSIN = 11   # ASESINO
    SORCERER = 12   # HECHICERO
    WARLOCK = 13    # WARLOCK
    ILLUSIONIST = 14 # ILUSIONISTA
    PSY_MAGE = 15    # HECHICERO MENTALISTA
    SUMMONER = 16    # CONJURADOR
    WARRIOR_SUMMONER = 17 # GUERRERO CONJURADOR
    MENTALIST = 18  # MENTALISTA
    WARRIOR_MENTALIST = 19    # GUERRERO MENTALISTA
    NOVICE = 20     # NOVEL
    # UNOFFICIAL CATEGORIES (Neko Mimi Hexxet)
    GOTHIC_LOLITA = 21
    MAGIC_TSUNDERE = 22 # TSUNDERE MAGICA
    MOE = 23
    NEKOMIMI = 24
    YANDERE = 25
    YANGIRE = 26
    MAGICAL_GIRL = 27
    HEX_WITCH = 28  # BRUJITA TENEBROSA
    
class raceType(Enum):
    HUMAN = 0   # Humanos
    # NEPHILIMS (HALF SOUL)
    NEPH_SYLVAIN = 1
    NEPH_JAYAN = 2
    NEPH_DANJAYNI = 3
    NEPH_EBUDAN = 4
    NEPH_DAIMAH = 5
    NEPH_DUKZARIST = 6
    NEPH_DEVAH = 7
    NEPH_VETALA = 8
    NEPH_TUANDALIR = 9
    # Class
    BETWEEN_WORLDS = 10
    # PURE RACES
    PURE_SYLVAIN = 11
    PURE_JAYAN = 12
    PURE_DANJAYNI = 14
    PURE_EBUDAN = 14
    PURE_DAIMAH = 15
    PURE_DUKZARIST = 16
    PURE_DEVAH = 17
    PURE_VETALA = 18
    PURE_TUANDALIR = 19
    # Class
    UNDEAD = 20
    ELEMENTAL = 21
    ANIMA = 22
    NATURAL = 23

class AnimaCharacter:
    def __init__(self):       
        # PROGRAM VARIABLES
        self.allowNonCanonCategories = False
        self.allowEurakia = True
        self.allowInterregns = False
        self.showBaseStats = True
        self.showFinalStats = True
        
        # CHARACTER SHEET
        # Name Generator
        self.female_names = []
        self.male_names = []
        self.neutral_names = []
        
        # Base line 
        self.name = ""
        self.category = categoryType.NONE # current category (last leveled)
        self.category1 = categoryType.NONE
        self.category2 = categoryType.NONE
        self.category3 = categoryType.NONE
        self.level = 0 # Real level (sum of categories)
        self.levelcat1 = 0 # First Category level
        self.levelcat2 = 0 # Second Category level
        self.levelcat3 = 0 # Third Category level
        self.age = 0
        self.sex = ""
        self.race = raceType.HUMAN
        self.eye_color = hairEyeColor.BROWN
        self.hair_color = hairEyeColor.BROWN
        self.hair_style = hairStyle.BOLD
        self.country = countries.ABEL
        self.etnicity = etnicities.ASHER
        self.PD = 0
        self.appearance = 0     # Dice throw
        # Pressence and resistances
        self.pressence = 0
        self.RF = 0 # Physic resistance
        self.RV = 0 # Venom Resistance
        self.RM = 0 # Magic Resistance
        self.RP = 0 # Psychic Resistance
        self.RE = 0 # Desease Resistance
        
        # EXP
        self.level_exp = 0
        self.acumulated_exp = 0
        
        # Stats
        # -------------------------------------------
        # Agility
        self.agility = 0
        self.agi_bonus = 0      # auto-calculated
        self.agi_modifier = 0   # advantages and other
        self.agi_temp_mod = 0   # temporal
        # Constitution
        self.constitution = 0
        self.con_bonus = 0      # auto-calculated
        self.con_modifier = 0   # advantages and other
        self.con_temp_mod = 0   # temporal
        # Dexterity
        self.dexterity = 0
        self.dex_bonus = 0      # auto-calculated
        self.dex_modifier = 0   # advantages and other
        self.con_temp_mod = 0   # temporal
        # Strenght
        self.strenght = 0
        self.str_bonus = 0      # auto-calculated
        self.str_modifier = 0   # advantages and other
        self.str_temp_mod = 0   # temporal
        # Intelligence
        self.intelligence = 0
        self.int_bonus = 0      # auto-calculated
        self.int_modifier = 0   # advantages and other
        self.int_temp_mod = 0   # temporal
        # Perception
        self.perception = 0
        self.per_bonus = 0      # auto-calculated
        self.per_modifier = 0   # advantages and other
        self.per_temp_mod = 0   # temporal
        # Power
        self.power = 0
        self.pow_bonus = 0      # auto-calculated
        self.pow_modifier = 0   # advantages and other
        self.pow_temp_mod = 0   # temporal
        # Willpower 
        self.willpower = 0
        self.will_bonus = 0     # auto-calculated
        self.will_modifier = 0  # advantages and other
        self.will_temp_mod = 0  # temporal
        
        # Stat dependant attributes (BASE)
        # -------------------------------------------
        self.hp_base = 0             # constitution dependant
        self.size = 0                # STR + CON
        self.height = 0              # Centimeters see size limits, size dependant
        self.weight = 0              # Kilograms see size limit, size dependant
        self.carry_weight = 0        # STR dependant, how much can carry without fatigue
        self.lift_weight = 0         # STR dependant, how much can move or lift
        self.fatigue_base = 0        # constitution dependant
        self.movement_stat_base = 0  # agility dependant
        self.presence_base = 0       # level dependant
        self.regen_base = 0          # constitution dependant
        self.regen_hp_resting = 0    # regen dependant (CON)
        self.regen_hp_unrest = 0     # regen dependant (CON)
        self.negative_reduction = 0  # regen dependant (CON)
        self.regen_effect = ""       # regen dependant (CON)
        self.carry_weight_base = 0   # strenght dependant
        self.actions_x_turn_base = 0 # DES + AGI dependant
        self.ki_pool_base = 0        # STR, AGI, DES, CON, POW, WILL dependant
        self.ki_act_base = 0         # STR, AGI, DES, CON, POW, WILL dependant
        self.zeon_pool_base = 0      # power dependant
        self.magic_act_base = 0      # power dependant
        self.magic_levels_base = 0   # intelligence dependant
        self.innate_magic_base = 0   # act dependant
        self.psychic_potential_base = 0 # willpower dependant
        
        # Calculated (TOTAL)
        # -------------------------------------------
        # POOLS
        self.hp_total = 0             # Base + Multiples + CON Mod + Category increase
        self.zeon_pool_total = 0      # Base + PD_invest + CON Mod + Category increase
        self.fatigue_total = 0        # CON + Modifiers
        self.regen_final = 0         # base + bonuses
        self.movement_value = 0      # Meters, based on movement stat base
        # COMBAT SKILL
        self.attack_skill_total = 0   # Base + DEX MOD + Invest + WeaponMod + Category increase
        self.parry_skill_total = 0    # Base + DEX MOD + Invest + WeaponMod + Category increase
        self.flee_skill_total = 0     # Base + AGI MOD + Invest + WeaponMod + Category increase
        # KI SKILLS
        self.ki_pool_total = 0
        self.ki_ACT_total = 0               # How much Ki can be extracted from pool per turn
        # MAGIC SKILLS
        self.magic_projection_total = 0 # Base + Invested + STAT MOD + Spheres
        self.magic_projection_ofensive = 0 # magic_projection_total + (+/- magic_imbalance)
        self.magic_projection_defensive = 0 # magic_projection_total - (+/- magic_imbalance)        
        self.magic_ACT_total = 0            # How much Zeon can be extracted from pool per turn
        self.summon_total = 0         # convocar
        self.domination_total = 0     # dominar
        self.confine_total = 0        # atar
        self.unsummon_total = 0       # desconvocar
        # PSYCHIC SKILLS
        self.psychic_projection_total = 0 # Base + Invested + STAT MOD
        self.cv_pool_total = 0        # PDBought = CAT + Invest with PD
        self.cv_spend = 0             # How many cvs spend buying features
        self.cv_innate_pool_total = 0 # Bought with CVs
        # TURN
        self.base_turn_total = 20
        
        
        # MODIFIERS (bought, modifiers, increases, etc)
        #--------------------------------------------
                # Buyable with PDs (Development points)
        # -------------------------------------------
        self.hp_multiples_invest = 0   # Using PDs
        self.attack_skill_invest = 0   # HA (Habilidad Ataque)
        self.parry_skill_invest = 0    # HP (Habilidad Parada)
        self.flee_skill_invest = 0     # HE (Habilidad Esquiva)
        self.wear_armor_invest = 0
        self.ki_pool_invest = 0        # How many ki has the character (+1)
        self.ki_act_invest = 0         # How fast ki is acumulated (+1)
        self.zeon_pool_invest = 0      # adds n * 5 zeon. Using PDs
        self.zeon_act_invest = 0       #
        self.magic_projection_invest = 0 #
        self.skill_summon_invest = 0   #
        self.skill_dominate_invest = 0 #
        self.skill_atar_invest = 0     #
        self.skill_unsummon_invest = 0 #
        self.cv_invest = 0             #
        self.psy_projection_invest = 0 #
        #--------------------------------------------
                # Modified by equipment
        #--------------------------------------------
        self.armor_turn_modifier = 0
        #--------------------------------------------
                # Modified by choice
        #--------------------------------------------
        self.magic_imbalance = 0       # positive improves attack projection, negative improves defense projection
        
        
        # Current state of the character (CURRENT)
        # -------------------------------------------
        # POOLS
        self.hp_current = 0
        self.fatigue_current = 0
        # KI
        self.ki_pool_current = 0
        self.ki_ready = 0             # How much Ki is ready to be used
        # MAGIC
        self.zeon_pool_current = 0
        self.zeon_ready = 0           # How much zeon is ready to be used
        # PSYCHIC POOLS
        self.free_cvs = 0             # Coste voluntad libres. Ready to use Willpower Cost.
        

        # Category dependant attributes
        # -------------------------------------------
        # Base
        self.hp_cat_increase = 0        # per level
        self.hp_multipe_cost = 0    # cost to get +CON Health points
        self.turn_increase = 0      # per level
        self.martial_knowledge_increase = 0 # per level
        self.innate_cv_increase_each = 0    # +1 cv each X levels
        # COMBAT SKILLS
        self.combat_skill_limit = 50  # 50 or 60 % of MAX PDs investment allowed
            # Level increase
        self.attack_incr_cat = 0    # Increase in attack skill per level (max 50)
        self.parry_incr_cat = 0     # Increase in parry skill per level (max 50)
        self.flee_incr_cat = 0      # Increase in flee skill per level (max 50)
        self.armor_wear_cat = 0     # Increase waer armor skill per level 
            # Costs
        self.attack_increase_cost = 0 # PD Cost: increase 1 attack skill (HA)
        self.parry_increase_cost = 0  # PD Cost: increse 1 parry skill (HP) 
        self.flee_increase_cost = 0   # PD Cost: increse 1 flee skill (HP)
        self.armor_proficiency_cost = 0 # PD Cost: increase 1 wear armor
        # KI SKILLS
        self.ki_acumulator_cost = 0   # PD Cost: increase 1 KI ACU in one Stat        
        # MAGIC SKILLS
        self.zeon_incr_cat = 0              # Increase in zeon pool points per level
        self.increase_zeon_cost = 0         # PD Cost: increase 5 total zeon pool
        self.magic_act_mult_cost = 0        # PD Cost: increase Magic ACT
        self.magic_projection_incr_cost = 0 # PD Cost: increase 1 magic projection
        # PSYCHIC SKILLS
        self.cv_cost = 0
        self.psychic_projection_incr_cost = 0 # PD Cost: increase +1
        
        # Added points
        # To acumulate effects of advantadges, etc.
        # ---------------------------------------------
        # Base
        self.regen_added_points = 0   
        
        # SECONDARY SKILLS 
        # PROBLEM: TOO MANY WAYS AND POINTS TO IMPROVE THIS
        # SUGGESTION: JUST USE ONE INDICATOR!
        # -------------------------------------------
        # Base (Obtained through PD investment)
        # STAT_BONUS
        # SPECIAL (Obtained)
        # CAT
        # BRANCH (Sets all costs) Category deendant
        self.athletic_branch_cost = 0
        self.social_branch_cost = 0
        self.perception_branch_cost = 0
        self.intelectual_branch_cost = 0
        self.vigor_branch_cost = 0
        self.subterfuge_branch_cost = 0
        self.creative_branch_cost = 0
        
        # PARTICULAR (Overrides the branch costs if not -1)
        # ATHLETICS
        # cost : if reduced or increased cost
        self.skill_acrobatics_cost = -1
        self.skill_athletism_cost = -1
        self.skill_mount_cost = -1
        self.skill_swim_cost = -1
        self.skill_climb_cost = -1
        self.skill_jump_cost = -1
        # Total skill (BASE + CAT + ESP + (BONOS[Max100] = STAT + INNATE1 + INNATE2))
        self.skill_acrobatics = 0
        self.skill_athletism = 0
        self.skill_mount = 0
        self.skill_swim = 0
        self.skill_climb = 0
        self.skill_jump = 0
        # BASE : bought through PD
        self.skill_acrobatics_base = 0
        self.skill_athletism_base = 0
        self.skill_mount_base = 0
        self.skill_swim_base = 0
        self.skill_climb_base = 0
        self.skill_jump_base = 0
        # CAT: category increase total
        self.skill_acrobatics_cat = 0
        self.skill_athletism_cat = 0
        self.skill_mount_cat = 0
        self.skill_swim_cat = 0
        self.skill_climb_cat = 0
        self.skill_jump_cat = 0
        # CAT: category increase per level
        self.skill_acrobatics_cat_increase = 0
        self.skill_athletism_cat_increase = 0
        self.skill_mount_cat_increase = 0
        self.skill_swim_cat_increase = 0
        self.skill_climb_cat_increase = 0
        self.skill_jump_cat_increase = 0
        # ESP: special modifiers
        self.skill_acrobatics_esp = 0
        self.skill_athletism_esp = 0
        self.skill_mount_esp = 0
        self.skill_swim_esp = 0
        self.skill_climb_esp = 0
        self.skill_jump_esp = 0
        # BONUS: total bonus (status + innate1(+10) + innate2(+stat))
        self.skill_acrobatics_bonus = 0
        self.skill_athletism_bonus = 0
        self.skill_mount_bonus = 0
        self.skill_swim_bonus = 0
        self.skill_climb_bonus = 0
        self.skill_jump_bonus = 0
        # bonus per status
        self.skill_acrobatics_bonus_stat = 0
        self.skill_athletism_bonus_stat = 0
        self.skill_mount_bonus_stat = 0
        self.skill_swim_bonus_stat = 0
        self.skill_climb_bonus_stat = 0
        self.skill_jump_bonus_stat = 0
        # bonus per innate 1 (+10)
        self.skill_acrobatics_bonus_innate1 = 0
        self.skill_athletism_bonus_innate1 = 0
        self.skill_mount_bonus_innate1 = 0
        self.skill_swim_bonus_innate1 = 0
        self.skill_climb_bonus_innate1 = 0
        self.skill_jump_bonus_innate1 = 0
        # bonus per innate 2 (+stat bonus)
        self.skill_acrobatics_bonus_innate2 = 0
        self.skill_athletism_bonus_innate2 = 0
        self.skill_mount_bonus_innate2 = 0
        self.skill_swim_bonus_innate2 = 0
        self.skill_climb_bonus_innate2 = 0
        self.skill_jump_bonus_innate2 = 0
        
        # SOCIAL BRANCH
        # cost : if reduced or increased cost
        self.skill_style_cost = -1
        self.skill_intimidate_cost = -1
        self.skill_leadership_cost = -1
        self.skill_persuation_cost = -1
        # Total skill (BASE + CAT + ESP + (BONOS[Max100] = STAT + INNATE1 + INNATE2))
        self.skill_style = 0
        self.skill_intimidate = 0
        self.skill_leadership = 0
        self.skill_persuation = 0
        # BASE : bought through PD
        self.skill_style_base = 0
        self.skill_intimidate_base = 0
        self.skill_leadership_base = 0
        self.skill_persuation_base = 0
        # CAT: category increase total (increase per level * level)
        self.skill_style_cat = 0
        self.skill_intimidate_cat = 0
        self.skill_leadership_cat = 0
        self.skill_persuation_cat = 0
        # CAT: category increase per level
        self.skill_style_cat_increase = 0
        self.skill_intimidate_cat_increase = 0
        self.skill_leadership_cat_increase = 0
        self.skill_persuation_cat_increase = 0
        # ESP: special modifiers
        self.skill_style_esp = 0
        self.skill_intimidate_esp = 0
        self.skill_leadership_esp = 0
        self.skill_persuation_esp = 0
        # BONUS: total bonus (status + innate1(+10) + innate2(+stat))
        self.skill_style_bonus = 0
        self.skill_intimidate_bonus = 0
        self.skill_leadership_bonus = 0
        self.skill_persuation_bonus = 0
        # bonus per status
        self.skill_style_bonus_stat = 0
        self.skill_intimidate_bonus_stat = 0
        self.skill_leadership_bonus_stat = 0
        self.skill_persuation_bonus_stat = 0
        # bonus per innate 1 (+10)
        self.skill_style_bonus_innate1 = 0
        self.skill_intimidate_bonus_innate1 = 0
        self.skill_leadership_bonus_innate1 = 0
        self.skill_persuation_bonus_innate1 = 0
        # bonus per innate 2 (+stat bonus)
        self.skill_style_bonus_innate2 = 0
        self.skill_intimidate_bonus_innate2 = 0
        self.skill_leadership_bonus_innate2 = 0
        self.skill_persuation_bonus_innate2 = 0
        
        # PERCEPTION BRANCH
        # cost : if reduced or increased cost
        self.skill_notice_cost = -1
        self.skill_search_cost = -1
        self.skill_track_cost = -1
        # Total skill (BASE + CAT + ESP + (BONOS[Max100] = STAT + INNATE1 + INNATE2))
        self.skill_notice = 0
        self.skill_search = 0
        self.skill_track = 0
        # BASE : bought through PD
        self.skill_notice_base = 0
        self.skill_search_base = 0
        self.skill_track_base = 0
        # CAT: category increase total
        self.skill_notice_cat = 0
        self.skill_search_cat = 0
        self.skill_track_cat = 0
        # CAT: category increase per level
        self.skill_notice_cat_increase = 0
        self.skill_search_cat_increase = 0
        self.skill_track_cat_increase = 0
        # ESP: special modifiers
        self.skill_notice_esp = 0
        self.skill_search_esp = 0
        self.skill_track_esp = 0
        # BONUS: total bonus (status + innate1(+10) + innate2(+stat))
        self.skill_notice_bonus = 0
        self.skill_search_bonus = 0
        self.skill_track_bonus = 0
        # bonus per status
        self.skill_notice_bonus_stat = 0
        self.skill_search_bonus_stat = 0
        self.skill_track_bonus_stat = 0
        # bonus per innate 1 (+10)
        self.skill_notice_bonus_innate1 = 0
        self.skill_search_bonus_innate1 = 0
        self.skill_track_bonus_innate1 = 0
        # bonus per innate 2 (+stat bonus)
        self.skill_notice_bonus_innate2 = 0
        self.skill_search_bonus_innate2 = 0
        self.skill_track_bonus_innate2 = 0
        
        # VIGOR BRANCH
        # cost : if reduced or increased cost
        self.skill_composture_cost = -1
        self.skill_feat_strengh_cost = -1
        self.skill_withstand_pain_cost = -1
        # Total skill (BASE + CAT + ESP + (BONOS[Max100] = STAT + INNATE1 + INNATE2))
        self.skill_composture = 0
        self.skill_feat_strengh = 0
        self.skill_withstand_pain = 0
        # BASE : bought through PD
        self.skill_composture_base = 0
        self.skill_feat_strengh_base = 0
        self.skill_withstand_pain_base = 0
        # CAT: category increase total
        self.skill_composture_cat = 0
        self.skill_feat_strengh_cat = 0
        self.skill_withstand_pain_cat = 0
        # CAT: category increase per level
        self.skill_composture_cat_increase = 0
        self.skill_feat_strengh_cat_increase = 0
        self.skill_withstand_pain_cat_increase = 0
        # ESP: special modifiers
        self.skill_composture_esp = 0
        self.skill_feat_strengh_esp = 0
        self.skill_withstand_pain_esp = 0
        # BONUS: total bonus (status + innate1(+10) + innate2(+stat))
        self.skill_composture_bonus = 0
        self.skill_feat_strengh_bonus = 0
        self.skill_withstand_pain_bonus = 0
        # bonus per status
        self.skill_composture_bonus_stat = 0
        self.skill_feat_strengh_bonus_stat = 0
        self.skill_withstand_pain_bonus_stat = 0
        # bonus per innate 1 (+10)
        self.skill_composture_bonus_innate1 = 0
        self.skill_feat_strengh_bonus_innate1 = 0
        self.skill_withstand_pain_bonus_innate1 = 0
        # bonus per innate 2 (+stat bonus)
        self.skill_composture_bonus_innate2 = 0
        self.skill_feat_strengh_bonus_innate2 = 0
        self.skill_withstand_pain_bonus_innate2 = 0
        
        # INTELECTUAL BRANCH
        # cost : if reduced or increased cost
        self.skill_animals_cost = -1
        self.skill_appraisal_cost = -1
        self.skill_arquitechture_cost = -1
        self.skill_herbal_lore_cost = -1
        self.skill_history_cost = -1
        self.skill_law_cost = -1
        self.skill_magic_appraisal_cost = -1
        self.skill_medicine_cost = -1
        self.skill_memorize_cost = -1
        self.skill_navigation_cost = -1
        self.skill_occultism_cost = -1
        self.skill_sciences_cost = -1
        self.skill_tactics_cost = -1
        # Total skill (BASE + CAT + ESP + (BONOS[Max100] = STAT + INNATE1 + INNATE2))
        self.skill_animals = 0
        self.skill_appraisal = 0
        self.skill_arquitechture = 0
        self.skill_herbal_lore = 0
        self.skill_history = 0
        self.skill_law = 0
        self.skill_magic_appraisal = 0
        self.skill_medicine = 0
        self.skill_memorize = 0
        self.skill_navigation = 0
        self.skill_occultism = 0
        self.skill_sciences = 0
        self.skill_tactics = 0
        # BASE : bought through PD
        self.skill_animals_base = 0
        self.skill_appraisal_base = 0
        self.skill_arquitechture_base = 0
        self.skill_herbal_lore_base = 0
        self.skill_history_base = 0
        self.skill_law_base = 0
        self.skill_magic_appraisal_base = 0
        self.skill_medicine_base = 0
        self.skill_memorize_base = 0
        self.skill_navigation_base = 0
        self.skill_occultism_base = 0
        self.skill_sciences_base = 0
        self.skill_tactics_base = 0
        # CAT: category increase total
        self.skill_animals_cat = 0
        self.skill_appraisal_cat = 0
        self.skill_arquitechture_cat = 0
        self.skill_herbal_lore_cat = 0
        self.skill_history_cat = 0
        self.skill_law_cat = 0
        self.skill_magic_appraisal_cat = 0
        self.skill_medicine_cat = 0
        self.skill_memorize_cat = 0
        self.skill_navigation_cat = 0
        self.skill_occultism_cat = 0
        self.skill_sciences_cat = 0
        self.skill_tactics_cat = 0
        # CAT: category increase per level
        self.skill_animals_cat_increase = 0
        self.skill_appraisal_cat_increase = 0
        self.skill_arquitechture_cat_increase = 0
        self.skill_herbal_lore_cat_increase = 0
        self.skill_history_cat_increase = 0
        self.skill_law_cat_increase = 0
        self.skill_magic_appraisal_cat_increase = 0
        self.skill_medicine_cat_increase = 0
        self.skill_memorize_cat_increase = 0
        self.skill_navigation_cat_increase = 0
        self.skill_occultism_cat_increase = 0
        self.skill_sciences_cat_increase = 0
        self.skill_tactics_cat_increase = 0
        # ESP: special modifiers
        self.skill_animals_esp = 0
        self.skill_appraisal_esp = 0
        self.skill_arquitechture_esp = 0
        self.skill_herbal_lore_esp = 0
        self.skill_history_esp = 0
        self.skill_law_esp = 0
        self.skill_magic_appraisal_esp = 0
        self.skill_medicine_esp = 0
        self.skill_memorize_esp = 0
        self.skill_navigation_esp = 0
        self.skill_occultism_esp = 0
        self.skill_sciences_esp = 0
        self.skill_tactics_esp = 0
        # BONUS: total bonus (status + innate1(+10) + innate2(+stat))
        self.skill_animals_bonus = 0
        self.skill_appraisal_bonus = 0
        self.skill_arquitechture_bonus = 0
        self.skill_herbal_lore_bonus = 0
        self.skill_history_bonus = 0
        self.skill_law_bonus = 0
        self.skill_magic_appraisal_bonus = 0
        self.skill_medicine_bonus = 0
        self.skill_memorize_bonus = 0
        self.skill_navigation_bonus = 0
        self.skill_occultism_bonus = 0
        self.skill_science_bonuss = 0
        self.skill_tactics_bonus = 0
        # bonus per status
        self.skill_animals_bonus_stat = 0
        self.skill_appraisal_bonus_stat = 0
        self.skill_arquitechture_bonus_stat = 0
        self.skill_herbal_lore_bonus_stat = 0
        self.skill_history_bonus_stat = 0
        self.skill_law_bonus_stat = 0
        self.skill_magic_appraisal_bonus_stat = 0
        self.skill_medicine_bonus_stat = 0
        self.skill_memorize_bonus_stat = 0
        self.skill_navigation_bonus_stat = 0
        self.skill_occultism_bonus_stat = 0
        self.skill_sciences_bonus_stat = 0
        self.skill_tactics_bonus_stat = 0
        # bonus per innate 1 (+10)
        self.skill_animals_bonus_innate1 = 0
        self.skill_appraisal_bonus_innate1 = 0
        self.skill_arquitechture_bonus_innate1 = 0
        self.skill_herbal_lore_bonus_innate1 = 0
        self.skill_history_bonus_innate1 = 0
        self.skill_law_bonus_innate1 = 0
        self.skill_magic_appraisal_bonus_innate1 = 0
        self.skill_medicine_bonus_innate1 = 0
        self.skill_memorize_bonus_innate1 = 0
        self.skill_navigation_bonus_innate1 = 0
        self.skill_occultism_bonus_innate1 = 0
        self.skill_sciences_bonus_innate1 = 0
        self.skill_tactics_bonus_innate1 = 0
        # bonus per innate 2 (+stat bonus)
        self.skill_animals_bonus_innate2 = 0
        self.skill_appraisal_bonus_innate2 = 0
        self.skill_arquitechture_bonus_innate2 = 0
        self.skill_herbal_lore_bonus_innate2 = 0
        self.skill_history_bonus_innate2 = 0
        self.skill_law_bonus_innate2 = 0
        self.skill_magic_appraisal_bonus_innate2 = 0
        self.skill_medicine_bonus_innate2 = 0
        self.skill_memorize_bonus_innate2 = 0
        self.skill_navigation_bonus_innate2 = 0
        self.skill_occultism_bonus_innate2 = 0
        self.skill_sciences_bonus_innate2 = 0
        self.skill_tactics_bonus_innate2 = 0
        
        # SUBTEFRUGE BRANCH
        # cost : if reduced or increased cost
        self.skill_lockpick_cost = -1
        self.skill_disguise_cost = -1
        self.skill_hide_cost = -1
        self.skill_stealth_cost = -1
        self.skill_traps_cost = -1
        self.skill_poison_cost = -1
        # Total skill (BASE + CAT + ESP + (BONOS[Max100] = STAT + INNATE1 + INNATE2))
        self.skill_lockpick = 0
        self.skill_disguise = 0
        self.skill_hide = 0
        self.skill_stealth = 0
        self.skill_traps = 0
        self.skill_poison = 0
        # BASE : bought through PD
        self.skill_lockpick_base = 0
        self.skill_disguise_base = 0
        self.skill_hide_base = 0
        self.skill_stealth_base = 0
        self.skill_traps_base = 0
        self.skill_poison_base = 0
        # CAT: category increase total
        self.skill_lockpick_cat = 0
        self.skill_disguise_cat = 0
        self.skill_hide_cat = 0
        self.skill_stealth_cat = 0
        self.skill_traps_cat = 0
        self.skill_poison_cat = 0
        # CAT: category increase per level
        self.skill_lockpick_cat_increase = 0
        self.skill_disguise_cat_increase = 0
        self.skill_hide_cat_increase = 0
        self.skill_stealth_cat_increase = 0
        self.skill_trap_cat_increases = 0
        self.skill_poison_cat_increase = 0
        # ESP: special modifiers
        self.skill_lockpick_esp = 0
        self.skill_disguise_esp = 0
        self.skill_hide_esp = 0
        self.skill_stealth_esp = 0
        self.skill_trap_esp = 0
        self.skill_poison_esp = 0
        # BONUS: total bonus (status + innate1(+10) + innate2(+stat))
        self.skill_lockpick_bonus = 0
        self.skill_disguise_bonus = 0
        self.skill_hide_bonus = 0
        self.skill_stealth_bonus = 0
        self.skill_traps_bonus = 0
        self.skill_poison_bonus = 0
        # bonus per status
        self.skill_lockpick_bonus_stat = 0
        self.skill_disguise_bonus_stat = 0
        self.skill_hide_bonus_stat = 0
        self.skill_stealth_bonus_stat = 0
        self.skill_traps_bonus_stat = 0
        self.skill_poison_bonus_stat = 0
        # bonus per innate 1 (+10)
        self.skill_lockpick_bonus_innate1 = 0
        self.skill_disguise_bonus_innate1 = 0
        self.skill_hide_bonus_innate1 = 0
        self.skill_stealth_bonus_innate1 = 0
        self.skill_trap_bonus_innate1 = 0
        self.skill_poison_bonus_innate1 = 0
        # bonus per innate 2 (+stat bonus)
        self.skill_lockpick_bonus_innate2 = 0
        self.skill_disguise_bonus_innate2 = 0
        self.skill_hide_bonus_innate2 = 0
        self.skill_stealth_bonus_innate2 = 0
        self.skill_traps_bonus_innate2 = 0
        self.skill_poison_bonus_innate2 = 0
        
        # CREATIVE BRANCH
        # cost : if reduced or increased cost
        self.skill_art_cost = -1
        self.skill_dance_cost = -1
        self.skill_forge_cost = -1
        self.skill_music_cost = -1
        self.skill_sleight_of_hand_cost = -1
        # Total skill (BASE + CAT + ESP + (BONOS[Max100] = STAT + INNATE1 + INNATE2))
        self.skill_art = 0
        self.skill_dance = 0
        self.skill_forge = 0
        self.skill_music = 0
        self.skill_sleight_of_hand = 0
        # BASE : bought through PD
        self.skill_art_base = 0
        self.skill_dance_base = 0
        self.skill_forge_base = 0
        self.skill_music_base = 0
        self.skill_sleight_of_hand_base = 0
        # CAT: category increase total
        self.skill_art_cat = 0
        self.skill_dance_cat = 0
        self.skill_forge_cat = 0
        self.skill_music_cat = 0
        self.skill_sleight_of_hand_cat = 0
        # CAT: category increase per level
        self.skill_art_cat_increase = 0
        self.skill_dance_cat_increase = 0
        self.skill_forge_cat_increase = 0
        self.skill_music_cat_increase = 0
        self.skill_sleight_of_hand_cat_increase = 0
        # ESP: special modifiers
        self.skill_art_esp = 0
        self.skill_dance_esp = 0
        self.skill_forge_esp = 0
        self.skill_music_esp = 0
        self.skill_sleight_of_hand_esp = 0
        # BONUS: total bonus (status + innate1(+10) + innate2(+stat))
        self.skill_art_bonus = 0
        self.skill_dance_bonus = 0
        self.skill_forge_bonus = 0
        self.skill_music_bonus = 0
        self.skill_sleight_of_hand_bonus = 0
        # bonus per status
        self.skill_art_bonus_stat = 0
        self.skill_dance_bonus_stat = 0
        self.skill_forge_bonus_stat = 0
        self.skill_music_bonus_stat = 0
        self.skill_sleight_of_hand_bonus_stat = 0
        # bonus per innate 1 (+10)
        self.skill_art_bonus_innate1 = 0
        self.skill_dance_bonus_innate1 = 0
        self.skill_forge_bonus_innate1 = 0
        self.skill_music_bonus_innate1 = 0
        self.skill_sleight_of_hand_bonus_innate1 = 0
        # bonus per innate 2 (+stat bonus)
        self.skill_art_bonus_innate2 = 0
        self.skill_dance_bonus_innate2 = 0
        self.skill_forge_bonus_innate2 = 0
        self.skill_music_bonus_innate2 = 0
        self.skill_sleight_of_hand_bonus_innate2 = 0
        
        
        # EQUIPMENT STATS
        # OFFENSIVE
        self.weapon_name = ""
        self.weapon_damage = 0
        self.weapon_turn = 0
        self.weapon_str_req = 0
        self.weapon_crit_1 = weaponCritType.NONE
        self.weapon_crit_2 = weaponCritType.NONE
        self.weapon_type = weaponType.NONE
        self.weapon_special = ""
        self.weapon_quality = 0    # Calidad
        self.weapon_presence = 0   # Presencia
        self.weapon_fortitude = 0  # Entereza
        self.weapon_breakage = 0   # Rotura
        
        # DEFENSIVE
        self.armor_at_cut = 0
        self.armor_at_imp = 0
        self.armor_at_thr = 0
        self.armor_at_hea = 0
        self.armor_at_col = 0
        self.armor_at_ele = 0
        self.armor_at_ene = 0
        self.armor_requirement = 0
        self.armor_perception_pen = 0
        self.armor_fortitude = 0
        self.armor_presence = 0
        self.armor_location = armorLocation.NONE
        self.armor_type = armorType.NONE

    #
    #  PERSISTENCE
    #
    #
    #
    def loadChara(self, saveFile):
        #Load character sheet
        print("Load Character")
        
    def saveChara(self):
        #Save character sheet
        print("Save Character")

    #
    #  SETTERS
    #
    #
    #        
    def setNewCategory(self, cat, catlevel):
        # set costs, benefits, bonus and others depending on category
        print("set category")
        if (self.category1 == categoryType.NONE):
            self.category1 = cat
            self.levelcat1 = catlevel
        elif (self.category2 == categoryType.NONE):
            self.category2 = cat
            self.levelcat2 = catlevel
        else:
            self.category3 = cat
            self.levelcat3 = catlevel
        self.level = self.level1 + self.level2 + self.level3
        self.category = cat
        self.recalculate()
            
    def setCategoryLevel(self, cat, catlevel):
        print("set category")
        if (self.category1 == cat):
            self.levelcat1 = catlevel
        elif (self.category2 == cat):
            self.levelcat2 = catlevel
        elif (self.category3 == cat):
            self.levelcat3 = catlevel
        else:
            print("Category not found (", cat, "). Use one of the characters categories.")
            return
        self.level = self.level1 + self.level2 + self.level3
        self.recalculate()
    
    def setLevel(self, level):
        # sets level
        if (level > 0 and level < 21):
            self.level = level
        else:
            print("Invalid level value, use 1-20")
        
    def setSecondarySkill(self, skill, base):
        # Set values to SecondarySkills
        print("setSecondarySkills")

    #
    #  GETTERS
    #
    #     
    def getSecondarySkill(self, skill):
        print("returns total skill value")
        value = 0
        return value

    #
    #  FUNCTIONALITIES
    #
    #
    #   
    def addExp(self, exp):
        self.level_exp = self.level_exp + exp
        self.acumulated_exp = self.acumulated_exp + exp
    
    def calculateMovementBase(self):
        self.movement_stat_base = self.agility
        if self.movement_stat_base == 1:
            self.movement_value = 1
        elif self.movement_stat_base == 2:
            self.movement_value = 4
        elif self.movement_stat_base == 3:
            self.movement_value = 8
        elif self.movement_stat_base == 4:
            self.movement_value = 15
        elif self.movement_stat_base == 5:
            self.movement_value = 20
        elif self.movement_stat_base == 6:
            self.movement_value = 22
        elif self.movement_stat_base == 7:
            self.movement_value = 25
        elif self.movement_stat_base == 8:
            self.movement_value = 28
        elif self.movement_stat_base == 9:
            self.movement_value = 32
        elif self.movement_stat_base == 10:
            self.movement_value = 35
        elif self.movement_stat_base == 11:
            self.movement_value = 40
        elif self.movement_stat_base == 12:
            self.movement_value = 50
        elif self.movement_stat_base == 13:
            self.movement_value = 80
        elif self.movement_stat_base == 14:
            self.movement_value = 150
        elif self.movement_stat_base == 15:
            self.movement_value = 250
        elif self.movement_stat_base == 16:
            self.movement_value = 500
        elif self.movement_stat_base == 17:
            self.movement_value = 1000
        elif self.movement_stat_base == 18:
            self.movement_value = 5000
        elif self.movement_stat_base == 19:
            self.movement_value = 25000
        elif self.movement_stat_base == 20:
            self.movement_value = 50000
        if (self.showBaseStats):
            print("Movement Base: ", self.movement_value, " meters per turn.")
   
    def calculateHPBase(self):
        if self.constitution == 1:
            self.hp_base = 5
        elif self.constitution == 2:
            self.hp_base = 20
        elif self.constitution == 3:
            self.hp_base = 40
        elif self.constitution == 4:
            self.hp_base = 55
        elif self.constitution == 5:
            self.hp_base = 70
        elif self.constitution == 6:
            self.hp_base = 85
        elif self.constitution == 7:
            self.hp_base = 95
        elif self.constitution == 8:
            self.hp_base = 110
        elif self.constitution == 9:
            self.hp_base = 120
        elif self.constitution == 10:
            self.hp_base = 135
        elif self.constitution == 11:
            self.hp_base = 150
        elif self.constitution == 12:
            self.hp_base = 160
        elif self.constitution == 13:
            self.hp_base = 175
        elif self.constitution == 14:
            self.hp_base = 185
        elif self.constitution == 15:
            self.hp_base = 200
        elif self.constitution == 16:
            self.hp_base = 215
        elif self.constitution == 17:
            self.hp_base = 225
        elif self.constitution == 18:
            self.hp_base = 240
        elif self.constitution == 19:
            self.hp_base = 250
        elif self.constitution == 20:
            self.hp_base = 260
        else:
            print("ERROR - Invalida constitution value:", self.constitution)
            return    
        if (self.showBaseStats):
            print("HP Base:", self.hp_base)
        
    def calculatePresenceAndResistances(self):
        self.presence = 30 + 5*self.level
        self.RF = self.presence + self.con_bonus
        self.RV = self.presence + self.con_bonus
        self.RM = self.presence + self.pow_bonus
        self.RE = self.presence + self.con_bonus
        self.RP = self.presence + self.will_bonus
        print("Presence: ", self.presence)
        print("RF: ", self.RF)
        print("RV: ", self.RV)
        print("RM: ", self.RM)
        print("RE: ", self.RE)
        print("RP: ", self.RP)        
    
    def calculateStatBonus(self, stateValue, stateName):
        # stablish stateBonus
        stateBonus = 0
        if stateValue == 1:
            stateBonus = -30
        elif stateValue == 2:
            stateBonus = -20
        elif stateValue == 3:
            stateBonus = -10
        elif stateValue == 4:
            stateBonus = -5
        elif stateValue == 5:
            stateBonus = 0
        elif stateValue == 6 or stateValue == 7:
            stateBonus = 5
        elif stateValue == 8 or stateValue == 9:
            stateBonus = 10
        elif stateValue == 10:
            stateBonus = 15
        elif stateValue == 11 or stateValue == 12:
            stateBonus = 20
        elif stateValue == 13 or stateValue == 14:
            stateBonus = 25
        elif stateValue == 15:
            stateBonus = 30
        elif stateValue == 16 or stateValue == 17:
            stateBonus = 35
        elif stateValue == 18 or stateValue == 19:
            stateBonus = 40
        elif stateValue == 20:
            stateBonus = 45
        else:
            stateBonus = -500
            print("ERROR - Invalid status value for", stateName)
        # SET VALUE AS STATUS BONUS
        if stateName == "strenght":
            self.str_bonus = stateBonus
        elif stateName == "agility":
            self.agi_bonus = stateBonus
        elif stateName == "dexterity":
            self.dex_bonus = stateBonus
        elif stateName == "constitution":
            self.con_bonus = stateBonus
        elif stateName == "perception":
            self.per_bonus = stateBonus
        elif stateName == "intelligence":
            self.int_bonus = stateBonus
        elif stateName == "willpower":
            self.will_bonus = stateBonus
        elif stateName == "power":
            self.pow_bonus = stateBonus
        else:
            print("ERROR - invalid stateName: ", stateName)
        if stateBonus >= 0:
            print(stateValue, "( +", stateBonus, ")", stateName)
        else:
            print(stateValue, "(", stateBonus, ")", stateName)
        
    def calculateRegenerationBase(self):
        if self.constitution == 1 or self.constitution == 2:
            self.regen_base = 0
        elif self.constitution > 2 and self.constitution < 8:
            self.regen_base = 1
        elif self.constitution == 8 or self.constitution == 9:
            self.regen_base = 2
        elif self.constitution == 10:
            self.regen_base = 3
        elif self.constitution == 11:
            self.regen_base = 4
        elif self.constitution == 12:
            self.regen_base = 5
        elif self.constitution == 13:
            self.regen_base = 6
        elif self.constitution == 14:
            self.regen_base = 7
        elif self.constitution == 15:
            self.regen_base = 8
        elif self.constitution == 16:
            self.regen_base = 9
        elif self.constitution == 17:
            self.regen_base = 10
        elif self.constitution == 18:
            self.regen_base = 11
        elif self.constitution == 19 or self.constitution == 20:
            self.regen_base = 12
        else:
            print("ERROR - Invalid constitution value.")
            self.regen_base = -1000
        if (self.showBaseStats):
            print("Regen Base: ", self.regen_base)
        
    def calculatePsyPotential(self):
        if self.willpower > 0 and self.willpower <= 4:
            self.psychic_potential_base = 0
        elif self.willpower == 5:
            self.psychic_potential_base = 10
        elif self.willpower == 6:
            self.psychic_potential_base = 20
        elif self.willpower == 7:
            self.psychic_potential_base = 30
        elif self.willpower == 8:
            self.psychic_potential_base = 40
        elif self.willpower == 9:
            self.psychic_potential_base = 50
        elif self.willpower == 10:
            self.psychic_potential_base = 60
        elif self.willpower == 11:
            self.psychic_potential_base = 70
        elif self.willpower == 12:
            self.psychic_potential_base = 80
        elif self.willpower == 13:
            self.psychic_potential_base = 90
        elif self.willpower == 14:
            self.psychic_potential_base = 100
        elif self.willpower == 15:
            self.psychic_potential_base = 120
        elif self.willpower == 16:
            self.psychic_potential_base = 140
        elif self.willpower == 17:
            self.psychic_potential_base = 160
        elif self.willpower == 18:
            self.psychic_potential_base = 180
        elif self.willpower == 19:
            self.psychic_potential_base = 200
        elif self.willpower == 20:
            self.psychic_potential_base = 220
        else:
            print("ERROR - Invalid willpower value:", self.willpower)
        if (self.showBaseStats):
            print("Psychic Potential Base:", self.psychic_potential_base)
        
    def calculateRegenStats(self):
        # calculate final regen
        self.regen_final = self.regen_base + self.regen_added_points
        
        if self.regen_final == 1:
            self.regen_hp_resting = 10
            self.regen_hp_unrest = 5
            self.negative_reduction = 5
            self.regen_effect = "No effect."
        
        elif self.regen_final == 2:
            self.regen_hp_resting = 20
            self.regen_hp_unrest = 10
            self.negative_reduction = 5   
            self.regen_effect = "No effect."
        
        elif self.regen_final == 3:
            self.regen_hp_resting = 30
            self.regen_hp_unrest = 15
            self.negative_reduction = 5
            self.regen_effect = "No effect."
        
        elif self.regen_final == 4:
            self.regen_hp_resting = 40
            self.regen_hp_unrest = 20
            self.negative_reduction = 10
            self.regen_effect = "No effect."
            
        elif self.regen_final == 5:
            self.regen_hp_resting = 50
            self.regen_hp_unrest = 25
            self.negative_reduction = 10
            self.regen_effect = "No scars remain."
        
        elif self.regen_final == 6:
            self.regen_hp_resting = 75
            self.regen_hp_unrest = 30
            self.negative_reduction = 15   
            self.regen_effect = "Inmune to bleeding effects."
        
        elif self.regen_final == 7:
            self.regen_hp_resting = 100
            self.regen_hp_unrest = 50
            self.negative_reduction = 20
            self.regen_effect = "Clean amputated attached limbs heal in a week."
        
        elif self.regen_final == 8:
            self.regen_hp_resting = 250
            self.regen_hp_unrest = 100
            self.negative_reduction = 25
            self.regen_effect = "Clean amputated attached limbs heal in 5 days."
        
        elif self.regen_final == 9:
            self.regen_hp_resting = 500
            self.regen_hp_unrest = 200
            self.negative_reduction = 30   
            self.regen_effect = "Clean amputated attached limbs heal in 3 days. Automatically overcome between life and death status."
        
        elif self.regen_final == 10:
            self.regen_hp_resting = 1440
            self.regen_hp_unrest = 1440
            self.negative_reduction = 40   
            self.regen_effect = "Heals 1HP/min. Clean amputated attached limbs heal in 1 days. Automatically overcome between life and death status."
        
        elif self.regen_final == 11:
            self.regen_hp_resting = 2880
            self.regen_hp_unrest = 2880
            self.negative_reduction = 50   
            self.regen_effect = "Heals 2HP/min. Any amputated limbs rests heal in 7 days. Automatically overcome between life and death status."
        
        elif self.regen_final == 12:
            self.regen_hp_resting = 7200
            self.regen_hp_unrest = 7200
            self.negative_reduction = 120
            self.regen_effect = "Heals 5HP/min. Any amputated limbs rests heal in 3 days. Automatically overcome between life and death status."
        
        elif self.regen_final == 13:
            self.regen_hp_resting = 14440
            self.regen_hp_unrest = 14440
            self.negative_reduction = 240  
            self.regen_effect = "Heals 10HP/min. Any amputated limbs rests heal in 1 days. Automatically overcome between life and death status."
        
        elif self.regen_final == 14:
            self.regen_hp_resting = 28800
            self.regen_hp_unrest = 28800
            self.negative_reduction = 360
            self.regen_effect = "Heals 1HP/assault. Any member rests attached heals in hours. Automatically overcome between life and death status."
        
        elif self.regen_final == 15:
            self.regen_hp_resting = 144000
            self.regen_hp_unrest = 144000
            self.negative_reduction = 480
            self.regen_effect = "Heals 5HP/assault. Any member rests attached heals in one assault. Any member lost (except head) regrow in 1 week. Automatically overcome between life and death status."
            
        elif self.regen_final == 16:
            self.regen_hp_resting = 288000
            self.regen_hp_unrest = 288000
            self.negative_reduction = 1440
            self.regen_effect = "Heals 10HP/assault. Any member lost (except head) regrow in 1 day. Automatically overcome between life and death status."
        
        elif self.regen_final == 17:
            self.regen_hp_resting = 720000
            self.regen_hp_unrest = 720000
            self.negative_reduction = 288000
            self.regen_effect = "Heals 25HP/assault. Recover 10 negative/assault. Any member lost (except head) regrow in few minutes. Automatically overcome between life and death status."
        
        elif self.regen_final == 18:
            self.regen_hp_resting = 1440000
            self.regen_hp_unrest = 1440000
            self.negative_reduction = 720000
            self.regen_effect = "Heals 50HP/assault. Recover 25 negative/assault. Any member lost (except head) regrow in few assaults. Automatically overcome between life and death status."
            
        elif self.regen_final == 19:
            self.regen_hp_resting = 2880000
            self.regen_hp_unrest = 2880000
            self.negative_reduction = 100000000
            self.regen_effect = "Heals 100HP/assault. Inmune to negatives. Any member lost (except head) regrow in 1 assault. Automatically overcome between life and death status."
        
        elif self.regen_final == 20:
            self.regen_hp_resting = 7200000
            self.regen_hp_unrest = 7200000
            self.negative_reduction = 100000000
            self.regen_effect = "Heals 250HP/assault. Inmune to critical attacks."
            
        else:
            print("ERROR- Invalid final regeneration score:", self.regen_final)
            self.regen_hp_resting = 50
            self.regen_hp_unrest = 25
            self.negative_reduction = 10
            self.regen_effect = "No scars remain."
        
        print("Final Regeneration score:", self.regen_final)
        print("Daily HP regen resting: ", self.regen_hp_resting)
        print("Daily HP regen without rest: ", self.regen_hp_unrest)
        print("Daily negative reduction: ", self.negative_reduction)
        print("Regeneration especial effect:", self.regen_effect)
            
        
    def calculateActionsXTurnBase(self):
        value = self.dexterity + self.agility
        if value >= 1 and value < 11:
            self.actions_x_turn_base = 1
        elif value >= 11 and value < 15:
            self.actions_x_turn_base = 2
        elif value >= 15 and value < 20:
            self.actions_x_turn_base = 3
        elif value >= 20 and value < 23:
            self.actions_x_turn_base = 4
        elif value >= 23 and value < 26:
            self.actions_x_turn_base = 5
        elif value >= 26 and value < 29:
            self.actions_x_turn_base = 6
        elif value >= 29 and value < 32:
            self.actions_x_turn_base = 8
        elif value >= 32:
            self.actions_x_turn_base = 10
        else:
            print("Invalid dex+agi value:", self.value)
            self.actions_x_turn_base = -1000
        print("Actions per turn: ", self.actions_x_turn_base)
        
    def calculateZeonBase(self):
        if self.power == 1:
            self.zeon_pool_base = 5
        elif self.power == 2:
            self.zeon_pool_base = 20
        elif self.power == 3:
            self.zeon_pool_base = 40
        elif self.power == 4:
            self.zeon_pool_base = 55
        elif self.power == 5:
            self.zeon_pool_base = 70
        elif self.power == 6:
            self.zeon_pool_base = 85
        elif self.power == 7:
            self.zeon_pool_base = 95
        elif self.power == 8:
            self.zeon_pool_base = 110
        elif self.power == 9:
            self.zeon_pool_base = 120
        elif self.power == 10:
            self.zeon_pool_base = 135
        elif self.power == 11:
            self.zeon_pool_base = 150
        elif self.power == 12:
            self.zeon_pool_base = 160
        elif self.power == 13:
            self.zeon_pool_base = 175
        elif self.power == 14:
            self.zeon_pool_base = 185
        elif self.power == 15:
            self.zeon_pool_base = 200
        elif self.power == 16:
            self.zeon_pool_base = 215
        elif self.power == 17:
            self.zeon_pool_base = 225
        elif self.power == 18:
            self.zeon_pool_base = 240
        elif self.power == 19:
            self.zeon_pool_base = 250
        elif self.power == 20:
            self.zeon_pool_base = 265
        else:
            print("ERROR - Invalid power stat: ", self.power)
            self.zeon_pool_base = -1000
        if (self.showBaseStats):
            print("Zeon Base: ", self.zeon_pool_base)
        
    def calculateMagicACTBase(self):
        if self.power >=1 and self.power <5:
            self.magic_act_base = 0
        elif self.power >= 5 and self.power < 8:
            self.magic_act_base = 5
        elif self.power >= 8 and self.power < 12:
            self.magic_act_base = 10
        elif self.power >= 12 and self.power < 15:
            self.magic_act_base = 15
        elif self.power == 15:
            self.magic_act_base = 20
        elif self.power >= 16 and self.power < 18:
            self.magic_act_base = 25
        elif self.power >= 18 and self.power < 20:
            self.magic_act_base = 30
        elif self.power == 20:
            self.magic_act_base = 35
        else:
            print("ERROR- Invalid power value:", self.power)
            self.magic_act_base = -1000
        if (self.showBaseStats):
            print("Magic ACT Base: ", self.magic_act_base)
        
    def calculateInnateMagicBase(self):
        if self.magic_ACT_tocal < 10:
            self.innate_magic_base = 0
        elif self.magic_ACT_total >= 10 and self.magic_ACT_total < 55:
            self.innate_magic_base = 10
        elif self.magic_ACT_total >= 55 and self.magic_ACT_total < 75:
            self.innate_magic_base = 20
        elif self.magic_ACT_total >= 75 and self.magic_ACT_total < 95:
            self.innate_magic_base = 30
        elif self.magic_ACT_total >= 95 and self.magic_ACT_total < 115:
            self.innate_magic_base = 40
        elif self.magic_ACT_total >= 115 and self.magic_ACT_total < 135:
            self.innate_magic_base = 50
        elif self.magic_ACT_total >= 135 and self.magic_ACT_total < 155:
            self.innate_magic_base = 60
        elif self.magic_ACT_total >= 155 and self.magic_ACT_total < 185:
            self.innate_magic_base = 70
        elif self.magic_ACT_total >= 185 and self.magic_ACT_total < 200:
            self.innate_magic_base = 80
        elif self.magic_ACT_total >= 200:
            self.innate_magic_base = 90
        else:
            print("ERROR - Invalid magic ACT value:", self.magic_act_base)
            self.innate_magic_base = -1000            
        if (self.showBaseStats):
            print("Innate Magic Base: ", self.innate_magic_base)
        
    def calculateMagicLevelBase(self):
        if self.intelligence >= 1 and self.intelligence < 6:
            self.magic_levels_base = 0
        elif self.intelligence == 6:
            self.magic_levels_base = 10
        elif self.intelligence == 7:
            self.magic_levels_base = 20
        elif self.intelligence == 8:
            self.magic_levels_base = 30
        elif self.intelligence == 9:
            self.magic_levels_base = 40
        elif self.intelligence == 10:
            self.magic_levels_base = 50
        elif self.intelligence == 11:
            self.magic_levels_base = 75
        elif self.intelligence == 12:
            self.magic_levels_base = 100
        elif self.intelligence == 13:
            self.magic_levels_base = 150
        elif self.intelligence == 14:
            self.magic_levels_base = 200
        elif self.intelligence == 15:
            self.magic_levels_base = 300
        elif self.intelligence == 16:
            self.magic_levels_base = 400
        elif self.intelligence == 17:
            self.magic_levels_base = 500
        elif self.intelligence == 18:
            self.magic_levels_base = 600
        elif self.intelligence == 19:
            self.magic_levels_base = 700
        elif self.intelligence == 20:
            self.magic_levels_base = 800
        else:
            print("ERROR - Invalid intelligence value:", self.intelligence)
            self.magic_levels_base = -1000     
        if (self.showBaseStats):
            print("Magic Levels Base: ", self.magic_levels_base)
        
    def calculateCarryWeight(self):
        weightIndex = self.strenght
        
        if weightIndex == 1:
            self.carry_weight = 1
            self.lift_weight = 1
        elif weightIndex == 2:
            self.carry_weight = 5
            self.lift_weight = 10
        elif weightIndex == 3:
            self.carry_weight = 10
            self.lift_weight = 20
        elif weightIndex == 4:
            self.carry_weight = 15
            self.lift_weight = 40
        elif weightIndex == 5:
            self.carry_weight = 25
            self.lift_weight = 60
        elif weightIndex == 6:
            self.carry_weight = 40
            self.lift_weight = 120
        elif weightIndex == 7:
            self.carry_weight = 60
            self.lift_weight = 180
        elif weightIndex == 8:
            self.carry_weight = 80
            self.lift_weight = 260
        elif weightIndex == 9:
            self.carry_weight = 100
            self.lift_weight = 350
        elif weightIndex == 10:
            self.carry_weight = 150
            self.lift_weight = 420
        elif weightIndex == 11:
            self.carry_weight = 200
            self.lift_weight = 600
        elif weightIndex == 12:
            self.carry_weight = 350
            self.lift_weight = 1000
        elif weightIndex == 13:
            self.carry_weight = 1000
            self.lift_weight = 3000
        elif weightIndex == 14:
            self.carry_weight = 5000
            self.lift_weight = 25000
        elif weightIndex == 15:
            self.carry_weight = 15000
            self.lift_weight = 100000
        elif weightIndex == 16:
            self.carry_weight = 100000
            self.lift_weight = 500000
        elif weightIndex == 17:
            self.carry_weight = 500000
            self.lift_weight = 2500000
        elif weightIndex == 18:
            self.carry_weight = 1000000
            self.lift_weight = 10000000
        elif weightIndex == 19:
            self.carry_weight = 10000000
            self.lift_weight = 150000000
        elif weightIndex == 20:
            self.carry_weight = 99999999
            self.lift_weight = 999999999
        else:
            print("ERROR - Invalid strenght value:", self.strenght)
        print("Carry weight:", self.carry_weight, "Kg.")
        print("Lift weight:", self.lift_weight, "Kg.")
    
    def calculateSize(self):
        self.size = self.strenght + self.constitution
        minHeight = 0
        maxHeight = 250
        minWeight = 5
        maxWeight = 450
        
        if self.size == 2:
            minHeight = 20
            maxHeight = 60
            minWeight = 5
            maxWeight = 15
        elif self.size == 3:
            minHeight = 40
            maxHeight = 60
            minWeight = 10
            maxWeight = 20      
        elif self.size == 4:
            minHeight = 60
            maxHeight = 100
            minWeight = 20
            maxWeight = 30
        elif self.size == 5:
            minHeight = 80
            maxHeight = 120
            minWeight = 20
            maxWeight = 50
        elif self.size == 6:
            minHeight = 100
            maxHeight = 140
            minWeight = 30
            maxWeight = 50
        elif self.size == 7:
            minHeight = 110
            maxHeight = 150
            minWeight = 30
            maxWeight = 60
        elif self.size == 8:
            minHeight = 120
            maxHeight = 160
            minWeight = 35
            maxWeight = 70
        elif self.size == 9:
            minHeight = 130
            maxHeight = 160
            minWeight = 40
            maxWeight = 80
        elif self.size == 10:
            minHeight = 140
            maxHeight = 170
            minWeight = 40
            maxWeight = 90
        elif self.size == 11:
            minHeight = 140
            maxHeight = 180
            minWeight = 50
            maxWeight = 100
        elif self.size == 12:
            minHeight = 150
            maxHeight = 180
            minWeight = 50
            maxWeight = 120
        elif self.size == 13:
            minHeight = 150
            maxHeight = 180
            minWeight = 50
            maxWeight = 140
        elif self.size == 14:
            minHeight = 160
            maxHeight = 190
            minWeight = 50
            maxWeight = 150
        elif self.size == 15:
            minHeight = 160
            maxHeight = 200
            minWeight = 60
            maxWeight = 180
        elif self.size == 16:
            minHeight = 170
            maxHeight = 210
            minWeight = 70
            maxWeight = 220
        elif self.size == 17:
            minHeight = 170
            maxHeight = 210
            minWeight = 80
            maxWeight = 240
        elif self.size == 18:
            minHeight = 180
            maxHeight = 220
            minWeight = 90
            maxWeight = 260
        elif self.size == 19:
            minHeight = 190
            maxHeight = 230
            minWeight = 100
            maxWeight = 280
        elif self.size == 20:
            minHeight = 200
            maxHeight = 240
            minWeight = 110
            maxWeight = 320
        elif self.size == 21:
            minHeight = 210
            maxHeight = 260
            minWeight = 120
            maxWeight = 450
        elif self.size == 22:
            minHeight = 250
            maxHeight = 280
            minWeight = 400
            maxWeight = 600
        else:
            print("ERROR - Invalid size value:", self.size)
        self.height = randint(minHeight, maxHeight)
        self.weight = minWeight + (0.1 * randint(maxWeight-100, maxWeight))
        print("Size:", self.size)
        print("Weight:", self.weight, "Kg")
        print("Height:", self.height, "Cm")

        
    def calculateKiPoolStatAport(self, value):
        if value >= 1 and value < 10:
            return value
        elif value > 10:
            return (10 + ((value - 10)*2))
        else:
            return 0
        
    def calculateKiACTStatAport(self, value):
        if value > 0 and value < 10:
            return 1
        elif value >= 10 and value < 13:
            return 2
        elif value >= 13 and value < 16:
            return 3
        elif value >= 16:
            return 4
        else:
            print("ERROR - stat value invalid:", value)
            return 0
        
    def calculateKi(self):
        kipool = 0
        kiact = 0
        
        # KI pool
        str_aport = self.calculateKiPoolStatAport(self.strenght + self.str_modifier)
        agi_aport = self.calculateKiPoolStatAport(self.agility + self.agi_modifier)
        dex_aport = self.calculateKiPoolStatAport(self.dexterity + self.dex_modifier)
        con_aport = self.calculateKiPoolStatAport(self.constitution + self.con_modifier)
        pow_aport = self.calculateKiPoolStatAport(self.power + self.pow_modifier)
        wil_aport = self.calculateKiPoolStatAport(self.willpower + self.will_modifier)
        kipool = str_aport + agi_aport + dex_aport + con_aport + pow_aport + wil_aport
        
        # KI ACT
        str_aport = self.calculateKiACTStatAport(self.strenght + self.str_modifier)
        agi_aport = self.calculateKiACTStatAport(self.agility + self.agi_modifier)
        dex_aport = self.calculateKiACTStatAport(self.dexterity + self.dex_modifier)
        con_aport = self.calculateKiACTStatAport(self.constitution + self.con_modifier)
        pow_aport = self.calculateKiACTStatAport(self.power + self.pow_modifier)
        wil_aport = self.calculateKiACTStatAport(self.willpower + self.will_modifier)
        kiact = str_aport + agi_aport + dex_aport + pow_aport + wil_aport
        
        self.ki_pool_base = kipool
        self.ki_act_base = kiact
        if self.showBaseStats:
            print("Ki Pool Base:", self.ki_pool_base)
            print("Ki ACT Base:", self.ki_act_base)
         
    def fatigueActionNegatives(self):
        if self.fatigue_current == 0:
            return -120
        elif self.fatigue_current == 1:
            return -80
        elif self.fatigue_current == 2:
            return -40
        elif self.fatigue_current == 3:
            return -20
        elif self.fatigue_current == 4:
            return -10
        elif self.fatigue_current < 0:
            print("ERROR - Invalid Fatigue value:", self.fatigue_current)
            return -120
        else:
            return 0
           
    def calculateTotals(self):
        self.hp_total = self.hp_base + self.hp_multiples_invest*self.constitution + self.hp_cat_increase
        print("HP Total: ", self.hp_total)
        self.innate_magic_total = self.innate_magic_base #+ spheres + objects
        
        
    def calculateALLstatBonus(self):
        self.calculateStatBonus(self.strenght, "strenght")
        self.calculateStatBonus(self.agility, "agility")
        self.calculateStatBonus(self.dexterity, "dexterity")
        self.calculateStatBonus(self.constitution, "constitution")
        self.calculateStatBonus(self.perception, "perception")
        self.calculateStatBonus(self.intelligence, "intelligence")
        self.calculateStatBonus(self.willpower, "willpower")
        self.calculateStatBonus(self.power, "power")
    
    def calculateStateDependants(self):
        self.calculateHPBase()
        self.calculateSize()
        self.fatigue_base = self.constitution
        if (self.showBaseStats):
            print("Fatigue Base: ", self.fatigue_base)
        self.calculateCarryWeight()
        self.calculateMovementBase()
        self.calculateRegenerationBase()
        self.calculateRegenStats()
        self.calculateActionsXTurnBase()
        # KI
        self.calculateKi()
        # Magical
        self.calculateZeonBase()
        self.calculateMagicACTBase()
        self.calculateMagicLevelBase()
        # PSY
        self.calculatePsyPotential()
    
    def recalculateALL(self):
        # calculates all the variables with current information
        # Level
        if self.level < 1 or self.level > 20:
            self.setLevel(1)
            
        # ADD Advantage bonus
        
        # REMOVE Disadvantage bonus
            
        # Calculate finals
        self.calculateTotals()
        
        # Calculate state dependants
        self.calculateALLstatBonus()
        self.calculatePresenceAndResistances()
        self.calculateStateDependants()
        
        # SECONDARY SKILLS
        # Calculate Bonus = stat bonus + innate 1 + innate 2
        self.skill_acrobatics_bonus_stat = self.agi_bonus
        self.skill_acrobatics_bonus = self.skill_acrobatics_bonus_stat + self.skill_acrobatics_bonus_innate1 + self.skill_acrobatics_bonus_innate2
        if (self.skill_acrobatics_bonus > 100):
            print("WARNING: Bonus on skill acrobatics is greater than 100. Set to 100.")
            self.skill_acrobatics_bonus = 100;
        # Calculate CAT = cat_increase * level
        # WARNING: Does not take in consideration multiclass
        self.skill_acrobatics_cat = self.skill_acrobatics_cat_increase * self.level
        # Calculate Final skill: BASE + BONUS + CAT + ESP
        self.skill_acrobatics = self.skill_acrobatics_base + self.skill_acrobatics_bonus + self.skill_acrobatics_cat + self.skill_acrobatics_esp
    
    def diceRoll(self, dice):
        result = 0
        if dice == "d10":
            result = randint(1, 10)
        elif dice == "d100":
            result = randint(1, 100)
        return result
    
    def setStatsByCategory(self, results):
        # Set dice results to stats depending on category
        # TO DO
        
        # STR
        #    Adds damage
        #    More weight carry / lift
        #    Affects Size
        #    Counts for Ki Pool / Ki ACT
        
        # AGI
        #    More Flee
        #    More Movement speed
        #    More Turn
        #    Actions x Turn
        #    Counts for Ki Pool / Ki ACT
        
        # DEX
        #    More Attack skill
        #    More Parry skill
        #    More Turn
        #    Actions x Turn
        #    Counts for Ki Pool / Ki ACT
        
        # CON
        #    More HP
        #    More Fatigue
        #    More Regen 
        #    Affects Size
        #    RF, RV, RE
        #    Counts for Ki Pool / Ki ACT
        
        # PERCEPTION
        #    Affects Perception
        #    
        
        # INT
        #    Magic Levels
        #    Magic spell capability
        
        # POW
        #    Zeon Pool
        #    Magic ACT
        #    Innate Magic
        #    RM
        #    Counts for Ki Pool / Ki ACT
        
        # WILL
        #    Willpower Consumtions (CVs)
        #    Psyquic Potential
        #    RP
        #    Counts for Ki Pool / Ki ACT     
        
        # Worst [0] to Best [7]
        if self.category == categoryType.WARRIOR: #1
            self.strenght = results[4]
            self.dexterity = results[7]
            self.agility = results[5]
            self.constitution = results[6]
            self.intelligence = results[0]
            self.power = results[3]
            self.willpower = results[2]
            self.perception = results[1]
        elif self.category == categoryType.ACROBAT: #2
            self.strenght = results[5]
            self.dexterity = results[4]
            self.agility = results[7]
            self.constitution = results[6]
            self.intelligence = results[2]
            self.power = results[3]
            self.willpower = results[1]
            self.perception = results[0]
        elif self.category == categoryType.PALADIN: #3
            self.strenght = results[4]
            self.dexterity = results[7]
            self.agility = results[0]
            self.constitution = results[6]
            self.intelligence = results[1]
            self.power = results[3]
            self.willpower = results[5]
            self.perception = results[2]
        elif self.category == categoryType.DARK_PALADIN: #4
            self.strenght = results[4]
            self.dexterity = results[7]
            self.agility = results[0]
            self.constitution = results[6]
            self.intelligence = results[1]
            self.power = results[3]
            self.willpower = results[5]
            self.perception = results[2]
        elif self.category == categoryType.WEAPON_MASTER: #5
            self.strenght = results[5]
            self.dexterity = results[6]
            self.agility = results[4]
            self.constitution = results[7]
            self.intelligence = results[1]
            self.power = results[3]
            self.willpower = results[2]
            self.perception = results[0]
        elif self.category == categoryType.TECHNICIAN: #6
            self.strenght = results[6]
            self.dexterity = results[7]
            self.agility = results[4]
            self.constitution = results[3]
            self.intelligence = results[1]
            self.power = results[5]
            self.willpower = results[2]
            self.perception = results[0]
        elif self.category == categoryType.TAO: #7
            self.strenght = results[7]
            self.dexterity = results[6]
            self.agility = results[5]
            self.constitution = results[4]
            self.intelligence = results[1]
            self.power = results[3]
            self.willpower = results[2]
            self.perception = results[0]
        elif self.category == categoryType.EXPLORER: #8
            self.strenght = results[2]
            self.dexterity = results[7]
            self.agility = results[6]
            self.constitution = results[3]
            self.intelligence = results[5]
            self.power = results[1]
            self.willpower = results[0]
            self.perception = results[4]
        elif self.category == categoryType.SHADOW: #9
            self.strenght = results[5]
            self.dexterity = results[7]
            self.agility = results[6]
            self.constitution = results[3]
            self.intelligence = results[0]
            self.power = results[4]
            self.willpower = results[1]
            self.perception = results[2]
        elif self.category == categoryType.THIEF: #10
            self.strenght = results[1]
            self.dexterity = results[6]
            self.agility = results[7]
            self.constitution = results[0]
            self.intelligence = results[4]
            self.power = results[3]
            self.willpower = results[2]
            self.perception = results[5]
        elif self.category == categoryType.ASSASSIN: #11
            self.strenght = results[6]
            self.dexterity = results[7]
            self.agility = results[1]
            self.constitution = results[4]
            self.intelligence = results[2]
            self.power = results[3]
            self.willpower = results[0]
            self.perception = results[5]
        elif self.category == categoryType.SORCERER: #12
            self.strenght = results[0]
            self.dexterity = results[5]
            self.agility = results[1]
            self.constitution = results[2]
            self.intelligence = results[7]
            self.power = results[6]
            self.willpower = results[4]
            self.perception = results[3]
        elif self.category == categoryType.WARLOCK: #13
            self.strenght = results[4]
            self.dexterity = results[7]
            self.agility = results[0]
            self.constitution = results[2]
            self.intelligence = results[6]
            self.power = results[5]
            self.willpower = results[3]
            self.perception = results[1] 
        elif self.category == categoryType.ILLUSIONIST: #14
            self.strenght = results[0]
            self.dexterity = results[6]
            self.agility = results[1]
            self.constitution = results[2]
            self.intelligence = results[7]
            self.power = results[5]
            self.willpower = results[3]
            self.perception = results[4]
        elif self.category == categoryType.PSY_MAGE: #15
            self.strenght = results[0]
            self.dexterity = results[4]
            self.agility = results[1]
            self.constitution = results[3]
            self.intelligence = results[7]
            self.power = results[5]
            self.willpower = results[6]
            self.perception = results[2]
        elif self.category == categoryType.SUMMONER: #16
            self.strenght = results[0]
            self.dexterity = results[4]
            self.agility = results[2]
            self.constitution = results[3]
            self.intelligence = results[6]
            self.power = results[5]
            self.willpower = results[7]
            self.perception = results[1]
        elif self.category == categoryType.WARRIOR_SUMMONER: #17
            self.strenght = results[4]
            self.dexterity = results[6]
            self.agility = results[0]
            self.constitution = results[5]
            self.intelligence = results[1]
            self.power = results[3]
            self.willpower = results[7]
            self.perception = results[2]
        elif self.category == categoryType.MENTALIST: #18
            self.strenght = results[1]
            self.dexterity = results[6]
            self.agility = results[2]
            self.constitution = results[4]
            self.intelligence = results[5]
            self.power = results[0]
            self.willpower = results[7]
            self.perception = results[3]
        elif self.category == categoryType.WARRIOR_MENTALIST: #19
            self.strenght = results[5]
            self.dexterity = results[6]
            self.agility = results[3]
            self.constitution = results[4]
            self.intelligence = results[1]
            self.power = results[0]
            self.willpower = results[7]
            self.perception = results[2]
        elif self.category == categoryType.NOVICE: #20
            shuffle(results)
            self.strenght = results[0]
            self.dexterity = results[1]
            self.agility = results[2]
            self.constitution = results[3]
            self.intelligence = results[4]
            self.power = results[5]
            self.willpower = results[6]
            self.perception = results[7]
        elif self.category == categoryType.GOTHIC_LOLITA:
            self.strenght = results[3]
            self.dexterity = results[5]
            self.agility = results[0]
            self.constitution = results[4]
            self.intelligence = results[2]
            self.power = results[7]
            self.willpower = results[6]
            self.perception = results[1]
        elif self.category == categoryType.MAGIC_TSUNDERE:
            self.strenght = results[4]
            self.dexterity = results[5]
            self.agility = results[0]
            self.constitution = results[2]
            self.intelligence = results[6]
            self.power = results[7]
            self.willpower = results[3]
            self.perception = results[1]
        elif self.category == categoryType.MOE:
            self.strenght = results[0]
            self.dexterity = results[4]
            self.agility = results[1]
            self.constitution = results[5]
            self.intelligence = results[6]
            self.power = results[2]
            self.willpower = results[3]
            self.perception = results[7]
        elif self.category == categoryType.NEKOMIMI:
            self.strenght = results[0]
            self.dexterity = results[5]
            self.agility = results[1]
            self.constitution = results[2]
            self.intelligence = results[7]
            self.power = results[4]
            self.willpower = results[3]
            self.perception = results[6]
        elif self.category == categoryType.YANDERE:
            self.strenght = results[1]
            self.dexterity = results[6]
            self.agility = results[5]
            self.constitution = results[2]
            self.intelligence = results[3]
            self.power = results[0]
            self.willpower = results[7]
            self.perception = results[4]
        elif self.category == categoryType.YANGIRE:
            self.strenght = results[0]
            self.dexterity = results[5]
            self.agility = results[1]
            self.constitution = results[3]
            self.intelligence = results[2]
            self.power = results[4]
            self.willpower = results[7]
            self.perception = results[6]
        elif self.category == categoryType.MAGICAL_GIRL:
            self.strenght = results[2]
            self.dexterity = results[5]
            self.agility = results[1]
            self.constitution = results[0]
            self.intelligence = results[6]
            self.power = results[7]
            self.willpower = results[4]
            self.perception = results[3]
        elif self.category == categoryType.HEX_WITCH:
            self.strenght = results[1]
            self.dexterity = results[5]
            self.agility = results[2]
            self.constitution = results[4]
            self.intelligence = results[6]
            self.power = results[3]
            self.willpower = results[0]
            self.perception = results[7]
        else:
            print("ERROR- Category is invalid: ", self.category)
            
    
    def generateRandomStats(self, throw_kind):
        # Generate a random dice roll for the stats
        # throw_kind use the manual different ways to calculate stats
        if throw_kind == 1:
            results = []
            for i in range(8):
                result = 0
                while (result < 4):
                    result = self.diceRoll("d10")
                results.append(result)
            results.sort()
            results[0] = 9
            results.sort()
            #shuffle(results)
            print("Dice rolls:", results)
            self.setStatsByCategory(results)
        elif throw_kind == 2:
            results = []
            for i in range(8):
                dice1 = self.diceRoll("d10")
                dice2 = self.diceRoll("d10")
                if dice1 > dice2:
                    results.append(dice1)
                else:
                    results.append(dice2)
            shuffle(results)
            print("Dice rolls:", results)
        elif throw_kind == 3:
            self.strenght = self.diceRoll("d10")
            self.dexterity = self.diceRoll("d10")
            self.agility = self.diceRoll("d10")
            self.constitution = self.diceRoll("d10")
            self.intelligence = self.diceRoll("d10")
            self.power = self.diceRoll("d10")
            self.willpower = self.diceRoll("d10")
            self.perception = self.diceRoll("d10")
        else:
            self.strenght = self.diceRoll("d10")
            self.dexterity = self.diceRoll("d10")
            self.agility = self.diceRoll("d10")
            self.constitution = self.diceRoll("d10")
            self.intelligence = self.diceRoll("d10")
            self.power = self.diceRoll("d10")
            self.willpower = self.diceRoll("d10")
            self.perception = self.diceRoll("d10")
            return 
        self.setStatsByCategory(results)
        
        
    def setStat(self, stat, value):
        name = stat.lower()
        if value > 0 and value < 21:    
            if name == "strenght" or name == "str" or name == "fue" or name == "fuerza":
                self.strenght = value
            elif name == "agility" or name == "agi" or name == "agilidad":
                self.agility = value
            elif name == "dexterity" or name == "dex" or name == "des" or name == "destreza":
                self.dexterity = value
            elif name == "constitution" or name == "con" or name == "constitution":
                self.constitution = value
            elif name == "perception" or name == "per" or name == "percepcion":
                self.perception = value
            elif name == "intelligence" or name == "int" or name == "inteligencia":
                self.intelligence = value
            elif name == "willpower" or name == "will" or name == "vol" or name == "voluntad":
                self.willpower = value
            elif name == "power" or name == "pow" or name == "pod" or name == "poder":
                self.power = value
            else:
                print("Invalid stat:", stat, ". Use str, agi, dex, con, per, int, will or pow.")
                return
        else:
            print("Invalid value:", value, ". Please use 1-20")
            return
        #self.recalculateAll()#??
        print("Set value for", name, " to", value)
            
    def generateCharacterAppearance(self):
        # Appearance
        self.appearance = self.diceRoll("d10")
        print("Appearance: ", self.appearance)
        
        # Gender
        result = self.diceRoll("d100")
        if (result < 10):
            self.sex = "Other"
        if (result >= 10 and result < 55):
            self.sex = "Male"
        else:
            self.sex = "Female"
        print("Gender: ", self.sex)
        
        # HairStyle
        hair = -1
        if self.sex == "Male":
            hair = randint(0,24)
        else:
            hair = randint(3,32)
        self.hair_style = hairStyle(hair)
        print("Hair Style:", self.hair_style)
        
        # Hair Color (20)
        self.hair_color = hairEyeColor(randint(0,20))
        print("Hair Color:", self.hair_color)
        
        # Eye Color
        self.eye_color = hairEyeColor(randint(0,20))
        print("Eye Color:", self.eye_color)
        
    
    def generateOrigins(self):
        # Country
        if self.allowInterregns:    
            self.country = countries(randint(0, 46))
        elif self.allowEurakia:
            self.country = countries(randint(0, 43))
        else:
            self.country = countries(randint(0, 38))
        print("Country:", self.country)
        
        # Etnicity
        if self.allowEurakia:
            self.etnicity = etnicities(randint(0, 15))
        else:
            self.etnicity = etnicities(randint(0, 9))
        print("Etnicity:", self.etnicity)
        
            
    def showCategory(self):
        print(self.category)
    
    def pickRandomCategory(self):
        pick = 0
        if (self.allowNonCanonCategories):
            pick = randint(1,28)
        else:
            pick = randint(1,20)
        self.category1 = categoryType(pick)
        self.category = self.category1
        self.showCategory()
           
    def checkStats(self):
        # TO DO: Check limits (Primary limit, difference between attack and defense, skill bonus max, invested PD and others)
        print("check values")
    
    def pickRandomName(self):
        # Pick random name
        try:
            if self.sex == "Male":    
                with open('MaleNamesDB.txt') as openfileobject:
                    for line in openfileobject:
                        self.male_names.append(line)
                    openfileobject.close()
                size = len(self.male_names)
                self.name = self.male_names[randint(0,size-1)]
            elif self.sex == "Female":
                with open('FemaleNamesDB.txt') as openfileobject:
                    for line in openfileobject:
                        self.female_names.append(line)
                    openfileobject.close()
                size = len(self.female_names)
                self.name = self.female_names[randint(0,size-1)]
            else:
                with open('NeutralNamesDB.txt') as openfileobject:
                    for line in openfileobject:
                        self.neutral_names.append(line)
                    openfileobject.close()
                size = len(self.male_names)
                self.name = self.male_names[randint(0,size-1)]
        except:
            print("ERROR - Something went wrong.")
        
        self.name = self.name.rstrip()
        print("Name:", self.name)
    
    def saveTextSheet(self):
        #character_name = input("¿Character name?")
        #file_name = character_name + ".txt"
        save_dir = ".\\GeneratedSheets\\"
        file_name = save_dir + self.name + ".txt"
        exists = True
        i = 1

        # Find valid name
        while exists:
            exists = os.path.exists(file_name)
            if (exists):
                file_name = self.name + "_" + str(i) + ".txt"
                i = i +1
        # Open file
        try:
            file_object = open(file_name, "w+")
        except IOError:
            print("File not accessible")
        
        # Write data (%s string, %d int)
        try:
            file_object.write("Name: %s\n" % self.name)
            file_object.write("Level: %d\n" % self.level)
            file_object.write("Appearance: %d\n" % self.appearance)
            file_object.write("Gender: %s\n" % self.sex)
            file_object.write("Hair style: %s\n" % self.hair_style.name)
            file_object.write("Hair color: %s\n" % self.hair_color.name)
            file_object.write("Eye color: %s\n" % self.eye_color.name)
            file_object.write("Country: %s\n" % self.country.name)
            file_object.write("Etnicity: %s\n" % self.etnicity.name)
            file_object.write("Category: %s\n" % self.category.name)
            file_object.write("%d (%d) Strenght\n" % (self.strenght, self.str_bonus))
            file_object.write("%d (%d) Agility\n" % (self.agility, self.agi_bonus))
            file_object.write("%d (%d) Dexterity\n" % (self.dexterity, self.dex_bonus))
            file_object.write("%d (%d) Constitution\n" % (self.constitution, self.con_bonus))
            file_object.write("%d (%d) Perception\n" % (self.perception, self.per_bonus))
            file_object.write("%d (%d) Intelligence\n" % (self.intelligence, self.int_bonus))
            file_object.write("%d (%d) Willpower\n" % (self.willpower, self.will_bonus))
            file_object.write("%d (%d) Power\n" % (self.power, self.pow_bonus))
            file_object.write("Presence: %s\n" % self.presence)
            file_object.write("HP Base: %d\n" % self.hp_base)
            file_object.write("Physical Resistance: %d\n" % self.RF)
            file_object.write("Poison Resistance: %d\n" % self.RV)
            file_object.write("Magic Resistance: %d\n" % self.RM)
            file_object.write("Sickness Resistance: %d\n" % self.RE)
            file_object.write("Psy Resistance: %d\n" % self.RP)
            file_object.write("HP Base: %d\n" % self.hp_base)
            file_object.write("Size: %d\n" % self.size)
            file_object.write("Weight: %d kg\n" % self.weight)
            file_object.write("Height: %d cm\n" % self.height)
            file_object.write("Fatigue: %d\n" % self.fatigue_base)
            file_object.write("Carry Weight: %d\n" % self.carry_weight)
            file_object.write("Lift Weight: %d\n" % self.lift_weight)
            file_object.write("Movement: %d\n" % self.movement_stat_base)
            file_object.write("Regeneration: %d\n" % self.regen_base)
            file_object.write("Daily HP regen resting: %d\n" % self.regen_hp_resting)
            file_object.write("Daily HP regen without rest: %d\n" % self.regen_hp_unrest)
            file_object.write("Daily negative reduction: %d\n" % self.negative_reduction)
            file_object.write("Regen special effect: %s\n" % self.regen_effect)
            file_object.write("Actions per turn: %d\n" % self.actions_x_turn_base)
            file_object.write("Ki pool: %d\n" % self.ki_pool_base)
            file_object.write("Ki ACT: %d\n" % self.ki_act_base)
            file_object.write("Zeon pool: %d\n" % self.zeon_pool_base)
            file_object.write("Magic ACT: %d\n" % self.magic_act_base)
            file_object.write("Magic Levels: %d\n" % self.magic_levels_base)
            file_object.write("Psychic Potential: %d\n" % self.psychic_potential_base)
        except IOError:
            print("Problem writing data")
        finally:
            file_object.close()
        
    def generateRandomCharacter(self):
        #Give stats to character
        print("ANIMA CHARACTER GENERATOR")
        self.level = 1
        print("Level:", self.level)
        self.generateCharacterAppearance()
        self.pickRandomName()
        self.generateOrigins()
        self.pickRandomCategory()
        self.generateRandomStats(1)
        self.recalculateALL()
        self.saveTextSheet()
        
    def checkMenuSelection(self, selection):
        if selection == "1" or selection == "2" or selection == "3" or selection == "4" or selection == "5":
            return True
        else:
            print("selection:", selection, "is invalid")
            return False
    
    def getInput(self, message):
        validation = False
        while not validation:
            var = input(message)
            valid = input("Input: ", var, ". Are you sure? (y/n)")
            if (valid == "y" or valid == "Y"):
                validation = True
        return var
    
    def categoriaDesdeTexto(self):
        print("Categoria desde seleccion de texto")
    
    def generateNewCharacter(self):
        print("GenerateNewChara")
        self.name = self.getInput("¿Nombre del personaje?")
    
    def mainProgram(self):
        menuState = "0" # EntryPoint
        playStatus = True
        print("Entered Main Program")
        while playStatus:
            if menuState == "0":
                # ENTRYPOINT MENU
                print("HELLO TO ANIMA PYTHON CHARACTER SHEET!")
                print("--------------------------------------")
                print("Choose what you want to do:")
                print("1.- Start a new character sheet")
                print("2.- Generate a random character sheet")
                print("3.- Load a character sheet")
                print("4.- Save actual sheet")
                print("5.- Edit character sheet")
                menuChoice = "-1"
                menuChoice = input("Select one option: ")
                isValidChoice = self.checkMenuSelection(menuChoice)
                if isValidChoice:
                    menuState = menuChoice
                else:
                    print("Invalid choice, please select one number.")
                    print("")
            elif menuState == "1":
                print("Generation of new character")
                # 
            elif menuState == "2":
                # Generate random character sheet
                print("Menu state 2")
                self.generateRandomCharacter()
            elif menuState == "3":
                # 
                print("Menu state 3")
            else:
                print("Invalid menu state, returning to main menu")
                menuState = 0
    
if __name__ == "__main__":
    charaSheet = AnimaCharacter()
    charaSheet.generateRandomCharacter()
    #charaSheet.mainProgram()