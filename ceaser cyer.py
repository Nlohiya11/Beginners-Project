letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
to_continue = True
while to_continue:
    choice = input("type encode for encrypting and decode for decrypting : ")
    text = input("input your text : ")
    shift = int(input("the number by which you want to shift the text for encryption : "))
    list_text = list(map(str, text))


    def ceaser_cyper(a, n):
        word = ""
        if a == "decode":
            n *= -1
        for i in list_text:
            if i in letters:
                word_position = letters.index(i)
                word_position += n
                letter = letters[word_position]
                word += letter
            else:
                word += i
        print(f"\nYour {a}d text is {word}")


    shift = shift % 26
    ceaser_cyper(a=choice, n=shift)
    resume = input("\n\ndo you want to continue (yes/no) :")
    if resume == "no":
        to_continue = False
    elif resume == "yes":
        to_continue = True
    else:
        print("wrong input so it will consider as no")
        to_continue = False
