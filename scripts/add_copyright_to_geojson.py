import json
import sys

file = sys.argv[1]

copyright = sys.argv[2]

data = json.load(open(file))

data['copyright'] = copyright

print json.dumps(data, indent=2)
