import os
from bottle import route, run, redirect, abort, error, template
import csv
import CreateURL

def readSource():
  urls = {}
  try:
    reader = csv.reader(open('urls.csv', 'r'), delimiter=',')
    for line in reader:
      urls[line[0]] = line[1]
  except Exception:
    print "Can't read source!"
  return urls

@route('/post', method = 'post')
def create():
  c = CreateURL.CreateURL()
  url = c.create('http://asdzxczxczxczxc')
  return url

@route('/post', method = 'get')
def showForm():
  return template('form')

@route('/<c>')
def process(c):
  __urls = readSource()
  if len(__urls) == 0:
    abort(404, "No such identifier")
  if c in __urls.keys():
    url = __urls[c]
    redirect(url, 301)
    return url
  else:
    abort(404, "No URL associated to that identifier")

@error(404)
def error404(error):
  return template('404')
run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
