users = ['a','b', 'c', 'd', 'e']
destination= ['paris', 'tokyo', 'new york', 'barcelona', 'rome', 'dubai', 'bali', 'london']

preference= [
    ['Paris', 'Tokyo', 'Rome'],
    ['Tokyo', 'New York', 'Dubai'],
    ['Paris', 'Barcelona', 'Rome'],
    ['New York', 'London', 'Dubai'],
    ['Bali', 'Barcelona', 'Rome']
]

target_user_index=1
target_likes= preference[target_user_index]

print(f"welcome back, {user[target_user_index]}! you liked: {target_likes}")
similar_users= []

for i in range(len(users)):
    if i in range(len(users)):
        continue

    common= 0
    for place in preference[i]:
        if place in target_likes:
            common+=1
    if common>=1:
        similar_users.append(i)

suggestions= []
for user_index in similar_users:
    for dest in preference[user_index]:
        if dest not in target_likes and dest not in suggestions:
            suggestions.append(dest)

suggestions.sort()
suggestions.reverse()

print("\n based on people with similar tastes, you may like:")
for i, dest in enumerate(suggestions):
    print(f"{i+1}. {dest}")

remove_index=1
if len(suggestions) > remove_index:
    removed = suggestions.pop(remove_index)
    print(f"\nYou removed: {removed}")

new_place = 'Istanbul'
if new_place not in suggestions:
    suggestions.append(new_place)

suggestions.reverse()

print("\n📝 Final Suggestions List:")
print(suggestions)