line_count = 0
lines = 0
word = ( )
character_count = 0
f = open('sample_a5.py','r')
for line in f:
    line_count = line_count + 1
    print line_count,'-',line
print 'line count',':',line_count
print 'character_count',':',character_count
f.close()

#I was unable to figure out how to do the character count for this.
#I would really appreciate if you could show me how once you read
# and grade my work. Thank you!