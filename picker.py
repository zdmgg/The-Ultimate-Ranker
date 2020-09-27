import time, re
teams = dict()

# Function for exiting the program
def exitfunc(i):
    if re.match('[Ee][Xx][Ii][Tt]', i):
        time.sleep(0.5)
        print('\nExiting...')
        time.sleep(0.5)
        exit()

def calcscore(team):
    team

print('\n\nSWISS PICKER WITH BUCHHOLZ')
time.sleep(1)
print("Type 'exit' whenever you want to exit the program.")
time.sleep(1)


# STEP 1: Inputting team names
print('\nStep 1: Inputting teams')
time.sleep(1)

# Importing teams or inputting teams?
while True:
    yn = input('\nWould you like to import team names?\n> ')
    exitfunc(yn)
    time.sleep(0.5)

    # Importing teams
    if re.match('[Yy][Ee][Ss]', yn):
        while True:
            file = input('\nPlease enter the file name.\n> ')
            exitfunc(file)
            try:
                imp = open(file)
            except:
                print('\nError: file not found. Please try again.')
                time.sleep(0.5)
                continue
            break
        for line in imp:
            line = line.strip()
            teams[line] = [0, 0]
        time.sleep(1)
        print('\nStep 1 is finished!')
        time.sleep(1)
        print('\nYou have inputted', len(teams), 'teams into the tournament.')

        # Showing inputted teams
        ctr = 0
        time.sleep(1)
        print('\nHere are your inputted teams:\n')
        for team in teams.keys():
            ctr = ctr + 1
            time.sleep(1)
            print(ctr, '-', team)

        time.sleep(1.5)
        break

    # Inputting teams
    if re.match('[Nn][Oo]', yn):
        print('\nYou have chosen not to import team names.')
        time.sleep(1)
        print('Type "done" when you are done entering team names.\n')
        time.sleep(1)

        while True:
            team = input('Enter team ' + str(len(teams) + 1) + ': ')

            # Handles exit
            exitfunc(team)

            # When user types done
            if re.match('[Dd][Oo][Nn][Ee]', team):
                print('\nStep 1 is finished!')
                time.sleep(1)
                print('\nYou have inputted', len(teams), 'teams into the tournament.')
                time.sleep(1.5)

                print('\nHere are your inputted teams:\n')
                ctr = 0
                for team in teams.keys():
                    ctr = ctr + 1
                    time.sleep(1)
                    print(ctr, '-', team)

                time.sleep(1.5)


                while True:
                    yn = input('\nWould you like to input more teams?\n> ')
                    time.sleep(0.5)
                    exitfunc(yn)
                    if re.match('^[Yy][Ee][Ss]', yn) or re.search('^[Nn][Oo]', yn):
                        print('\n')
                        break
                    else:
                        print('\nPlease input yes/no.')
                        time.sleep(0.5)
                        continue

                if re.match('[Yy][Ee][Ss]', yn):
                    continue
                elif len(teams) == 0:
                    print('You have inputted zero teams. Please try again.')
                    time.sleep(1)
                    print("Otherwise, you may type 'exit' to exit the program.\n")
                    time.sleep(1)
                    continue
                elif len(teams) == 1:
                    print('Picker done!')
                    time.sleep(1)
                    print('Scores:')

                    for team in teams.items():
                        # HERE GOES THE DEFINITION

                elif re.match('[Nn][Oo]', yn):
                    break

            # [W, L]
            teams[team] = [0, 0, 0]

        break
    else:
        print('\nPlease type yes/no.')
        time.sleep(0.5)
        continue

# STEP 1.5: Determining BYE
if len(teams) % 2 == 1:
    print('Step 1.5: Determining BYE')
    time.sleep(1)
    print('\nYou have inputted an odd number of teams.')
    time.sleep(1.5)
    print('To have even matchups, please pick the team')
    time.sleep(1.5)
    print('that gets to automatically advance to the second round.')
    time.sleep(1.5)
    team = input('\nEnter team: ')

    exitfunc(team)

elif len(teams) % 2 == 0:
    pass
