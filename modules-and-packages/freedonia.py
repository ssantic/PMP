province_tax_rates = {
    'Chico': 0.5, 'Groucho': 0.7, 'Harpo': 0.5, 'Zeppo': 0.4}

hour_tax_corrections = {
    '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1,
    '9': 1, '10': 1, '11': 1, '12': 0.5, '13': 1, '14': 1, '15': 1,
    '16': 1, '17': 1, '18': 1, '19': 1, '20': 1, '21': 1, '22': 1,
    '23': 0.95, '24': 0}

def calculate_tax(amount, province, hour):
    tax = float(amount) * \
    province_tax_rates[province] * hour_tax_corrections[str(hour)]
    return float(amount) + tax