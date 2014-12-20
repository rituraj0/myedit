from datetime import datetime
import uuid
import calendar

d = datetime.utcnow()
uc=calendar.timegm(d.utctimetuple())

uu=uuid.uuid1();
st="hello"
st=str(uu);
print(st);
print(d);
print(uc);
