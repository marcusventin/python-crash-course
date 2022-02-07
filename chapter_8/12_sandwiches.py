def sandwich_fillings(*fillings):
    print("Here are the sandwich fillings you requested:")
    for filling in fillings:
        print(f"- {filling}")

sandwich_fillings('egg', 'cress')

sandwich_fillings('cheese', 'tomato', 'egg', 'bacon', 'chicken', 'turkey')