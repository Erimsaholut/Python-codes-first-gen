import pandas as pd

raw_text = """
Italian
English
Word strength


abitare
to live
Strong


agosto
August
Strong


alto / alta
tall
Strong


anch'io
me too
Strong


Anche a me.
me too
Weak


andare
to go
Weak


antipasti
starters
Weak


anziano / anziana
old
Strong


aprile
April
Strong


Arrivederci
Goodbye
Strong


avere caldo
to be hot
Weak


avere fame
to be hungry
Weak


avere freddo
to be cold
Weak


avere mal di denti
to have toothache
Weak


avere mal di pancia
to have bellyache
Weak


avere mal di schiena
to have backache
Weak


avere mal di testa
to have a headache
Weak


avere sete
to be thirsty
Weak


avere sonno
to be sleepy
Weak


basso / bassa
short
Strong


bevande
drinks
Weak


biondo / bionda
blond
Strong


Buon compleanno!
Happy birthday!
Weak


Buonasera
Good evening
Strong


Buongiorno
Good morning
Strong


caldo / calda
hot
Strong


Che ore sono?
What time is it?
Weak


Chi parla?
Who is speaking?
Medium


chiocciola
at
Strong


Ciao ciao!
Bye-bye!
Weak


Ciao!
Goodbye!
Medium


Ciao!
Hello! / Hi!
Strong


Cin cin!
Cheers!
Weak


Come si chiama?
What is your name? (formal)
Strong


Come sta?
How are you? (formal)
Strong


Come stai?
How are you? (informal language)
Strong


Come ti chiami?
What's your name?
Strong


Come va?
How's it going?
Strong


contorni
side dishes
Weak


correre
to run
Strong


così così
so-so
Strong


cucinare
to cook
Strong


data di nascita
date of birth
Strong


Di dov'è?
Where are you from? (formal)
Strong


Di dove sei?
Where are you from?
Strong


dicembre
December
Strong


dodici
twelve
Strong


dodici
dodici
Strong


dolci
desserts
Weak


doppio / doppia
double
Strong


Dove vivi?
Where do you live?
Strong


dovere
to have to, to need to
Weak


essere
to be
Strong


fare danza classica
to do ballet
Strong


fare gli anni
to turn (years)
Weak


fare jogging
to jog
Strong


fare nuoto
to go swimming
Medium


fare palestra
to go to the gym
Medium


fare sport
to do sport
Strong


fare trekking
fare trekking
Strong


fare trekking
to go hiking
Strong


fare un brindisi
to make a toast
Weak


fare un regalo
to give a present
Weak


fare una festa
to have a party
Weak


fare una foto
to take a photo
Weak


fare una torta
to make a cake
Weak


fare yoga
to do yoga
Strong


febbraio
February
Medium


felice
happy
Strong


festeggiare
to celebrate
Weak


freddo / fredda
cold
Strong


frizzante
sparkling
Strong


gennaio
January
Strong


giovane
young
Strong


giugno
June
Weak


gli occhiali
the glasses
Medium


grande
large
Strong


Grazie
Thank you
Strong


guardare la TV
watch TV
Weak


i latticini
dairy products
Weak


i salumi
the cured meats
Weak


il cinema
the cinema
Weak


il collega / la collega
the colleague
Strong


il computer
the computer
Medium


il fine settimana
on the weekends
Medium


il formaggio
the cheese
Weak


il giocatore / la giocatrice
the player
Strong


il giornale
the newspaper
Medium


il latte
the milk
Strong


il libro
the book
Medium


il maiale
the pork
Weak


il manzo
the beef
Weak


il mese
the month
Strong


il pane
the bread
Medium


il pesce
the fish
Weak


il pollo
the chicken
Weak


il portafoglio
the wallet
Medium


il ragazzo
The young man / the guy
Strong


il ragù alla bolognese
the bolognese sauce
Weak


il riso
the rice
Medium


il sale
the salt
Medium


il supermercato
the supermarket
Weak


il teatro
the theatre
Weak


il telefono / il cellulare
the mobile phone
Medium


il vitello
the veal
Weak


iscriversi
to enrol
Medium


l'accendino
the lighter
Medium


l'agnello
the lamb
Weak


l'amico / l'amica
the friend
Strong


l'anno
the year
Strong


l'insalata
the salad
Weak


l'olio
the oil
Medium


l'orologio
the watch
Medium


l'ufficio
the office
Weak


l'ufficio postale
the post office
Weak


l'uomo
the man
Strong


la banca
the bank
Weak


la biblioteca
the library
Weak


la bistecca
the steak
Weak


la borsa
the bag
Strong


la carne
the meat
Weak


la chiesa
the church
Weak


la donna
the woman
Strong


la palestra
the gym
Weak


la palla
the ball
Strong


la pallacanestro
the basketball
Strong


la pallavolo
the volleyball
Strong


la ragazza
The young woman
Strong


la scuola
the school
Weak


la stazione
the train station
Weak


la zuppa
the soup
Weak


lavorare
to work
Strong


lavorare in giardino
to work in the garden
Weak


le chiavi
the keys
Strong


le verdure
the vegetables
Weak


leggere
to read
Strong


lei
she
Strong


lo scontrino
the receipt
Strong


lo zucchero
the sugar
Strong


loro
they
Strong


luglio
July
Strong


lui
he
Strong


luogo di nascita
place of birth
Medium


maggio
May
Strong


male
bad
Strong


mangiare
to eat
Weak


marzo
March
Medium


mezzanotte
midnight
Weak


mezzogiorno
midday / noon
Weak


mia figlia
my daughter
Strong


mia madre
my mother
Strong


mia moglie
my wife
Strong


mia nonna
my grandmother
Strong


mia sorella
my sister
Strong


mio figlio
my son
Strong


mio fratello
my brother
Strong


mio marito
my husband
Strong


mio nonno
my grandfather
Strong


mio padre
my father
Strong


moro / mora
brown-haired
Strong


naturale
still
Strong


nazionalità
nationality
Medium


Neanche a me.
me neither
Weak


noi
we
Strong


novembre
November
Medium


numero di telefono
phone number
Medium


nuotare
to swim
Medium


ogni giorno
every day
Medium


ogni mattina
every morning
Strong


ogni sera
every evening
Strong


ottobre
October
Medium


pagare con la carta
to pay by card
Strong


pagare in contanti
to pay with cash
Strong


parlare
to talk
Strong


pattinare
to skate
Medium


Per favore
Please
Strong


Piacere.
Nice to meet you.
Strong


piccolo / piccola
small
Strong


Prego
You are welcome
Strong


prendere
to have (used when ordering, literally: to take)
Weak


primi
first course
Weak


Pronto?
Hello?
Strong


punto
dot
Strong


quattordici
fourteen
Medium


quindici
fifteen
Medium


sciare
to ski
Strong


secondi
second course
Weak


settembre
September
Medium


Sono le 11 in punto.
It's 11 o'clock.
Weak


Sono le dieci meno un quarto.
It's a quarter to ten.
Weak


Sono le sei e mezzo.
It's half past six.
Weak


Sono le tre e un quarto.
It's a quarter past three.
Weak


spegnere le candeline
to blow out the candles
Weak


stanco / stanca
tired (male / female)
Strong


studiare
to study
Strong


Sì, te lo passo.
Yes, I'll get him for you. / Yes, I'll get her for you.
Weak


tredici
thirteen
Strong


triste
sad
Strong


trovare
to find
Strong


Un attimo, per favore.
One moment, please.
Strong


un caffè
an espresso
Strong


un caffè americano
an americano (espresso diluted with a lot of hot water, in a bigger cup)
Strong


un caffè corretto
an espresso with liqueur (a small amount of liqueur is poured in the espresso)
Strong


un caffè lungo
a long coffee (one shot of espresso with double the water)
Strong


un caffè macchiato
an espresso macchiato (an espresso with a little bit of foamed milk)
Strong


un caffè ristretto
a short espresso (same amount of coffee with half the water)
Strong


un cameriere / una cameriera
a waiter / a waitress
Strong


un cappuccino
a cappuccino
Strong


un commesso / una commessa
a shop assistant
Strong


un cornetto
a croissant
Strong


un gatto / una gatta
a male cat, a female cat
Weak


un giornalista / una giornalista
a journalist
Strong


un infermiere / un'infermiera
a nurse
Strong


un insegnante / un'insegnante
a teacher
Strong


un manager / una manager
a manager
Strong


un negozio
a shop
Strong


un operaio / un'operaia
a factory worker
Strong


un ospedale
a hospital
Strong


un panino
a sandwich
Strong


un ristorante
a restaurant
Strong


un ufficio
an office
Strong


una birra
a beer
Strong


una fabbrica
a factory
Strong


una farmacia
a pharmacy
Weak


una macelleria
a butcher's
Weak


una panetteria
a bakery
Weak


una pasticceria
a patisserie
Weak


una pasticceria
a pastry shop
Strong


una salumeria
a salumeria (a specialist shop which sells different types of cured meat)
Weak


una volta alla settimana
once a week
Strong


undici
eleven
Strong


uno stagista / una stagista
an intern
Strong


vegano / vegana
vegan (male / female)
Weak


vegetariano / vegetariana
vegetarian (male / female)
Weak


venire
to come
Weak


voi
you (plural)
Strong


vuoto / vuota
plain (literally, "empty")
Strong
"""

lines = [line.strip() for line in raw_text.strip().split("\n") if line.strip()]

entries = [lines[i:i+3] for i in range(0, len(lines), 3)]

df = pd.DataFrame(entries, columns=["Italian", "English", "Word strength"])

df.to_csv("italian_words_anki.csv", index=False)

print("CSV dosyası başarıyla oluşturuldu: italian_words_anki.csv")