import os
import bottle
import csv

def readSource():
  urls = {}
  try:
    reader = csv.reader(open('urls.csv', 'r'), delimiter=',')
    for line in reader:
      print "Reading", line[0]
      urls[line[0]] = line[1]
  except Exception:
    print "Can't read source!"
  return urls

app = bottle.app()
@app.route('/<c>')
def process(c):
  __urls = readSource()
  if len(__urls) == 0:
    bottle.abort(404, "No such identifier")
  try:
    url = __urls[c]
    bottle.redirect(url)
    return url
  except KeyError :
    bottle.response.status = '404 Not Found'
    return "No URL associated to that identifier\n\n"

bottle.run(app=app,host='0.0.0.0')
