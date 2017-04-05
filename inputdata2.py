import urllib
import urllib2

url ="https://republic-of-iot.000webhostapp.com/david_API/addEmp.php"
p1 = raw_input('enter name : ')
p2 = raw_input('enter destination : ')
p3 = raw_input('enter salary: ')

values = {'name' : p1,
          'desg' : p2,
          'salary' : p3} 


data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()

