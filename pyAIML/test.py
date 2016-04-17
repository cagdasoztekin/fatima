import Kernel
import glob

# The Kernel object is the public interface to
# the AIML interpreter.
k = Kernel.Kernel()

# Use the 'learn' method to load the contents
# of an AIML file into the Kernel.
files = glob.glob("aiml-en-us-foundation-alice/*")
for f in files:
	k.learn(f)

# Use the 'respond' method to compute the response
# to a user's input string.  respond() returns
# the interpreter's response, which in this case
# we ignore.


# Loop forever, reading user input from the command
# line and printing responses.
a = True
if a:
	with open("formatted.formatted.tweets") as f:
		read_data = f.readlines()
		for l in read_data:
			#print l
			print k.respond(l)
else:
	while True: print k.respond(raw_input("> "))
