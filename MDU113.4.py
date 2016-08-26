import time
import random

classs = str("null");
level = 0;
choice = 0;
quality = str("Common");
qualitychoice = 0;
armour = str("Head");
armourchoice = 0;
material = str("Dirt");
itembudget = 0;

# Getting the level and class from the player
print ("What level are you from 1-30");
while True:
    try:
        level = int(input());
    except ValueError:
        print("Please enter a number between 1-30");
        continue
    else:
        break

while level > 30 or level < 1:
    print ("Please enter a number between 1-30");
    level = int(input());
print ("Are you 1. A Wookie 2. A Droid or 3. A Stormtrooper");
while True:
    try:
        choice = int(input());
    except ValueError:
        print("Please enter a number between 1-3");
        continue
    else:
        break

itembudget = level * 100

while choice > 3 or choice < 1:
    print("Please choose 1, 2 or 3");
    choice = int(input());
if choice == 1:
    classs = str(("Wookie"));
if choice == 2:
    classs = str(("Droid"));
if choice == 3:
    classs = str(("StormTrooper"));

# Choosing quality
print("What quality is the item?");
print("1. Common, 2. Uncommon, 3. Rare, 4. Epic, 5. Legendary, 6. Artifact");
while True:
    try:
        qualitychoice = int(input());
    except ValueError:
        print("Please enter a number between 1-6")
        continue
    else:
        break

while qualitychoice > 6 or qualitychoice < 1:
    print("Please choose a quality between 1-6");
    print("1. Common, 2. Uncommon, 3. Rare, 4. Epic, 5. Legendary, 6. Artifact");
    qualitychoice = int(input());
if qualitychoice == 1:
    quality = str("Common");
    itembudget += 100;
if qualitychoice == 2:
    quality = str("Uncommon");
    itembudget += 250;
if qualitychoice == 3:
    quality = str("Rare");
    itembudget += 500;
if qualitychoice == 4:
    quality = str("Epic");
    itembudget += 1000;
if qualitychoice == 5:
    quality = str("Legendary");
    itembudget += 2000;
if qualitychoice == 6:
    quality = str("Artifact");
    itembudget += 3000;

# Choosing the slot for the armour
print("What slot is the armour for?");
print("1. Head, 2. Chest, 3. Arms, 4. Legs");
while True:
    try:
        armourchoice = int(input());
    except ValueError:
        print("Please enter a number between 1-4")
        continue
    else:
        break

while armourchoice > 4 or armourchoice < 1:
    print("Please choose a number between 1-4");
    print("1. Head, 2. Chest, 3. Arms, 4. Legs");
    armourchoice = int(input());
if armourchoice == 1:
    armour = str("Helmet");
    itembudget += 500;
if armourchoice == 2:
    armour = str("Breastplate");
    itembudget += 3000;
if armourchoice == 3:
    armour = str("Armguard");
    itembudget += 1000;
if armourchoice == 4:
    armour = str("Leggings");
    itembudget += 2000;


print("Generating an " + str(quality) + " " + str(armour) + " for a level " + str(level) + " " + str(classs));
time.sleep(1);
print("...");
time.sleep(1);
print("...");
time.sleep(1);
print("...");

# Generating random armour materials
materialpercent = float(random.random());
armourbuff = 0;
if materialpercent > 0 and materialpercent < 0.5625:
    material = str("Recycled cloth");
    armourbuff = 1;
if materialpercent > 0.5625 and materialpercent < 0.8125:
    material = str("Discount rusted plate");
    armourbuff = 2;
if materialpercent > 0.8125 and materialpercent < 0.9375:
    material = str("Slightly rusted plate");
    armourbuff = 3;
if materialpercent > 0.9375 and materialpercent < 1:
    material = str("Pristine plate");
    armourbuff = 4;

# Generating random armour attributes depending on class
droidatt = ["Combat Mastery", "Acuity", "Strength", "Multistrike"];
wookieatt = ["Damage Mitigation", "Stamina", "Combat Mastery", "Strength", "Alertness", "Multistrike"];
stormatt = ["Combat Mastery", "Acuity", "Strength", "Alertness", "Damage Mitigation", "Multistrike"];
attribute = str("Null");
if classs == str("Droid"):
    attribute = str(random.choice(droidatt));
if classs == str("Wookie"):
    attribute = str(random.choice(wookieatt));
if classs == str("StormTrooper"):
    attribute = str(random.choice(stormatt));

# Generate random status effects depending on rarity and class
droideffect = ["XP bonus", "Cyborg Mastery Bonus", "Multistrike", "Life Leech Aura"];
wookieeffect = ["XP bonus", "Life Leech Aura", "Regeneration Aura", "Damage Mitigation Bonus"];
stormeffect = ["XP bonus", "Cyborg Mastery Bonus", "Multistrike", "Damage Mitigation Bonus"];
status = []
if classs == str("Droid"):
    if quality == str("Common"):
        status.append("no status effect");
    if quality == str("Uncommon"):
        uncommon1 = float(random.random());
        if uncommon1 > 0 and uncommon1 < 0.1:
            uncommonstatus = str(random.choice(droideffect));
            droideffect.remove(str(uncommonstatus));
            status.append(str(uncommonstatus));
        else:
            status.append("no status effect");
    if quality == str("Rare"):
        rare1 = float(random.random());
        if rare1 > 0 and rare1 < 0.5:
            rarestatus = str(random.choice(droideffect));
            droideffect.remove(str(rarestatus));
            status.append(str(rarestatus));
        else:
            status.append("no status effect");
    if quality == str("Epic"):
        epic1 = float(random.random());
        if epic1 > 0 and epic1 < 0.75:
            epicstatus = str(random.choice(droideffect));
            droideffect.remove(str(epicstatus));
            status.append(str(epicstatus));
        if epic1 > 0 and epic1 < 0.25:
            epicstatus = str(random.choice(droideffect));
            droideffect.remove(str(epicstatus));
            status.append(str(epicstatus));
        else:
            status.append("no status effect");
    if quality == str("Legendary"):
        legendary1 = float(random.random());
        legendarystatus = str(random.choice(droideffect));
        droideffect.remove(str(legendarystatus));
        status.append(str(legendarystatus));
        if legendary1 > 0 and legendary1 < 0.50:
            legendarystatus = str(random.choice(droideffect));
            droideffect.remove(str(legendarystatus));
            status.append(str(legendarystatus));
            legendarystatus = str(random.choice(droideffect));
            droideffect.remove(str(legendarystatus));
            status.append(str(legendarystatus));
        if legendary1 > 0 and legendary1 < 0.25:
            legendarystatus = str(random.choice(droideffect));
            droideffect.remove(str(legendarystatus));
            status.append(str(legendarystatus));
    if quality == str("Artifact"):
        artifact1 = float(random.random());
        artifactstatus = str(random.choice(droideffect));
        droideffect.remove(str(artifactstatus));
        status.append(str(artifactstatus));
        artifactstatus = str(random.choice(droideffect));
        droideffect.remove(str(artifactstatus));
        status.append(str(artifactstatus));
        if artifact1 > 0 and artifact1 < 0.5:
            artifactstatus = str(random.choice(droideffect));
            droideffect.remove(str(artifactstatus));
            status.append(str(artifactstatus));
        if artifact1 > 0 and artifact1 < 0.25:
            artifactstatus = str(random.choice(droideffect));
            droideffect.remove(str(artifactstatus));
            status.append(str(artifactstatus));

if classs == str("Wookie"):
    if quality == str("Common"):
        status.append("no status effect");
    if quality == str("Uncommon"):
        uncommon1 = float(random.random());
        if uncommon1 > 0 and uncommon1 < 0.1:
            uncommonstatus = str(random.choice(wookieeffect));
            wookieeffect.remove(str(uncommonstatus));
            status.append(str(uncommonstatus));
        else:
            status.append("no status effect");
    if quality == str("Rare"):
        rare1 = float(random.random());
        if rare1 > 0 and rare1 < 0.5:
            rarestatus = str(random.choice(wookieeffect));
            wookieeffect.remove(str(rarestatus));
            status.append(str(rarestatus));
        else:
            status.append("no status effect");
    if quality == str("Epic"):
        epic1 = float(random.random());
        if epic1 > 0 and epic1 < 0.75:
            epicstatus = str(random.choice(wookieeffect));
            wookieeffect.remove(str(epicstatus));
            status.append(str(epicstatus));
        if epic1 > 0 and epic1 < 0.25:
            epicstatus = str(random.choice(wookieeffect));
            wookieeffect.remove(str(epicstatus));
            status.append(str(epicstatus));
        else:
            status.append("no status effect");
    if quality == str("Legendary"):
        legendary1 = float(random.random());
        legendarystatus = str(random.choice(wookieeffect));
        wookieeffect.remove(str(legendarystatus));
        status.append(str(legendarystatus));
        if legendary1 > 0 and legendary1 < 0.5:
            legendarystatus = str(random.choice(wookieeffect));
            wookieeffect.remove(str(legendarystatus));
            status.append(str(legendarystatus));
            legendarystatus = str(random.choice(wookieeffect));
            wookieeffect.remove(str(legendarystatus));
            status.append(str(legendarystatus));
        if legendary1 > 0 and legendary1 < 0.25:
            legendarystatus = str(random.choice(wookieeffect));
            wookieeffect.remove(str(legendarystatus));
            status.append(str(legendarystatus));
    if quality == str("Artifact"):
        artifact1 = float(random.random());
        artifactstatus = str(random.choice(wookieeffect));
        wookieeffect.remove(str(artifactstatus));
        status.append(str(artifactstatus));
        artifactstatus = str(random.choice(wookieeffect));
        wookieeffect.remove(str(artifactstatus));
        status.append(str(artifactstatus));
        if artifact1 > 0 and artifact1 < 0.5:
            artifactstatus = str(random.choice(wookieeffect));
            wookieeffect.remove(str(artifactstatus));
            status.append(str(artifactstatus));
        if artifact1 > 0 and artifact1 < 0.25:
            artifactstatus = str(random.choice(wookieeffect));
            wookieeffect.remove(str(artifactstatus));
            status.append(str(artifactstatus));

if classs == str("StormTrooper"):
    if quality == str("Common"):
        status.append("no status effect");
    if quality == str("Uncommon"):
        uncommon1 = float(random.random());
        if uncommon1 > 0 and uncommon1 < 0.1:
            uncommonstatus = str(random.choice(stormeffect));
            stormeffect.remove(str(uncommonstatus));
            status.append(str(uncommonstatus));
        else:
            status.append("no status effect");
    if quality == str("Rare"):
        rare1 = float(random.random());
        if rare1 > 0 and rare1 < 0.5:
            rarestatus = str(random.choice(stormeffect));
            stormeffect.remove(str(rarestatus));
            status.append(str(rarestatus));
        else:
            status.append("no status effect");
    if quality == str("Epic"):
        epic1 = float(random.random());
        if epic1 > 0 and epic1 < 0.75:
            epicstatus = str(random.choice(stormeffect));
            stormeffect.remove(str(epicstatus));
            status.append(str(epicstatus));
        if epic1 > 0 and epic1 < 0.25:
            epicstatus = str(random.choice(stormeffect));
            stormeffect.remove(str(epicstatus));
            status.append(str(epicstatus));
        else:
            status.append("no status effect");
    if quality == str("Legendary"):
        legendary1 = float(random.random());
        legendarystatus = str(random.choice(stormeffect));
        stormeffect.remove(str(legendarystatus));
        status.append(str(legendarystatus));
        if legendary1 > 0 and legendary1 < 0.5:
            legendarystatus = str(random.choice(stormeffect));
            stormeffect.remove(str(legendarystatus));
            status.append(str(legendarystatus));
            legendarystatus = str(random.choice(stormeffect));
            stormeffect.remove(str(legendarystatus));
            status.append(str(legendarystatus));
        if legendary1 > 0 and legendary1 < 0.25:
            legendarystatus = str(random.choice(stormeffect));
            stormeffect.remove(str(legendarystatus));
            status.append(str(legendarystatus));
    if quality == str("Artifact"):
        artifact1 = float(random.random());
        artifactstatus = str(random.choice(stormeffect));
        stormeffect.remove(str(artifactstatus));
        status.append(str(artifactstatus));
        artifactstatus = str(random.choice(stormeffect));
        stormeffect.remove(str(artifactstatus));
        status.append(str(artifactstatus));
        if artifact1 > 0 and artifact1 < 0.5:
            artifactstatus = str(random.choice(stormeffect));
            stormeffect.remove(str(artifactstatus));
            status.append(str(artifactstatus));
        if artifact1 > 0 and artifact1 < 0.25:
            artifactstatus = str(random.choice(stormeffect));
            stormeffect.remove(str(artifactstatus));
            status.append(str(artifactstatus));

# Getting the stats of the armour based on its generated values
value = 0;
health = 0;
critchance = 0;
damage = 0;
dodge = 0;
damagemitigation = 0;
multistrike = 0;
# Basic armour values
itembudget1 = itembudget / 4;
itembudget2 = itembudget / 4;
itembudget3 = itembudget / 4;
itembudget4 = itembudget / 4;

value += level * 100 * armourbuff;
health += itembudget1 / 100 / 0.85 * armourbuff;
damage += itembudget2 / 20 * armourbuff;
damagemitigation += itembudget3 / 20 * armourbuff;
# Armour values based on attribute values
if attribute == str("Combat Mastery"):
    damage += itembudget4 / 10 * armourbuff;
    value += 20 * level * armourbuff;
if attribute == str("Damage Mitigation"):
    damagemitigation += itembudget4 / 10 * armourbuff;
    value += 20 * level * armourbuff;
if attribute == str("Stamina"):
    health += itembudget4 / 50 * armourbuff;
    value += 20 * level * armourbuff;
if attribute == str("Acuity"):
    critchance += 0.5 * level * armourbuff;
    value += 20 * level * armourbuff;
if attribute == str("Strength"):
    damage += itembudget4 / 10 * armourbuff;
    value += 20 * level * armourbuff;
if attribute == str("Alertness"):
    dodge += level * 0.5 * armourbuff;
    value += 20 * level * armourbuff;
if attribute == str("Multistrike"):
    multistrike += level * 0.5 * armourbuff;
    value += 20 * level * armourbuff;
# Calculate stats based on status effects that arnt unique (eg life leech aura)
if (str("Cyborg Mastery Bonus") in str(status)):
    damage += level * 20 * armourbuff;
if (str("Damage Mitigation Bonus") in str(status)):
    damagemitigation += level * 10 * armourbuff;
if (str("Multistrike") in str(status)):
    multistrike += level * 0.5 * armourbuff;
# Calculate value of status effects based on level and how many status effects
value += len(status) * level * 150 * armourbuff;

# Print all the information for the user
print("Your level " + str(level) + " " + str(classs) + " aquired a " + str(quality) + " " + str(material) + " " + str(armour));
time.sleep(1);
print("It has the attribute of " + str(attribute));
time.sleep(1);
print("and the status effects of " + str(status));
time.sleep(1);
print("The stats of the armour piece are:");
time.sleep(1);
print("Health: " + str(health));
time.sleep(1);
print("Damage: " + str(damage));
time.sleep(1);
print("Crit Chance: " + str(critchance) + "%");
time.sleep(1);
print("Dodge Chance: " + str(dodge) + "%");
time.sleep(1);
print("Damage Mitigation: " + str(damagemitigation));
time.sleep(1);
print("Multistrike Chance: " + str(multistrike) + "%");
time.sleep(1);
print("Value: " + str(value));
print("Press enter to exit");
input();
