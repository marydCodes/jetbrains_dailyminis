seasons_file = open('seasons.txt', 'r', encoding='utf-8')

seasons = seasons_file.readlines()
#favorite_season = seasons[2]

seasons_file.close()


print(seasons) # file.readlines() = every line as item in a list
#print(favorite_season)
favorite_season = seasons[2]
print(favorite_season)

print(*seasons)

print(*seasons[0])

for word in seasons:
    print(word[0])