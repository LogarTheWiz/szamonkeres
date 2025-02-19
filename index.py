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
#Határozd meg, melyik országban a legnagyobb a népsűrűség
#Számítsd ki az országok átlagos népsűrűségét
#Számítsd ki az összes ország együttes területét
#Határozd meg az országok népességének mediánját
#Listázd ki azokat az országokat, ahol a népsűrűség nagyobb, mint 150 fő/km²
#Rendezd az országokat területük szerint növekvő sorrendben
#Csoportosítsd az országokat alacsony (100 alatt), közepes (100–300) és magas (300 felett) népsűrűség kategóriákba.