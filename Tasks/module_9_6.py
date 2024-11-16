def all_variants(text):
    for long in range(1, len(text) + 1):
        for j in range(0, len(text)):
            if j + long < len(text) + 1:
                yield text[j:j+long]
    ## ~ 


for i in all_variants("abc"):
    print(i)