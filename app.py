import os
from bottle import route, run, redirect
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

@route('/<c>')
def process(c):
  __urls = readSource()
  if len(__urls) == 0:
    abort(404, "No such identifier")
  try:
    url = __urls[c]
    redirect(url)
    return url
  except KeyError :
    response.status = '404 Not Found'
    return "No URL associated to that identifier\n\n"

run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
