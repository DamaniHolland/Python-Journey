###############################################################################
#   Damani Holland
#   12/14/2025
#   CS Python
###############################################################################

'''

8-8. User Albums: Start with your program from Exercise 8-7 . Write a while 
loop that allows users to enter an album’s artist and title . Once you have that 
information, call make_album() with the user’s input and print the dictionary 
that’s created . Be sure to include a quit value in the while loop.

'''

def make_album(artist, title, tracks=''):
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album
        
while True:
    print("\nPlease enter the album name and artist to create an album.")
    print("enter 'q' anytime to quit ")
        
    artist_name = input("\nEnter artist name: ")
    if artist_name == 'q':
        break
    title_name = input("\nEnter title of album: ")
    if title_name == 'q':
        break
    tracks = input("\nDo you want to enter number of tracks? ")
    if tracks == 'no':
        continue
    elif tracks == 'q':
        break
    else:
        tracks = input("How many tracks are there? ")
    album = make_album(artist_name, title_name, tracks)
    print(album)