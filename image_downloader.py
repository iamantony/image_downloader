import os
import re
import urllib

# Need parser that searches txt file for addresses beginning with http://i.groupme.com/

group_id = "transcript-5815609.txt"
transcript = open(group_id)
for line in transcript:
    pass
#    # Do string processing here
#    #if 'http://i.groupme.com/' in 
#    #re.search(pattern, string, flags=0)
#    match = re.search('http://i.groupme.com/', line, flags=0)
#    if match:
#        process(match)
    
#transcript.close()

#handlers= {"p": # p tag handler
#           "h1": # h1 tag handler
#          }

## ... in the loop
#    if lyne.rstrip() in handlers :  # strip to remove trailing whitespace
#       # close current handler?
#        # start new handler?
#    else :
        # pass string to current handler



image_id = 'e3f9d0c0ac520130022766900689df55'
url = 'http://i.groupme.com/' + image_id
image = urllib.URLopener()
script_directory = os.path.dirname(os.path.abspath(__file__))

# Checks if new image directory already exists, creates it if it doesn't
if not os.path.exists(script_directory + '/images/'):
    os.makedirs(script_directory + '/images/')

image.retrieve(url, script_directory + '/images/' + image_id + '.jpg')


