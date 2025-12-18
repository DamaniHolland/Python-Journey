
'''

8-7. Album: Write a function called make_album() that builds a dictionary 
describing a music album . The function should take in an artist name and an 
album title, and it should return a dictionary containing these two pieces of 
information . Use the function to make three dictionaries representing different 
albums . Print each return value to show that the dictionaries are storing the 
album information correctly .Add an optional parameter to make_album() that allows you to store the 
number of tracks on an album . If the calling line includes a value for the num-
ber of tracks, add that value to the album’s dictionary . Make at least one new 
function call that includes the number of tracks on an album.

'''
def make_album(artist_name, album_name):
    album = {'artist_name': artist_name, 'album_name': album_name}
    return album

get_on_the_floor = make_album('michael jackson', 'get on the floor')
print(get_on_the_floor)

six = make_album('oli howe', 'six')
print(six)

good_morning = make_album('pj morton, susan carol', 'good morning')
print(good_morning)

def make_album_w_tracks(artist_name, album_name, track_qty=''):
    album = {'artist_name': artist_name, 'album_name': album_name,}
    if track_qty:
        album['track_qty'] = track_qty
    
    return album

six = make_album_w_tracks('oli howe', 'six', track_qty = 9)
print(six)

good_morning = make_album_w_tracks('pj morton, susan carol', 'good morning')
print(good_morning)