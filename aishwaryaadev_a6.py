# Assignment 6
# This program asks the user to enter a state in the US
# (CA, IL, NY)
# and it will look up the most famous food in that state. The user is then
# asked if they would like to see the best cities and restaurants that serve that specific dish.
state = ' '
# CA Dishes
ca_dishes = ['Burrito', 'Avocado toast', 'California sushi roll']

# CA dishes- cities to try in
burrito_mode1 = ['San Diego', 'Santa barbara']
avocado_toast_mode1 = ['Redding', 'Eureka']
sushi_roll_mode1 = ['Palm Springs', 'Los Angeles']

ca_dishes_mode1 = {'Burrito': burrito_mode1, 'Avocado toast': avocado_toast_mode1,
                   'California sushi roll': sushi_roll_mode1}

# IL Dishes
il_dishes = ['Cheese curds', 'Butter cake', 'Deep dish pizza']

# IL dishes-cities to try in
curds_mode1 = ['Rockford', 'Aurora']
cake_mode1 = ['Naperville', 'Elgin']
deep_pizza_mode1 = ['Chicago', 'Oak Park']

il_dishes_mode1 = {'Cheese curds': curds_mode1, 'Butter cake': cake_mode1,
                   'Deep dish pizza': deep_pizza_mode1}
# NY Dishes
ny_dishes = ['Thin crust pizza', 'Fish fry', 'Lobster roll']

# NY dishes-cities to try in
thin_pizza_mode1 = ['NYC', 'Manhattan']
fish_mode1 = ['Brooklyn', 'Albany']
lobster_mode1 = ['Buffalo', 'Bronx']

ny_dishes_mode1 = {'Thin crust pizza': thin_pizza_mode1, 'Fish fry': fish_mode1,
                   'Lobster roll': lobster_mode1}

# combining states and cities in one directory
state_dict = {'California': ca_dishes, 'IL': il_dishes, 'NY': ny_dishes}
dishes_dict = {'CA': ca_dishes_mode1, 'IL': il_dishes_mode1, 'NY': ny_dishes_mode1}

print '------------------------------------------------------'
print 'Welcome to Food and Travel Inspirations, a place where you can get information on the best'
print '            food to try and in which city, based on the state you choose'
print '------------------------------------------------------'
print 'Currently, we have food information for these states available:'
def myfirstfunction(states):
    for x in states:
        print (x)
places = ['California', 'Illinois', 'New York']
myfirstfunction(places)
print '                                 '
number = raw_input('Would you like to look up a US states best food? (Y/N): ')
print '                                 '
while number == 'Y':
    print 'Lets go eat!'
    state = raw_input('What US state would you like? (see list above): ')
    def mysecondfunction(string):
        response = 'You selected: ' + string + ', great choice!'
        return response
    print mysecondfunction(state)
    print ('These are the best foods to try in ' + state)
    if (state == 'California'):
        def mythirdfunction(dishes):
            for y in dishes:
                print (y)
        foods = ca_dishes
        mythirdfunction(foods)
        citiestosee = raw_input('Would you like to see which cities are best to try these foods in California? (Y/N): ')
        if citiestosee == 'N':
            print 'No problem, enjoy eating!'
        else:
            print ca_dishes_mode1
    elif (state == 'Illinois'):
        def myfourthfunction(ildishes):
            for z in ildishes:
                print (z)
        ilfoods = il_dishes
        myfourthfunction(ilfoods)
        citiestoseeil = raw_input('Would you like to see which cities are best to try these foods in Illinois? (Y/N): ')
        if citiestoseeil == 'N':
            print 'No problem, enjoy eating!'
        else:
            print il_dishes_mode1
    else:
        def myfifthfunction(nydishes):
            for f in nydishes:
                print (f)
        nyfoods = ny_dishes
        myfifthfunction(nyfoods)
        citiestoseeny = raw_input('Would you like to see which cities are best to try these foods in New York? (Y/N): ')
        if citiestoseeny == 'N':
            print 'No problem, enjoy eating!'
        else:
            print ny_dishes_mode1
    print '                           '
    continuing = raw_input('Would you like to check out another US States food? (Y/N): ')
    if continuing == 'N':
        break
print("Stay hungry!")


