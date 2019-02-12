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
print(ok._agenda_files)
print(ok._todo_keywords)
print(ok._tag_names)
