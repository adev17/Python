list = ['Holiday Project'', ''Fine Art Project'', ''Wedding Project']
entry = 'Y'
N = ' '
Y = ' '
continuing = ''
print '------------------------------------------------------'
print 'Welcome to Art Inspirations, a place where you can get instructions '
print '               to create art projects!'
print '------------------------------------------------------'
print 'Currently, we have these projects available:'
print list
print '                                 '
number = raw_input ('Would you like to do a project? (Y/N): ')
print '                                 '
while number == 'Y' :
    print 'Lets get artsy!'
    entry = raw_input('What project would you like to do? (see list above): ')
    if (entry == 'Holiday Project'):
        print 'Lets make a Jingle Bell Wreath Ornament!'
        print '                                 '
        print '1. Take one red chenille pipe cleaner and thread on alternating Silver and Gold bells.'
        print '   Push the bells so they are in the middle with even amounts of chenille pipe cleaner on both sides.'
        print '2. Now, twist the chenille pipe cleaner ends together to form a circle.'
        print '3. Thread some ribbon through the wreath and tie a knot in the ends to make a hanger.'
        print '                                 '
    elif (entry == 'Fine Art Project'):
        print 'Lets make a Sharpie Marker Decorated Planter'
        print '1. Paint your pot with acrylic paint and let dry completely.'
        print '2. Plan out some simple hand-drawn designs using dots, slanted lines, & triangles.'
        print '3. Draw your customized designs on the planters with various Sharpie markers. Match bold black'
        print '   with bright, eye-popping brilliant markers for dramatic contrast. Go crazy!'
        print '   Plant your succulents with potting soil and water.'
        print '                           '
    else:
        print 'Lets make a White Bridal Bouquet'
        print '1. Begin with your bush of peonies and then add small bundles of roses. Arrange'
        print '   them into a round, symmetrical shape.'
        print '2. Wrap florat wire tightly around the stems.'
        print '3. Next, use your floral cutters to trim the stems evenly'
        print '4. Finally, cover the wire with floral tape.'
        print '                           '
    print '                           '
    continuing = raw_input('Would you like another art project? (Y/N): ')
    if continuing == 'N':
        break
print("Have a crafty day!")