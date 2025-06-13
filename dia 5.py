empty_list = []

my_list = [1, 2, 3, 4, 5, 6]

length_of_list = len(my_list)

first_item = my_list[0]
middle_item = my_list[len(my_list) // 2]
last_item = my_list[-1]

mixed_data_types = ["Your Name", 30, 5.9, "Single", "Your Address"]

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

print(it_companies)

print(len(it_companies))

first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]
print(first_company, middle_company, last_company)

it_companies[0] = "Meta" 
print(it_companies)

it_companies.append("Netflix")

it_companies.insert(len(it_companies) // 2, "Spotify")

for i in range(len(it_companies)):
    if it_companies[i] != "IBM":
        it_companies[i] = it_companies[i].upper()

joined_companies = '#;  '.join(it_companies)
print(joined_companies)

company_exists = "Google" in it_companies
print(company_exists)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

first_three_companies = it_companies[:3]
print(first_three_companies)

last_three_companies = it_companies[-3:]
print(last_three_companies)

middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    middle_companies = it_companies[middle_index - 1:middle_index + 1]
else:
    middle_companies = it_companies[middle_index:middle_index + 1]
print(middle_companies)


it_companies.pop(0)


middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    it_companies.pop(middle_index - 1)  
    it_companies.pop(middle_index) 


it_companies.pop()

it_companies.clear()


del it_companies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

full_stack = front_end + back_end

full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')

print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
min_age = min(ages)
max_age = max(ages)

ages.append(min_age)
ages.append(max_age)

n = len(ages)
if n % 2 == 0:
    median_age = (ages[n // 2 - 1] + ages[n // 2]) / 2
else:
    median_age = ages[n // 2]

average_age = sum(ages) / len(ages)

age_range = max_age - min_age

min_avg_diff = abs(min_age - average_age)
max_avg_diff = abs(max_age - average_age)

print(f"Sorted ages: {ages}")
print(f"Min age: {min_age}, Max age: {max_age}")
print(f"Median age: {median_age}")
print(f"Average age: {average_age}")
print(f"Age range: {age_range}")
print(f"Min - Average difference: {min_avg_diff}, Max - Average difference: {max_avg_diff}")

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
n_countries = len(countries)

if n_countries % 2 == 0:
    middle_countries = countries[n_countries // 2 - 1:n_countries // 2 + 1]
else:
    middle_countries = countries[n_countries // 2]

if n_countries % 2 == 0:
    first_half = countries[:n_countries // 2]
    second_half = countries[n_countries // 2:]
else:
    first_half = countries[:n_countries // 2 + 1]
    second_half = countries[n_countries // 2 + 1:]

first_three, *scandic_countries = countries

print(f"Middle country(ies): {middle_countries}")
print(f"First half: {first_half}, Second half: {second_half}")
print(f"First three countries: {first_three}, Scandic countries: {scandic_countries}")
