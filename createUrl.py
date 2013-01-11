import csv
import sys
import time


class CreateURL: 
  baseUrl = 'http://0n.cl'
  def getParam(self, m):
    n = m
    s = []
    chars =  map(unichr, range(43, 123))
    base = len(chars)
    if n < base:
      return n
    while n > 0:
      x = n/base
      s.append(chars[n%base])
      n = x
    
    s.reverse()
    return m 

  def create(self, url):
    f = 'urls.csv'
    reader = csv.reader(open(f, 'r'), delimiter=',')
    urls = {}
    for line in reader:
      urls[line[1]] = line[0]
    
    currentSize = len(urls)
    id = self.getParam(currentSize)
    
    if url in urls.keys():
      id = urls[url]
    else:
      #for i in range(12737, 12751):
      if id == None:
        print "Can't add",url,"to source"
        exit(1)
      urls[url] = id
      writer = csv.writer(open(f, 'w'), delimiter=',')
      for i in urls:
        writer.writerow([urls[i], i])
    
    return "%s/%s" %(self.baseUrl,id)

