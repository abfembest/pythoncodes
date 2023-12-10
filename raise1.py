acct = 2000
debit = 4000
if acct > debit:
    bal = acct - debit
    print(bal)
else:
    raise Exception("Insufficient fund")
