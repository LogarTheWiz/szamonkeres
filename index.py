africa = [];
asia = [];
europe = [];
with open('./forras_europa.csv', 'r' ,encoding='utf-8') as forras:
    next(forras);
    for sor in forras:
        adatok = sor.strip().split(';');
        country = {'name':adatok[0],'capital':adatok[1],'size':adatok[2],'pop':adatok[3], 'pop/size':adatok[4]};
        europe.append((country));
with open('./forras_azsia.csv', 'r' ,encoding='utf-8') as forras:
    next(forras);
    for sor in forras:
        adatok = sor.strip().split(';');
        country = {'name':adatok[0],'capital':adatok[1],'size':adatok[2],'pop':adatok[3], 'pop/size':adatok[4]};
        asia.append((country));
with open('./forras_africa.csv', 'r' ,encoding='utf-8') as forras:
    next(forras);
    for sor in forras:
        adatok = sor.strip().split(';');
        country = {'name':adatok[0],'capital':adatok[1],'size':adatok[2],'pop':adatok[3], 'pop/size':adatok[4]};
        africa.append((country));

#Határozd meg, melyik ország rendelkezik a legnagyobb népességgel
#Határozd meg, melyik ország a legnagyobb területű
#Határozd meg, melyik országban a legnagyobb a népsűrűség
#Számítsd ki az országok átlagos népsűrűségét
#Számítsd ki az összes ország együttes területét
#Határozd meg az országok népességének mediánját
#Listázd ki azokat az országokat, ahol a népsűrűség nagyobb, mint 150 fő/km²
#Rendezd az országokat területük szerint növekvő sorrendben
#Csoportosítsd az országokat alacsony (100 alatt), közepes (100–300) és magas (300 felett) népsűrűség kategóriákba.