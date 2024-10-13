total = float(input("Введите сумму заказа: "))
if total > 1000:
    discount = total * 0.10
    total -= discount
    print(f"Предоставлена скидка 10%. Итого к оплате: {total}")
else:
    print(f"Итого к оплате: {total}")
