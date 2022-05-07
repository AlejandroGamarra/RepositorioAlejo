import re
regex=r"[456][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}"
tarjetas = ['4123456789123456','5123-4567-8912-3456','61234-567-8912-3456','4123356789123456','5133-3367-8912-3456','5123 - 3567 - 8912 - 3456']
for f in tarjetas:
    if re.match(regex,f):
        print(f"{f} es Valido")
    else:
        print(f"{f} NO es Valido")