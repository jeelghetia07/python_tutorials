l  = [12,3,6,2,5,9,8,4,7,11,45]
print(l)

print(l.reverse())                     #anathi akhi list order ma thay jai)
l.append(29)             #anathi list ma chele a no. add thay jai
l.reverse()              #anathi akhi list undhi thay jai
print(l.index(11))                 #e index no. batave
print(l.count(11))             #a ek no. ketli var ave che e kye
m = l.copy()
m[4] = 0
print(m)           #a etle je no. apde laikho ene relace krine biju lakhe che
l.insert(1,14,)             # a etle index 1 upar 14 ne replace kri nakhe
m = [900,4545,567]
l.extend(m)       #a etle m ma je no. che ene ama addd kri nakhe
print(l)