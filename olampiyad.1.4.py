def standardize_name(name):
    return name[0].upper() + name[1:].lower()
def process_names(n, names):
    women = []
    men = []
    for entry in names:
        gender, name, language = entry.split('.')
        name = standardize_name(name)  
        if gender == 'f':
            women.append((name, language))
        else:
            men.append((name, language))


    women.sort(key=lambda x: x[0])
    men.sort(key=lambda x: x[0])
    for name, language in women:
        print(f"f {name} {language}")
    for name, language in men:
        print(f"m {name} {language}")
n = int(input())  
names = [input() for _ in range(n)] 
process_names(n, names)