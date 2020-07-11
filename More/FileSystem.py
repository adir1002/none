from pathlib import Path

cwd=Path.cwd()
print(cwd)
parent=cwd.parent
print(parent.is_dir())
print()
print(parent.is_file())
for child in parent.iterdir():
    if child.is_dir():
        print(child)

print()
new_file= Path.joinpath(cwd, 'new_text.txt')
print(new_file)

print(new_file.exists())

print('\n\n\n\n')
demo=Path(Path.joinpath(cwd,'demo.txt'))
try :
    print(demo.name)
    print(demo.suffix)
    print(demo.parent.name)
    print(demo.stat().st_size)
except Exception as exex:
    print(exex)
