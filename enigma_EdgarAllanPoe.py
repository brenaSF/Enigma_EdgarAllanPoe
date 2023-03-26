

#Resolvendo o enigma 
stringOriginal= "5 3‡‡† 305)) 6; 4826)4‡.)4‡);80  6;48†8¶60))85;1‡(;:‡8†83(88)  5†;46(;8896?;8)‡(;485);5†  2:‡(;49562(5-4)8¶8;40692  85);)6†8)4‡‡;1(‡9;48081;8:8‡1  ;48†85;4)485†528806*81(‡9;48  ;(88;4(‡?34;48)4‡;161;:188;‡?;"


#Lista os caracteres únicos 
caracteres = set(stringOriginal)
print(caracteres)

#
dicionarioCaracteres = {}

for item in caracteres : 
    dicionarioCaracteres[item ] = stringOriginal.count(item)

for item in sorted(dicionarioCaracteres,key = dicionarioCaracteres.get,reverse=True):
    print(item,  dicionarioCaracteres[item])

nova_string = stringOriginal.replace('8','E')

nova_string = nova_string.replace(';','T')

nova_string = nova_string.replace('4','H')

nova_string = nova_string.replace('(','R')

nova_string = nova_string.replace('6','I')

nova_string = nova_string.replace('9','M')

nova_string = nova_string.replace('‡','O')
nova_string = nova_string.replace('?','U')
nova_string = nova_string.replace('3','G')

nova_string = nova_string.replace('†','D')
nova_string = nova_string.replace('6','I')
nova_string = nova_string.replace('*','N')

nova_string = nova_string.replace('5','A')


nova_string = nova_string.replace('0','L')
nova_string = nova_string.replace(')','S')
nova_string = nova_string.replace('2','B')
nova_string = nova_string.replace('.','P')
nova_string = nova_string.replace('¶','V')
nova_string = nova_string.replace('1','F')
nova_string = nova_string.replace(':','Y')
nova_string = nova_string.replace('9','M')
nova_string = nova_string.replace('-','C')




print(nova_string)