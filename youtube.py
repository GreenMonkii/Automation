import os
import sys
from pytube import Playlist, YouTube

def download_video(video_url, output_dir):
    try:
        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Download the video
        video = YouTube(video_url)
        video.streams.get_highest_resolution().download(output_path=output_dir)
    except Exception as e:
        print(f"Error downloading video: {str(e)}")


def download_playlist(playlist_url, output_dir):
    try:
        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Download the playlist
        playlist = Playlist(playlist_url)
        for video in playlist.videos:
            video.streams.get_highest_resolution().download(output_path=output_dir)
    except Exception as e:
        print(f"Error downloading playlist: {str(e)}")


if __name__ == "__main__":
    try:
        # Check if the required command-line arguments are provided
        if len(sys.argv) < 3:
            print("Usage: python test.py <mode> <url> <output_dir>")
            sys.exit(1)

        mode = sys.argv[1]
        url = sys.argv[2]
        output_dir = sys.argv[3] if len(sys.argv) == 4 else "./Downloads/Youtube Videos"

        if mode == "video":
            download_video(url, output_dir)
        elif mode == "playlist":
            download_playlist(url, output_dir)
        else:
            print("Invalid mode. Please choose 'video' or 'playlist'.")
            sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
