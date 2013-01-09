import os
from bottle import route, run, redirect, abort, error, template
import csv

def readSource():
  urls = {}
  try:
    reader = csv.reader(open('urls.csv', 'r'), delimiter=',')
    for line in reader:
      urls[line[0]] = line[1]
  except Exception:
    print "Can't read source!"
  return urls

@route('/<c>')
def process(c):
  __urls = readSource()
  if len(__urls) == 0:
    abort(404, "No such identifier")
  if c in __urls.keys():
    url = __urls[c]
    redirect(url)
    return url
  else:
    abort(404, "No URL associated to that identifier")

@error(404)
def error404(error):
  return template('404')
run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
