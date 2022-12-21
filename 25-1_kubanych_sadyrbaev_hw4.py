from random import randint, choice
from enum import Enum


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    BOOST = 2
    HEAL = 3
    SAVE_DAMAGE_AND_REVERT = 4
    STUN = 5
    GUARD_FOR_ALL = 6
    REVIVE = 7
    INVISIBILITY = 8
    LUCK = 9
    POISON_HEAL_SHURIKENS = 10
    SELF_DESTRUCTION = 11
    ONE_FOR_ALL = 12
    SIZE_INCREASE_AND_REDUCTION = 13
    OPOSSUM = 14
    VAMPIRISM = 15
    ANGEL_CROW = 16



class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        hero = choice(heroes)
        if hero.health <= 0:
            self.choose_defence(heroes)
        else:
            self.__defence = hero.super_ability

    def hit(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health = hero.health - self.damage

    def __str__(self):
        return f'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super().__init__(name, health, damage)
        if not isinstance(super_ability, SuperAbility):
            raise ValueError("Ability must be of type SuperAbility")
        else:
            self.__super_ability = super_ability

    def hit(self, boss):
        boss.health = boss.health - self.damage

    @property
    def super_ability(self):
        return self.__super_ability

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coeffient = randint(2, 5)
        boss.health = boss.health - self.damage * coeffient
        print(f'Warrior hits critically: {self.damage * coeffient}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            hero.damage += int(hero.damage * 0.25)
        print('Power of each heroes was increased!')

class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__saved_damaged = 0

    def apply_super_power(self, boss, heroes):
        self.health = self.health - int(boss.damage * 0.95)
        self.__saved_damaged = int(boss.damage * 0.05)
        self.damage = self.damage + self.__saved_damaged
        print("Berserk's power was increased")

class Thor(Hero):
    def __init__(self, name, health, damage):
        super(Thor, self).__init__(name, health, damage, SuperAbility.STUN)

    def apply_super_power(self, boss, heroes):
        stun_chance = randint(1, 11)
        if stun_chance == 3:
            print('Boss has been stunned')
            for hero in heroes:
                hero.health = hero.health + boss.damage

class Golem(Hero):
    def __init__(self, name, health, damage):
        super(Golem, self).__init__(name, health, damage, SuperAbility.GUARD_FOR_ALL)

    def apply_super_power(self, boss, heroes):
        self.health = self.health - (boss.damage + int(boss.damage * 0.8))
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.health = hero.health + int(boss.damage * 0.2)
        print('GUARDED!')

class Withcer(Hero):
    def __init__(self, name, health, damage=0):
        super(Withcer, self).__init__(name, health, damage, SuperAbility.REVIVE)
        if damage > 0:
            raise ValueError('Damage must be 0 for this hero!')

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health == 0 and hero != self and self.health > 0:
                hero.health = self.health
                self.health = 0
                print('Hero was revived')

class Lucky(Hero):
    def __init__(self, name, health, damage):
        super(Lucky, self).__init__(name, health, damage, SuperAbility.LUCK)

    def apply_super_power(self, boss, heroes):
        luck_chance = randint(1, 31) #шанс очень маленький, но он есть
        if luck_chance == 7 and self.health > 0:
            self.health = self.health + boss.damage
            print('Luck! Luck! Luck!')

class Samurai(Hero):
    def __init__(self, name, health, damage, damage_points):
        super(Samurai, self).__init__(name, health, damage, SuperAbility.POISON_HEAL_SHURIKENS)
        self.__damage_points = damage_points
    def apply_super_power(self, boss, heroes):
        dropout_chance = randint(1, 101)
        if dropout_chance % 2 == 0:
            boss.health = boss.health - self.__damage_points
            print('Boss was poisoned!')
        elif dropout_chance % 2 == 1:
            boss.health = boss.health + self.__damage_points
            print("Boss was cured!")

class Kamikadze(Hero):
    def __init__(self, name, health, damage=0):
        super(Kamikadze, self).__init__(name, health, damage, SuperAbility.SELF_DESTRUCTION)
        if damage > 0:
            raise ValueError('Damage must be 0 for this hero!')

    def apply_super_power(self, boss, heroes):
        if self.health <= boss.damage * 4: #чтоб он после первого раунда не умирал
            accuracy = randint(1, 21)
            if accuracy == 10:
                self.health = 0
                boss.health = boss.health - self.health
                print('EXACTLY ON TARGET! Astalavista Baby!')
            else:
                self.health = 0
                boss.health = boss.health - int(self.health * 0.5)
                print("MISSED! I've done everything I can.")

class Deku(Hero):
    def __init__(self, name, health, damage):
        super(Deku, self).__init__(name, health, damage, SuperAbility.ONE_FOR_ALL)

    def apply_super_power(self, boss, heroes):
        damage_chance = randint(1, 3)
        if damage_chance == 2:
            ability_chance = randint(5, 8)
            if ability_chance % 4 == 1: #20%
                boss.health = boss.health - int(self.damage * 1.2)
                boss.health = boss.health + self.damage
                self.health = int(self.health * 0.8)
                print('ONE FOR ALL 20%!')

            elif ability_chance % 4 == 2: #50%
                boss.health = boss.health - int(self.damage * 1.5)
                boss.health = boss.health + self.damage
                self.health = int(self.health * 0.5)
                print('ONE FOR ALL 50%!')

            else: #100%
                boss.health = boss.health - self.damage * 2
                boss.health = boss.health + self.damage
                self.health = 0
                print('ONE FOR ALL 100%!!!!')
        else:
            print('ONE FOR ALL not used!')

class AntMan(Hero):
    def __init__(self, name, health, damage):
        super(AntMan, self).__init__(name, health, damage, SuperAbility.SIZE_INCREASE_AND_REDUCTION)

    def apply_super_power(self, boss, heroes):
        size_chance = randint(1, 3)
        if size_chance == 1: #up
            boss.health = boss.health - int(self.damage*0.5)
            self.health = self.health - int(boss.damage * 0.5)
            print('Towards the SUN!')
        else: #down
            boss.health = boss.health - self.damage//2
            boss.health = boss.health + self.damage
            self.health = self.health + int(boss.damage*0.5)
            print('Quantumania!')

class Tricky(Hero):
    def __init__(self, name, health, damage):
        super(Tricky, self).__init__(name, health, damage, SuperAbility.OPOSSUM)

    def apply_super_power(self, boss, heroes):
        death_chance = randint(1, 5)
        if death_chance == 2:
            self.health = self.health + boss.damage
            boss.health = boss.health + self.damage
            print('IM DEAD!(not)')

class Hacker(Hero):
    def __init__(self, name, health, damage, vampire_damage):
        super().__init__(name, health, damage, SuperAbility.VAMPIRISM)
        self.__vampire_damage = vampire_damage

    def apply_super_power(self, boss, heroes):
        boss.health = boss.health - self.__vampire_damage
        hero = choice(heroes)
        if hero.health > 0 and hero != self:
            hero.health = hero.health + self.__vampire_damage
            print('BLOOD MOON ROSE!!!!!!!')
        else:
            self.health = self.health + self.__vampire_damage
            print('FIRST BLOOD!')

class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points
    @property
    def heal_points(self):
        return self.__heal_points

    @heal_points.setter
    def heal_points(self, value):
        self.__heal_points = value

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health = hero.health + self.__heal_points

class Druid(Hero):
    def __init__(self, name, health, damage, heal_points=0):
        super().__init__(name, health, damage, SuperAbility.ANGEL_CROW)
        self.__heal_points = heal_points
        if heal_points > 0:
            raise ValueError('Heal points must be 0 for this hero!')
    def apply_super_power(self, boss, heroes):
        summon_counter = 1
        while summon_counter > 0:
            summon_counter -= 1
            for hero in heroes:
                if hero.super_ability == SuperAbility.HEAL and hero != self:
                    hero.heal_points = int(hero.heal_points*1.2)
                    print('Doctors skills were increased!')
            if boss.health >=
            # else:
        #     print('VORON')



round_counter = 0


def print_statistics(boss, heroes):
    print('ROUND ' + str(round_counter) + ' -------------')
    print(boss)
    for hero in heroes:
        print(hero)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print("Boss won!!!")
    return all_heroes_dead


def play_round(boss, heroes):
    global round_counter
    round_counter += 1
    boss.choose_defence(heroes)
    boss.hit(heroes)
    for hero in heroes:
        if boss.defence != hero.super_ability and hero.health > 0 and boss.health > 0:
            hero.hit(boss)
            hero.apply_super_power(boss, heroes)
    print_statistics(boss, heroes)


def start_game():
    boss = Boss('Rashan', 1000, 50)
    warrior = Warrior('Conan', 250, 0)
    mage = Druid('Merlin', 280, 10)
    berserk = Berserk('Hiccup', 260, 0)
    kamikadze = Kamikadze('Rob', 300)
    deku = Deku('Midoria', 250, 20)
    hacker = Hacker('Kuba', 270, 5, 20)
    thor = Thor('Thor', 290, 17)
    tricky = Tricky('Jack', 300, 10)
    antman = AntMan('Scott', 250, 15)
    samurai = Medic('Raizo', 270, 20, 12)
    lucky = Lucky('Lucky', 260, 13)
    golem = Golem('Grut', 500, 5)
    witcher = Withcer('Geralt', 250)
    heroes = [warrior, mage, berserk, samurai, deku]

    print_statistics(boss, heroes)

    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)


start_game()
