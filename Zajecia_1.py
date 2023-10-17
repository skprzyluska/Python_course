
import random
liczba_kropek = int(input("Enter the number of dots"))
kropki_w_okręgu = 0
for i in range(liczba_kropek):
    kropka_x = random.uniform(-1, 1)
    kropka_y = random.uniform(-1, 1)
    print(kropka_x, kropka_y)
    kropka_r = (kropka_x * kropka_x) + (kropka_y * kropka_y)
    if ( kropka_r < 1 ):
        kropki_w_okręgu += 1

pi = 4 * (kropki_w_okręgu / liczba_kropek)

print ("pi = ")
print (pi)




