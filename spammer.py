import pyautogui as spam
import time

limite_msa=input('n msg:')
msg = input('Coleque a msg:')

i=0
time.sleep(2)

while i<int(limite_msa):
    spam.typewrite(msg)
    spam.press('Enter')

    i+=1