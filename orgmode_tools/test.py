import os
import sys
from read_orgmode import OrgmodeInfo

path = os.path.join(os.path.expanduser('~'), '.emacs')

try:
    f = open(path, 'r')
except Exception:
    print('noo')
    sys.exit(1)

# remove all line breaks for better parsing
emacs_file = f.read().replace('\n', '')

ok = OrgmodeInfo(emacs_file)

print("Agenda files: ")
for f in ok._agenda_files:
    print(f)

print("Todo keywords: ")
for k in ok._todo_keywords:
    print(k)

print("Tags: ")
for t in ok._tag_names:
    print("Value: {} ID: {}".format(t['name'], t['id']))
