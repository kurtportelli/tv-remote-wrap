def tv_remote(words):
    #define starting conditions
    keyboard = ('abcde123',
                'fghij456',
                'klmno789',
                'pqrst.@0',
                'uvwxyz_/',
                ('|', ' ', None, None, None, None, None, None))
    previous_x, previous_y = 0, 0
    previous_lower = True
    words = list(words)
    char_no = 0
    presses = 0
    
    while char_no < len(words):
        char = words[char_no]
        
        #if shift is needed, add its symbol to list and skip to next iteration
        if char.islower() != previous_lower and char.isalpha():
            words.insert(char_no, '|')
            previous_lower = not previous_lower
            continue
    
        #find the coordinates of the current character
        for row in range(len(keyboard)):
            if char.lower() in keyboard[row]:
                y = row
                x = keyboard[row].index(char.lower())
                break
        
        presses += min(abs(x - previous_x), (8 - abs(x - previous_x))) + \
                   min(abs(y - previous_y), (6 - abs(y - previous_y))) + 1
        previous_x, previous_y = x, y
        char_no += 1
    
    return presses
