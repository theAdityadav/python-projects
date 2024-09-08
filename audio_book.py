import pygame
import os

class AudiobookPlayer:
    def __init__(self, audiobook_file):
        self.audiobook_file = audiobook_file
        pygame.init()
        pygame.mixer.init()

    def play(self):
        pygame.mixer.music.load(self.audiobook_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()

def main():
    audiobook_file = input("Enter the path to the audiobook file: ")
    player = AudiobookPlayer(audiobook_file)
    while True:
        print("1. Play")
        print("2. Pause")
        print("3. Unpause")
        print("4. Stop")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            player.play()
        elif choice == "2":
            player.pause()
        elif choice == "3":
            player.unpause()
        elif choice == "4":
            player.stop()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()