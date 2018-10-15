import subprocess
import sys

command = ['cb', sys.argv[1], sys.argv[2]]

try:
 subprocess.call(command)

except Exception:
  print "no such command", Exception.message.__str__()
