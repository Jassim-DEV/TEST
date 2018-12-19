import random
import collections

letter=[random.choice('RJBOVN') for _ in range(4)] 
print(*letter)
count=collections.Counter(letter)
chance=10



def run():
    newtest=input('Entrez 4 lettres parmis R,J,B,O,V et N:')
    newtest_count=collections.Counter(newtest)
    
    misplaced = sum(min(count[k], newtest_count[k]) for k in count)
    juste = sum(a==b for a,b in zip(letter, newtest))
    
    misplaced = misplaced-juste
    inchance=attempt+1
    
    print('|-------------------|\n|{}| {} | {} | {}/10 | \n|-------------------|'.format(''.join(newtest), juste, misplaced,inchance))
    return juste!=4
    
for attempt in range(chance):
    if not run():
        print('BRAVO ! Vous avez terminé en {} tours'.format(attempt+1))
        break
    else:
        pass
else:
    print ('Game over, voici le code {} '.format(''.join(letter)))