string1 = 'Thirty'
string2 = 'Days'
string3 = 'Of'
string4 = 'Python'
result1 = string1 + ' ' + string2 + ' ' + string3 + ' ' + string4
print(result1)

# 2
result2 = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(result2)

# 3
company = "Coding For All"

# 4
print(company)

# 5
print(len(company))

# 6
print(company.upper())

# 7
print(company.lower())

# 8
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9
print(company[0:6])  # or company[:6]

# 10
print('Coding' in company)

# 11
print(company.replace('Coding', 'Python'))

# 12
print(company.replace('Everyone', 'All'))

# 13
print(company.split(' '))

# 14
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(','))

# 15
print(company[0])

# 16
print(company[-1])

# 17
print(company[10])

# 18
phrase1 = 'Python For Everyone'
acronym1 = ''.join([word[0] for word in phrase1.split()])
print(acronym1)  # Output: PFE

# 19
phrase2 = 'Coding For All'
acronym2 = ''.join([word[0] for word in phrase2.split()])
print(acronym2)  # Output: CFA

# 20
print(company.index('C'))

# 21
print(company.index('F'))

# 22
sentence1 = "Coding For All People"
print(sentence1.rfind('l'))

# 23
sentence2 = 'You cannot end a sentence with because because because is a conjunction'
print(sentence2.find('because'))

# 24
print(sentence2.rindex('because'))

# 25
start = sentence2.find('because')
end = sentence2.rindex('because') + len('because')
print(sentence2[start:end])

# 26
print(sentence2.find('because'))

# 27
print(sentence2.replace('because because because', ''))

# 28
print(company.startswith('Coding'))

# 29
print(company.endswith('coding'))

# 30
text = '   Coding For All      '
print(text.strip())

# 31. Método isidentifier()
print("30DaysOfPython".isidentifier())       # False
print("thirty_days_of_python".isidentifier()) # True

# 32. Unir con hash y espacio
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined = ' # '.join(libraries)
print(joined)

# 33. Secuencia de nueva línea
print("I am enjoying this challenge.\nI just wonder what is next.")

# 34. Secuencia de tabulación
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# 35. Formatear el área de un círculo
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {:.0f} meters square.".format(radius, area))

# 36. Mostrar operaciones con formato
a, b = 8, 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")
