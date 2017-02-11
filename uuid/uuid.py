__author__ = 'ipreacher'

import uuid

uuids = []

def  Security_code():
	for i in range(10):
		uuids.append(uuid.uuid4())
	print(uuids)
	f = open('uuids.txt','w')
	f.write(str(uuids))
	f.close()
	return 0

if __name__ == '__main__':
	Security_code()