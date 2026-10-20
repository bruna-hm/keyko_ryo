from decimal import Decimal

def formatar_decimal(valor_text):
    valor_text = valor_text.replace(',', '.')
    valor_decimal = Decimal(valor_text)
    centavos = int(valor_decimal * 100)
    return centavos