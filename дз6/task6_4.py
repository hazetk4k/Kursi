# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)
violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]
song1 = violator_songs_list[3][1]
song1_name = violator_songs_list[3][0]
blur = violator_songs_list[5][1]
blur_name = violator_songs_list[5][0]
song3 = violator_songs_list[-1][1]
song3_name = violator_songs_list[-1][0]
com_time = song1 + blur + song3
print(f"Общее время песен {song1_name}, {blur_name}, {song3_name} равно {com_time:.6g}")
#понятие не имею как расшифровывается .6g но оно работает) пока что ищу инфу
