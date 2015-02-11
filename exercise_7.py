or acc in accs:
    if re.search(r"^(x|y).*e$", acc):
        print("\t" + acc)
