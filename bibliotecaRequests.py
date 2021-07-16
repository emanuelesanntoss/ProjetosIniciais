import requests

WORD_URL = 'http://httpbin.org/'

# Get
r = requests.get(WORD_URL + '/events')
print ('requests.get -> %s = %s' % (r.url, r))


#################### URLs ####################
# HTTP Post
r = requests.post(WORD_URL + '/post', data = {'key':'value'})
print ('requests.post -> %s = %s' % (r.url, r))

# HTTP Put
r = requests.put(WORD_URL + '/put', data = {'key':'value'})
print ('requests.put -> %s = %s' % (r.url, r))

# HTTP Delete
r = requests.delete(WORD_URL + '/delete')
print ('requests.delete -> %s = %s' % (r.url, r))

# HTTP head
r = requests.head(WORD_URL + '/get')
print ('requests.head -> %s = %s' % (r.url, r))

# HTTP Options
r = requests.options(WORD_URL + '/get')
print ('requests.options -> %s = %s' % (r.url, r))

# HTTP Get passando valores
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(WORD_URL + '/get', params=payload)
print ('requests.get -> %s = %s' % (r.url, r))
