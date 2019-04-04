from pokemon import Pokemon
import time

pika = Pokemon('ピカチュウ', 30, 13)
zeni = Pokemon('ゼニガメ', 50, 6)

print('************************\n戦闘開始\n************************')

i = 0
while pika.ap > zeni.ap or pika.ap < zeni.ap:
    i += 1
    count = eval('+1')
    if pika.ap > zeni.ap:
        zeni.hp = zeni.hp - pika.ap
        print(
            '第' + str(i) + '戦' + '\n' + 
            '---------' + '\n' + 
            'ピカチュウの残りHP: ' + str(pika.hp) + '\n' + 
            'ゼニガメの残りHP: ' + str(zeni.hp)
            )
    elif pika.ap < zeni.ap:
        pika.hp = pika.hp - zeni.ap
        print(
            '第' + str(i) + '戦' + '\n' + 
            '-------' + '\n' + 
            'ピカチュウの残りHP: ' + str(pika.hp) + '\n' + 
            'ゼニガメの残りHP: ' + str(zeni.hp)
        )
    time.sleep(1)
    if pika.hp <= 0 or zeni.hp <= 0: 
        time.sleep(2)
        if pika.hp <= 0:
            print(
                '************************\n決着!!\n************************'  + '\n' + 
                'ピカチュウ瀕死..ゼニガメ勝利!!!'
            )
        elif zeni.hp <= 0:
            print(
                '************************\n決着!!\n************************'  + '\n' + 
                'ゼニガメ瀕死..ピカチュウ勝利!!!'
            )
        break

