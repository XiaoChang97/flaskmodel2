import hashlib
from datetime import datetime

msg = 'hello word'
md5 = hashlib.md5(msg.encode('utf-8'))
print(md5)
r = md5.hexdigest()
print(r)
print(datetime.now())
print(hashlib.sha1(msg.encode('utf-8')).hexdigest())
#64位16进制
print(hashlib.sha256(msg.encode('utf-8')).hexdigest())
#128位16进制
print(hashlib.sha512(msg.encode('utf-8')).hexdigest())