
num_people = int(input('Enter the number of people attending the cookout: '))
hotdogs_per_person = int(input('Enter the number of hot dogs each person will be given: '))


hotdog_packages = (num_people * hotdogs_per_person) // 10
bun_packages = (num_people * hotdogs_per_person) // 8

hotdogs_leftover = (num_people * hotdogs_per_person) % 10
buns_leftover = (num_people * hotdogs_per_person) % 8

print('Minimum number of hot dog packages required:', hotdog_packages)
print('Minimum number of hot dog bun packages required:', bun_packages)
print('Number of hot dogs left over:', hotdogs_leftover)
print('Number of hot dog buns left over:', buns_leftover)
