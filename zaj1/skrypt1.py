from importlib import reload
from os import getcwd
import czas
import time

print("Hello World")
#help(print)
current_path=getcwd()
print(current_path)
print(czas.aktualny_czas)
time.sleep(5)
print(czas.aktualny_czas)
reload(czas)
print(czas.aktualny_czas)