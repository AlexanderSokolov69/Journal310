from PyQt5.QtCore import Qt

for n in dir(Qt):
    if eval(f'Qt.{n}') == 83:
        print(n)