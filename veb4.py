
#Лекция 4: «Словари и сортировка подсчётом» 
СОРТИРОВКА ПОДСЧЕТОМ
СТАНДАРТНАЯ ЗАДАЧА: ЕСТЬ N чисел, которые лежат в диапозоне от 0 до K необходимо отсортировать. Стандратная сортировка имеет 
сложность о(N * LOGN)
Идея сортировкой подсчета. Считаем сколько раз некоторый k -тый символ входит в массив. ВАЖНО ЧТОБЫ K БЫЛО НЕБОЛЬШИМ
СТАНДАРТНЫЙ КОД:

def countsort(seq):
    min_r = min(seq)
    max_r = max(seq)
    len_seq =  max_r - min_r + 1 # длина диапозона
    k = [0]*len_seq
    for i in range(len(seq)):
        k[seq[i]-min_r]+=1 
        
    nowpos = 0
    for val in range(0,k):
        for i in range(count[val]):
            seq[nowpos] = val + minval # меняю исходную последовательность на отсортированную 
            nowpos+=1
          
ЛЮТАЯ ИМБА: КАК ПОНЯТЬ ЧТО ИЗ СИМВОЛОВ ОДНО ЧИСЛА МОЖНО СОСТАВИТЬ ДРУГОЕ! ПРОСТО ПОСЧИТАТЬ! АФИГЕТЬ... ТАК ЖЕ ПРОСТО

ГЛАВА 2:  СЛОВАРИ

Позволяет по ключу узнавать значение . Как множество - к каждому ключу прописано значение. 
Однако искать по значению нельзя. Это как в реальном словаре, который работает в одну строну. 
С одной стороны это отсортированно по буквам, но по русским 
а для анлийских ничего нет


Задача: данна шахматная доска. на ней стоят ладьи. сколько ладьей ббьют друг друга.
ПРИКОЛ ЗАДАЧИ: доска может быть гигантская, просто ограменная, однако количество ладей ограниченно. Это позволяет нам воспользоваться
словарями
def addrook(row_or_col,key):
    if key not in row_or_col: # проверяет есть ли уже данный столбец/строка в массиве данных, 
        row_or_col[key] = 0# если нет то создает
    row_or_col[key]+=1 # прибавляет к количеству  единицу 

def counparis(row_or_col,key):
    pairs = 0 
    for key in row_or_col:
        pairs += row_or_col[key] - 1 
    return pairs
  
rook_in_row ={}
rook_in_col ={}
for row, col in rookcoors:  #перебор пар элементо в массиве данных с координатами ладей по строчкамrow и столбцам col
    add(rooksinrow,row)#функции создающие словари с ключами(номера строк)и количествами ладей в одной строке/столбце
    add(rooksincol,col)
print(counparis(rooksinrow) + counparis(rooksincol))

### ГЛАВА 3: задел под оптимизацию
Как оценить качество алгоритма кроме сложности:

1) Требование памяти
2) Сложность поддержки
3) Возможность расспараллелливания
4) Необходимая классификаиця сотрудника


На сортировка обычно требуется n log n времени

Сколько слов в строке состоят из одних и тех же буковок? вывести такие слова

def groupwords(word):
  def keywords:
    symcnt = {}
    for i in word: # Только что понял имбулечку словарей: мы в качестве индексов используем элементы строки/массива
      if( word[i] not in symcnt):
        symcnt[i] = []
      symcnt[i]+=1 
    for i in sorted(symcnt.keys()): # Функция keys() в Python используется для получения всех ключей из словаря.
       lst.append(i) # добавляем символ
       lst.append(symcnt[i]) # добавляем сколько раз он встречается . Символы автоматически отсортированны
    return ''.join(lst)
  group = {}
  for word in words:
    groupkey = keywords(word)
    if(groupkey not in group):
      group[groupkey] = []
    group[groupkey].append(words)
  ans = []
  for groupkey in group:
    ans.append(group[gruopkey])
  return ans


    
      

ДОМАШНЯЯ РАБОТА :

ВВОД МНОГОСТРОЧНОГО ТЕКСТА :

input_text =  []
while True:
    try:
        line = input()
        if not line:
            break
        input_text.extend(line.split())
    except: EOFError
        break


a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)  # Вывод: [1, 2, 3, 4, 5, 6]
        

СОЗДАНИЕ ДВУМЕРНОГО СПИСКА:
def add(name, product,amount):
    if(name not in family_buying):
        family_buying[name] = {}
    if(product not in family_buying[name]):
        family_buying[name][product] = amount
    else:
        family_buying[name][product] += amount
    
    
    
    
family_buying = {}
input_text =  []
while True:
    try:
        line = input()
        if not line:
            break
        input_text.append(line)
    except EOFError:
        break
   
    
for line in input_text:
    name, product, amount  = map(str, line.split())
    add(name,product,int(amount))
    
for i in sorted(family_buying.keys()):
    print(i+':')
    for j in sorted(family_buying[i].keys()):
        print(j, family_buying[i][j])
АФИГЕТЬ В ПИТОНЕ НАПРЯМУЮ МОЖНО СРАВНИВАТЬ СЛОВАРИ. А Массивы?

