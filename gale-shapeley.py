def get_user_input():
    men_preferences = {}
    women_preferences = {}
    
    num_men = int(input("Enter the number of men: "))
    for _ in range(num_men):
        man = input("Enter the name of the man: ")
        preferences = input(f"Enter {man}'s preferences: ").split()
        men_preferences[man] = preferences
    
    num_women = int(input("Enter the number of women: "))
    for _ in range(num_women):
        woman = input("Enter the name of the woman: ")
        preferences = input(f"Enter {woman}'s preferences: ").split()
        women_preferences[woman] = preferences
    
    return men_preferences, women_preferences

men_preferences, women_preferences = get_user_input()

engaged_to = {}
women_engaged_to = {}

free_men = list(men_preferences.keys())

while free_men:
    m = free_men.pop(0)
    #if not men_preferences[m]:
        #continue  # Skip if man has no more preferences to propose to
    w = men_preferences[m][0]

    if w not in women_engaged_to:
        engaged_to[m] = w
        women_engaged_to[w] = m
    else:
        m_prime = women_engaged_to[w]
        if women_preferences[w].index(m) < women_preferences[w].index(m_prime):
            engaged_to[m] = w
            women_engaged_to[w] = m
            del engaged_to[m_prime]
            free_men.append(m_prime)
        else:
            free_men.append(m)
    men_preferences[m].pop(0)

print("Engagements:", engaged_to)
