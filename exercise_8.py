for acc in accs:
    if re.search(r"[0123456789]{3,100}", acc):
        print("\t" + acc)
