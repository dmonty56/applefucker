"""
welcome to applefucker v1.1!
released 03-27-2022
written by David Montgomery

no there's no executable, run this through your favorite IDE
this took a solid 30 seconds to run through my 3k songs so be patient with it.

read the README!
"""

from mutagen.easyid3 import EasyID3
import os

directory = r"C:\Users\Owner\Music"    # directory containing music, replace with your own
t = 0   # iterators to count how many operations happened
d = 0
da = 0
for root, dirs, files in os.walk(directory):    # os fuckery to move through subfolders
    for filename in files:
        f = os.path.join(root, filename)
        if f.endswith('.mp3'):  # only check mp3 files
            tags = EasyID3(f)
            if '/' in tags['tracknumber'][0]:   # changes [tracknumber]/[totaltracks] to [tracknumber]
                num = tags['tracknumber'][0].split('/')
                tr = num[0]
                if tr[0] == '0':    # checks if any track number starts with a 0 and fixes that
                    final = tr[1:]
                else:
                    final = tr
                tags['tracknumber'] = final
                tags.save()
                t += 1
            if 'discnumber' in tags.keys(): # checks if there's a discnumber tag at all
                if tags['discnumber'][0] == '1/1':  # removes discnumber tag for anything labeled 1/1
                    tags['discnumber'] = ''
                    tags.save()
                    d += 1
                elif '/' in tags['discnumber'][0]:  # changes [discnumber]/[totaldiscs] to [discnumber]
                    num = tags['discnumber'][0].split('/')
                    tags['discnumber'] = num[0]
                    tags.save()
                    d += 1
            if 'date' in tags.keys():   # checks if theres a date tag at all because some tracks are really that fucked
                if len(tags['date'][0]) > 4:    # changes date format from YYYY-MM-DD hh:mm to YYYY
                    k = tags['date'][0]
                    tags['date'] = k[0:4]
                    tags.save()
                    da += 1
print(t, " track numbers fixed!\n", 
d, " disc numbers fixed!\n", 
da, " dates fixed!")