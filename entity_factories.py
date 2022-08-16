from components.ai import HostileEnemy
from components import consumables, equippable
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item

player = Actor(
    char="@",
    colour=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=50, base_defense=1, base_power=2),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),
)

orc = Actor(
    char="h",
    colour=(63, 127, 63),
    name="Hood",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, base_defense=0, base_power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)
troll = Actor(
    char="T",
    colour=(0, 127, 0),
    name="Thug",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=15, base_defense=1, base_power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),
)
confusion_scroll = Item(
    char="~",
    colour=(207, 63, 255),
    name="Confusion Scroll",
    consumable=consumables.ConfusionConsumable(number_of_turns=10),
)
fireball_scroll = Item(
    char="~",
    colour=(255, 0, 0),
    name="Fire 100% Scroll",
    consumable=consumables.FireballDamageConsumable(damage=12, radius=3),
)
health_potion = Item(
    char="!",
    colour=(127, 0, 255),
    name="Drip Juice",
    consumable=consumables.HealingConsumable(amount=4),
)
lightning_scroll = Item(
    char="~",
    colour=(255, 255, 0),
    name="Lightning Scroll",
    consumable=consumables.LightningDamageConsumable(damage=20, maximum_range=5),
)

dagger = Item(
    char=",", colour=(0, 191, 255), name="Shank", equippable=equippable.Dagger()
)

sword = Item(char="/", colour=(0, 191, 255), name="Baseball Bat", equippable=equippable.Sword())

leather_armour = Item(
    char="[",
    colour=(139, 69, 19),
    name="Air Jordan",
    equippable=equippable.LeatherArmour(),
)

chain_mail = Item(
    char="[",
    colour=(139, 69, 19),
    name="Supreme Air Force",
    equippable=equippable.ChainMail(),
)
