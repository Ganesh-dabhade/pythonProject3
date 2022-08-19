def get_commission_amount(sales_amount, commission_pct):
    commission_amount = (sales_amount * commission_pct / 100) if commission_pct else 0
    return commission_amount

print(get_commission_amount(1000, 20))