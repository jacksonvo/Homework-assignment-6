for acc in accs:
    if re.search(r"^(x|y)", acc):
        print("\t" + acc)

