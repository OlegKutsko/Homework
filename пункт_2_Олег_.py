card = input("Введиите номер карточки:")
if len(card)==16 and card.isdigit():
    def card_hide(card):
        return '*' * (len(card)-4) + card[-4:]
    print(card_hide(card))
else:
    print("Ошибка: проверьте количество цифр и отсутствие букв")
