class Node:
    def __init__(self, songId):
        self.songId = songId
        self.prev = None
        self.next = None

class MusicPlayer:
    def __init__(self):
        self.head = None
        self.currentSong = None

    # Function to add a song to the end of the list
    def addSong(self, songId):
        # Complete this function
        current = self.head
        node=Node(songId)

        if current is None:
            self.head = node
            self.head.next = self.head
            self.head.prev = self.head
            self.currentSong = node

        else:
            if songId != self.head.songId:
                isSongFound = False
                while current.next != self.head:
                    if current.next.songId == songId:
                        isSongFound = True
                        break
                    current = current.next
                if not isSongFound:
                    current.next = node
                    node.prev = current
                    node.next = self.head
                    self.head.prev = node
                   


    # Function to play the next song
    def playNext(self):
        # Complete this function
        self.currentSong = self.currentSong.next

    # Function to play the previous song
    def playPrev(self):
        # Complete this function
        self.currentSong = self.currentSong.prev

    # Function to switch to a specific song
    def switchSong(self, songId):
        # Complete this function
        current = self.head
        if current.songId == songId:
            self.currentSong = current
        else:
            current=current.next
        while current != self.head:
            if current.songId == songId:
                self.currentSong = current
                break
            current = current.next
        

    # Function to return the songId of the current song playing
    def current(self):
        # Complete this function
        return self.currentSong.songId

    def __str__(self):
        arr=[]
        current = self.head
        arr.append(current.songId)
        while current.next != self.head:
            arr.append(current.next.songId)
            current = current.next

        return str(arr)

# Main function to test the music player
# if __name__ == "__main__":
#     player = MusicPlayer()
#     queries = int(input())
#     while queries > 0:
#         line = input().split()
#         query = int(line[0])

#         if query == 1:
#             songId = int(line[1])
#             player.addSong(songId)
#         elif query == 2:
#             player.playNext()
#         elif query == 3:
#             player.playPrev()
#         elif query == 4:
#             songId = int(line[1])
#             player.switchSong(songId)
#         elif query == 5:
#             print(player.current())
#         else:
#             print("Invalid query!")
#         queries -= 1

sol=MusicPlayer()
sol.addSong(1)
sol.addSong(2)
sol.addSong(3)

print(sol.current())
sol.playNext()#1-2
print(sol.current())
sol.playPrev()#2-1
print(sol.current())
sol.addSong(4)
sol.addSong(5)
sol.playNext()#1-2
sol.playNext()#2-3
sol.switchSong(1)#3-1
print(sol.current())
sol.playNext()#2-3
print(sol.current())