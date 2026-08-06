from pathlib import Path


r = Path(".").cwd().parent.parent
print(r.absolute())
