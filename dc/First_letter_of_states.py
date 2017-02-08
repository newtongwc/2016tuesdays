states = ['alaska', 'alabama', 'arkansas', 'arizona', 'california', 'colorado', 'connecticut', 'delaware',
        'florida', 'georgia', 'hawaii', 'iowa', 'idaho', 'illinois', 'indiana', 'kansas', 'kentucky', 'louisiana',
        'massachusetts', 'maryland', 'maine', 'michigan', 'minnesota', 'missouri', 'mississippi', 'montana',
        'north Carolina', 'north Dakota', 'nebraska', 'new hampshire', 'new jersey', 'new mexico', 'nevada',
        'new york', 'ohio', 'oklahoma','oregon', 'pennsylvania', 'rhode island', 'south carolina', 'south dakota',
        'tennessee', 'texas', 'utah', 'virginia', 'vermont', 'washington', 'wisconsin', 'west wirginia', 'wyoming']

while True:
    ur_state = raw_input("Type a letter of the alphabet to find out which states start with that letter\n--->")

    for state in states:
        if state.startswith(ur_state):
            print state

    new_state = raw_input("Now type a letter of the alphabet to find out which states has that letter in it\n--->")

    for stat in states:
        if stat.find(new_state):
            print stat









