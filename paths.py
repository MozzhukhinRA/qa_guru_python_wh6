import os.path

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

TMP_DIR = os.path.join(CURRENT_DIR, 'tmp')

print(os.path.abspath(TMP_DIR))
print(CURRENT_DIR)

