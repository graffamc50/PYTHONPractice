

#Python was created by Guido van Rossum
vocab = ['False', 'class', 'return', 'is', 'finally', 'none', 'if', 'for', 'lambda', 'continue', 'True', 'def', 'from', 'while', 'nonlocal', 'and', 'del', 'global', 'not', 'with', 'as', 'instance', 'method', 'elif', 'try', 'or', 'yield', 'assert', 'else', 'import', 'pass', 'break', 'except', 'in', 'raise']

#+,-,*,/,** = power, % = remainder
#

z = '------------------------------------------------------------------------'

a = 5
b = 2
c = a % b
print(c)

print('hello world')

print(z)

#Sequential Steps
x = 1    #assignment statement
x = x+1  #assignment with expression
print(x) #print statement
#variable, operator, constant, reserved word

#Conditional Steps
#"nested" if (wrong??)
x = 1
if x < 0:
    print('less than 0')
    if x > 0:
        print('more than 0')
        if x == 0:
            print('it be 0')
print('all done')

x = 1
if x == 0:
    print('hi')
else:
    print('bye')

x = 1
if x == 0:
    print('no poop')
elif x == 1:
    print('1 poop')
print('poop complete')

x = 5
if x == 0:
    print('no poop')
elif x == 1:
    print('1 poop')
elif x == 2:
    print('2 poops')
else:
    print('too many poops')



#Repeated Steps
x = 5
while x < 1000000:
   print(x)
   x = x**2
print("woooooo")

print('Please wait 2 seconds')
#time.sleep(2)


#continue runs the code over again from the top
#break escapes the loop

for i in range(6):
    print(i)

for i in [5,4,3,2,1]:
    print(i)
print('GO!')

largest_so_far = -100
for num in [2,3,6,3445,74,1324]:
    if num > largest_so_far:
        largest_so_far = num
        print(largest_so_far, num)
    else:
        print(largest_so_far, num)
print(str(largest_so_far) + ' is the largest number.')

winners = ['colton', 'andy', 'lauren']
e = 'goes to: '
r = '!!!'
count = 0
for i in winners:
    count = count+1
    print(count, e, i, r)


#x = input('enter a number:')

print(z)

x = 'hello' + ' ' + 'there'
print(x)

#Types
print(type('hello'))
print(type(1))
#int -> float
print(type(float(1)))
#str -> int
x = '123'
print(type(x))
print(type(int(x)))
#int / float -> str
x = str(int(123))
print(type(x))


    
print(z)

#error avoidance / detection "try and except stuff"
try:
    x = int('hello')
except:
    x = 1
print(x)

try:
    x = int('123')
except:
    x = 1
print(x)

print(z)

#define and functions
def thing():
    print('hello')
    print('goodbye')
thing()

print(max('hello za world'))

def greet(gen):
    if gen == 'M':
        return 'what up man'
    elif gen == 'F':
        return 'what up lady'
    else:
        return 'what even are you'
print(greet('M'))
print(greet('apache helicopter'))

def greet():
    return 'Hello'
print(greet(), 'Colton')

def divide(a,b):
    print(a/b)
    print(a%b)
divide(100,6)

print(z)

# STRINGS
s = 'woop diddy scoop'
print(s[0:4])
print(s[5:])
print(s[:])

w = 'WhAt IS uP'
print(w.lower())
print(w.upper())

w = '    What is up       '
print(w.lstrip())
print(w.rstrip())
print(w.strip())

w = 'What is up'
print(w.startswith('What'))
print(w.startswith('w'))

#file reading
handle = 'mbox.txt'
fhand = open(handle)
for lines in fhand:
    lines = lines.rstrip()
    #print(lines)


w = 'hello\nworld'
print(w)

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 3 or wds[0] != 'From':
        continue
    print(wds[2])

#LISTS

#lists are mutable, str are immutable
lotto = [2,14,43,34,51]
print(list(lotto))
print(lotto[2])
lotto[2] = 100
print(lotto[2])

a = [1,3,2]
b = [4,5,6]
c = a+b
print(c)
print(c[:3])
c.append(7)
print(c)
c.sort()
print(c)
print(c.reverse())

abc = 'A whole three words'
print(abc)
abc = abc.split()
print(abc)
for i in abc:
    print(i)

w = abc[1]
print(w.split('o'))

#dictionaries
counts = dict()
names = ['colton', 'andy', 'andy', 'colton', 'colton']
mydictionary = { }
print('Hello' in mydictionary)
for name in names:
    counts[name] = counts.get(name, 0) +1
print(counts)
for key in counts:
    print(key, counts[key])


print(z)

#GET and Items methods?


fname = 'clown.txt'
fhand = open(fname)
di = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for w in words:
        di[w] = di.get(w,0) + 1
print(di)

print('The most used word is:',max(di), 'for a total of:', max(di), 'times.')


print(z)
#Tuples
#immutable

x = (1,2,3)

fhand = open('romeo.txt')
d = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for w in words:
        d[w] = d.get(w, 0)+1
print(d)
l = list()
for k,v in d.items():
    l.append((v,k))
l = sorted(l,reverse=True)
print(l)
for v,k in l[:10]:
    print(k,v)

d = {'a':10,'c':22,'b':1}
t = sorted(d.items())
for k,v in t:
    print(k,v)
l = list()
for k,v in d.items():
    l.append((v,k))
print(l)
l = sorted(l)
print(l)
l = sorted(l, reverse=True)
print(l)

d = {'a':10,'c':22,'b':1}
print( sorted( [ (v,k) for k,v in d.items() ] ) )

print(z)

#Python Regular Expression Quick Guide

#^    Matches the beginning of a line
#$    Matches the end of the line
#.    Matches any character
#\s   Matches whitespace
#\S   Matches any non-whitespace character
#*    Repeats a character zero or more times
#*?   Repeats a character zero or more times (non-greedy)
#+    Repeats a character one or more times
#+?   Repeats a character one or more times (non-greedy)
#[aeiou]  Matches a single character in the listed set
#[^XYZ]   Matches a single character not in the listed set
#[a-z0-9] The set of characters can include a range
#(    Indicates where string extraction is to start
#)    Indicates where string extraction is to end

import re
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)

import re
line = 'From: stephen.marquard@uct.ac.za 10:10:10'
y = re.findall('^From .*@([^ ]*)',line)
print(y)

print(z)

import re
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    y = re.findall('^F.+:',line)
    if len(y) < 6: continue
    print(y)

print(z)

#SOCKETS and WEBBROWSER

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n' .encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

#shortened socket open
import urllib.request, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

#Web scraping / crawling

import urllib.error
import ssl

# to ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://www.dr-chuck.com'
html = urllib.request.urlopen(url, context=ctx)
#soup = BeautifulSoup(html, 'html.parser')

#retrieves all anchor tags
#tags = soup('a')
#for tag in tags:
#    print(tag.get('href', None))

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

#SOME BASIC XML STUFF

#import xml.entree.ElementTree as ET
data = '''
<person>
    <name>Colton</name>
    <phone type="intl">
    +1 734 303 4456
    </phone>
    <email hide="yes"/>
</perons>'''

#tree = ET.fromstring(data)
#print('Name:', tree.find('name').text)
#print('Attr:', tree.find('email').get('hide'))


#SOME JSON STUFF

import json

data2 = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data2)
print('Name:', info["name"])
print('email', info["email"]["hide"])

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    break
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)

#API = allpication program interface

# what does the .  between variables mean tho

print(dir(list()))

#how to use self in python
#how to use classes in python
#
#Class = template
#Attribute - variable within a class
#Method - a function in a class
#Object - a particular instance of a class
#Constructor - code that runs when an object is created
#Inheritance - the ablility to extend a class to make a new class
#
#SQL
#structured query data
#create tables, retrieve data, insert data, delete data

#INSERT INTO Users (name, email) VALUES ('Kristin', 'kf@umich.edu')
#DELETE FROM Users WHERE email='ted@umich.edu'
#UPDATE Users SET name="Charles" WHERE email='csev@umich.edu'
#SELECT * FROM Users
#SELECT * FROM Users WHERE email='csev@umich.edu'
#SELECT * FROM Users ORDER BY email

#SQLits in practice

import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

#fname = input('Enter file name: ')
#if (len(fname) < 1): fname = 'mbox-short.txt'
fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()

print(z)


