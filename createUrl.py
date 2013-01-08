import csv
import sys

f = 'urls.csv'
url =  sys.argv[1]
reader = csv.reader(open(f, 'r'), delimiter=',')
urls = {}

for line in reader:
  urls[line[1]] = line[0]

if url in urls.keys():
  print url, "ya existe!",urls[url]
else:
  #for i in range(12737, 12751):
  id = None
  for i in xrange(33, 127):
    id = unichr(int(unicode(hex(i)), 16))
    if not id in urls.values():
      break
  if id == None:
    print "Can't add",url,"to source"
    exit(1)
  urls[url] = id
  print id
  writer = csv.writer(open(f, 'w'), delimiter=',')
  for i in urls:
    writer.writerow([urls[i], i])
  
