
def combine_lists():
    first = ['Behind', 'every', 'great', 'man']
    second = ['is', 'a', 'woman']
    third = ['rolling', 'her', 'eyes']
    full = first + second + third
    print(' '.join(full))

def merge_list():
    menus = ["chicken strip", "beef burger", "steakhouse", "mushroom swiss", "whopper"] # List A
    price = [15,10,12,20,30] # List B
    menus.sort()
    price.sort()
    print(dict(zip(menus, price)))

def char_counter(text):
    obj_text = {} 
    text = text.lower()
    for i in text: 
        if i in obj_text: 
            obj_text[i] += '*'
        else: 
            obj_text[i] = '*'
    print(obj_text)

def bubble_sort(numbers):
    is_swap = True
    while(is_swap):
        is_swap = False
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                is_swap = True
    print(numbers)

def masking(text):
    not_mask = 3
    mask =''
    text_len = len(text)-not_mask
    for i in range(text_len):
        mask += '*'
    print(mask+text[text_len:])

# def missing_alphabet(text):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     alphabet = set(alphabet)
#     text = set(text)
#     print(alphabet.difference(text))

# missing_alphabet(['a,'])

def sort_odd(mynumbers):
    sorted_numbers_odd = sorted([item for item in mynumbers if item%2 != 0])
    index_odd= 0
    for i in range(len(mynumbers)):
        if mynumbers[i] %2 != 0:
            mynumbers[i] = sorted_numbers_odd[index_odd]
            index_odd += 1
    print(mynumbers)


