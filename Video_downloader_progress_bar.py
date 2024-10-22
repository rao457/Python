from pytube import YouTube
from tqdm import tqdm

# Initialize progress bar as a global variable
progress_bar = None

# Function to display progress bar
def progress_function(stream, chunk, bytes_remaining):
    global progress_bar
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    if progress_bar is None:
        # Initialize progress bar once we know the file size
        progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc=stream.title)
    progress_bar.update(len(chunk))

# URL of the YouTube video to be downloaded
video_url = 'https://youtu.be/GOiDf1wSMts'

# Create a YouTube object
yt = YouTube(video_url, on_progress_callback=progress_function)

# Get the highest resolution stream
stream = yt.streams.get_highest_resolution()

# Download the video
stream.download()

# Close the progress bar
if progress_bar is not None:
    progress_bar.close()

print("Download Complete!")
