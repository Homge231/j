import tkinter as tk  # Import the tkinter library with an alias 'tk' for ease of use
import font_manager as fonts  # Import the font_manager module for font management
import video_library as lib  # Import the video_library module for accessing video information

class UpdateVideoList:
    def __init__(self, window):
        self.window = window  # Store the Tkinter window object passed as an argument

        self.window.geometry("470x240")  # Set the dimensions of the window
        self.window.title("Update Videos")  # Set the title of the window

        fonts.configure()  # Call the configure function from the font_manager module to configure fonts

        self.video_number_label = tk.Label(self.window, text="Enter Video Number:")  # Create a label widget
        self.video_number_label.grid(row=0, column=0, padx=10, pady=10)  # Place the label in the window

        self.video_number_entry = tk.Entry(self.window)  # Create an entry widget for inputting video numbers
        self.video_number_entry.grid(row=0, column=1, padx=10, pady=10)  # Place the entry widget in the window

        self.new_rating_label = tk.Label(self.window, text="Enter New Rating:")  # Create a label widget
        self.new_rating_label.grid(row=1, column=0, padx=10, pady=10)  # Place the label in the window

        self.new_rating_entry = tk.Entry(self.window)  # Create an entry widget for inputting new ratings
        self.new_rating_entry.grid(row=1, column=1, padx=10, pady=10)  # Place the entry widget in the window

        self.update_rating_btn = tk.Button(self.window, text="Update Rating", command=self.update_video_rating)
        # Create a button widget to update video ratings
        self.update_rating_btn.grid(row=2, column=0, columnspan=2, padx=10, pady=10)  # Place the button in the window

        self.result_text = tk.Label(self.window, text="", font=("Helvetica", 10))
        # Create a label widget to display the result
        self.result_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)  # Place the label in the window

    def update_video_rating(self):
        video_number = self.video_number_entry.get()  # Get the video number entered by the user
        new_rating = self.new_rating_entry.get()  # Get the new rating entered by the user
        name = lib.get_name(video_number)  # Get the name of the video from the video_library module
        if name is not None:  # Check if the video name is found
            play_count = lib.get_play_count(video_number)  # Get the play count of the video
            lib.set_rating(video_number, new_rating)  # Set the new rating for the video
            self.result_text.config(text=f"Video: {name}\nNew Rating: {new_rating}\nPlay Count: {play_count}")
            # Display the result with video name, new rating, and play count
        else:
            self.result_text.config(text=f"Video {video_number} not found \n Please enter the video number")
            # Display a message if the video is not found

if __name__ == "__main__":
    window = tk.Tk()  # Create a Tkinter window
    update_video_list = UpdateVideoList(window)
    # Create an instance of the UpdateVideoList class with the Tkinter window
    window.mainloop()  # Run the Tkinter event loop to display the window and handle events
