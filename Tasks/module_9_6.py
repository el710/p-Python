def all_variants(text):
    for long in range(1, len(text) + 1):
        for j in range(0, len(text)):
            if j + long < len(text) + 1:
                yield text[j:j+long]
    ## ~ 


a = all_variants("abc")
for i in a:
    print(i)