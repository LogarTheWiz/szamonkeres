import statistics;
africa = [];
asia = [];
europe = [];
with open('./forras_europa.txt', 'r' ,encoding='utf-8') as forras:
    next(forras);
    for sor in forras:
        adatok = sor.strip().split(';');
        country = {'name':adatok[0],'capital':adatok[1],'size':adatok[2],'pop':adatok[3], 'pop/size':adatok[4]};
        europe.append((country));
with open('./forras_azsia.txt', 'r' ,encoding='utf-8') as forras:
    next(forras);
    for sor in forras:
        adatok = sor.strip().split(';');
        country = {'name':adatok[0],'capital':adatok[1],'size':adatok[2],'pop':adatok[3], 'pop/size':adatok[4]};
        asia.append((country));
with open('./forras_afrika.txt', 'r' ,encoding='utf-8') as forras:
    next(forras);
    for sor in forras:
        adatok = sor.strip().split(';');
        country = {'name':adatok[0],'capital':adatok[1],'size':adatok[2],'pop':adatok[3], 'pop/size':adatok[4]};
        africa.append((country));
def sortkey0(e):
    return e['name'];
def sortkey1(e):
    return e['capital'];
def sortkey2(e):
    return e['size'];
def sortkey3(e):
    return e['pop'];
def sortkey4(e):
    return e['pop/size'];
tempeurope = europe;
tempasia = asia;
tempafrica = africa;
tempeurope.sort(key=sortkey2, reverse=True);
tempasia.sort(key=sortkey2, reverse=True);
tempafrica.sort(key=sortkey2, reverse=True);
print(f'Legnagyobb országok:\n Európa: {tempeurope[0]['name']},{tempeurope[0]['size']} \n Ázsia: {tempasia[0]['name']},{tempasia[0]['size']} \n Afrika: {tempafrica[0]['name']},{tempafrica[0]['size']}');
tempeurope = europe;
tempasia = asia;
tempafrica = africa;
tempeurope.sort(key=sortkey3, reverse=True);
tempasia.sort(key=sortkey3, reverse=True);
tempafrica.sort(key=sortkey3, reverse=True);
print(f'Legnépesebb országok:\n Európa: {tempeurope[0]['name']},{tempeurope[0]['pop']} \n Ázsia: {tempasia[0]['name']},{tempasia[0]['pop']} \n Afrika: {tempafrica[0]['name']},{tempafrica[0]['pop']}');
tempeurope = europe;
tempasia = asia;
tempafrica = africa;
tempeurope.sort(key=sortkey4, reverse=True);
tempasia.sort(key=sortkey4, reverse=True);
tempafrica.sort(key=sortkey4, reverse=True);
print(f'Legnagyobb népsűrűségű országok:\n Európa: {tempeurope[0]['name']},{tempeurope[0]['pop/size']} \n Ázsia: {tempasia[0]['name']},{tempasia[0]['pop/size']} \n Afrika: {tempafrica[0]['name']},{tempafrica[0]['pop/size']}');
europepopsize = [];
for country in europe:
    europepopsize.append(country['pop/size']);
asiapopsize = [];
for country in asia:
    asiapopsize.append(country['pop/size']);
africapopsize = [];
for country in africa:
    africapopsize.append(country['pop/size']);
print(f'Népesség mediánok:\n Európa:{statistics.median(europepopsize)} \n Ázsia:{statistics.median(asiapopsize)} \n Afrika:{statistics.median(africapopsize)} \n');
europesize = 0;
for country in europe:
    europesize += country['size'];
asiasize = 0;
for country in asia:
    asiasize += country['size'];
africasize = 0;
for country in africa:
    africasize += country['size'];
print(f'Európa:{europesize}');
print(f'Ázsia:{asiasize}');
print(f'Afrika:{africasize}');
#Határozd meg az országok népességének mediánját
#Listázd ki azokat az országokat, ahol a népsűrűség nagyobb, mint 150 fő/km²
#Rendezd az országokat területük szerint növekvő sorrendben
#Csoportosítsd az országokat alacsony (100 alatt), közepes (100–300) és magas (300 felett) népsűrűség kategóriákba.