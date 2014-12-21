import os;
from subprocess import call
import subprocess 

#call( 'python test.py > o.txt');

cmd = " python test.py "

filename = "test.py";

ans = subprocess.check_output( [ 'python' , filename ] );

print(ans);