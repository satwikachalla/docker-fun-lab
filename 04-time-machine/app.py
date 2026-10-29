import sys

print("Running on Python", sys.version.split()[0])
if sys.version_info >= (3, 10):
    print("Modern Python: match/case and 'X | Y' type syntax are available")
else:
    print("Legacy Python: no match/case, no 'X | Y' type syntax")
