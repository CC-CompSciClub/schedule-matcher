
song_request = []

# Add to queue
print("Welcome to DJ Pythonic's Song Request Manager! ")
print("Enter the song title to make a song request.")
print("To exit, enter Quit.")
#Ask user for song
song = input("Enter a song title: ") 

while song != "Quit":
  song = input("Enter a song title: ")
  song_request.append(song)
  print("The song", song, "has been added to the list. ")
 # print(song_request)
  song = input("Enter a song title: ")
else :

 print("Thank you for your requests. Enjoy the show!")