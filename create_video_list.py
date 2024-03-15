import tkinter as tk  # Import tkinter library with an alias 'tk' for ease of use
import tkinter.scrolledtext as tkst  # Import scrolledtext module from tkinter for scrolled text widget
import font_manager as fonts  # Import font_manager module for font management
import video_library as lib  # Import video_library module for accessing video information

class CreateVideoList:
    def __init__(self, window):
        self.list_txt = []  # Initialize an empty list for temporary text storage
        self.window = window  # Store the Tkinter window object passed as an argument
        self.playlist = []  # Initialize an empty list for storing video playlist

        self.window.geometry("600x350")  # Set the dimensions of the window
        self.window.title("Create Video List")  # Set the title of the window

        fonts.configure()  # Call the configure function from the font_manager module to configure fonts

        self.video_number_label = tk.Label(self.window, text="Enter Video Number:")  # Create a label widget
        self.video_number_label.grid(row=0, column=0, padx=10, pady=10)  # Place the label in the window

        self.video_number_entry = tk.Entry(self.window)  # Create an entry widget for inputting video numbers
        self.video_number_entry.grid(row=0, column=1, padx=10, pady=10)  # Place the entry widget in the window

        self.add_to_playlist_btn = tk.Button(self.window, text="Add to Playlist", command=self.add_to_playlist)
        # Create a button widget to add videos to the playlist
        self.add_to_playlist_btn.grid(row=0, column=2, padx=10, pady=10)
        # Place the button in the window

        self.playlist_text = tkst.ScrolledText(self.window, width=40, height=10, wrap="word")
        # Create a scrolled text widget to display the playlist
        self.playlist_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        # Place the scrolled text widget in the window

        self.play_playlist_btn = tk.Button(self.window, text="Play Playlist", command=self.play_playlist)
        # Create a button widget to play the playlist
        self.play_playlist_btn.grid(row=2, column=0, padx=10, pady=10)  # Place the button in the window

        self.reset_playlist_btn = tk.Button(self.window, text="Reset Playlist", command=self.delete_playlist)
        # Create a button widget to reset the playlist
        self.reset_playlist_btn.grid(row=2, column=2, padx=10, pady=10)  # Place the button in the window

    def add_to_playlist(self):
        video_number = self.video_number_entry.get()  # Get the video number entered by the user
        name = lib.get_name(video_number)  # Get the name of the video from the video_library module
        director = lib.get_director(video_number)  # Get the director of the video from the video_library module
        if name is not None:  # Check if the video name is found
            self.playlist.append(name)  # Add the video name to the playlist
            self.playlist_text.insert(tk.END,f"{name} - {director} \n" )
            # Display the video name and director in the playlist
        else:
            self.playlist_text.insert(tk.END, f"Video {video_number} not found\n")
            # Display a message if the video is not found

    def play_playlist(self):
        for video_name in self.playlist:
            print(f"playing:{video_name}")  # Print each video name in the playlist to simulate playing

    def delete_playlist(self):
        self.playlist = []  # Reset the playlist by clearing the list
        self.playlist_text.delete("1.0", tk.END)  # Clear the playlist displayed in the scrolled text widget

if __name__ == "__main__":  # Check if this script is being run directly
    window = tk.Tk()  # Create a Tkinter window
    create_video_list = CreateVideoList(window) # Create an instance of the CreateVideoList class with the Tkinter window
    window.mainloop()  # Run the Tkinter event loop to display the window and handle events