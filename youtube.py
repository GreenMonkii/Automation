import os, sys
from pytube import Playlist, YouTube
from rich import print
from rich.prompt import Prompt


def download_video(video_url, output_dir):
    try:
        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Download the video
        video = YouTube(video_url)
        video.streams.get_highest_resolution().download(output_path=output_dir)
        print("Video downloaded successfully!")
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
        print("Playlist downloaded successfully!")
    except Exception as e:
        print(f"Error downloading playlist: {str(e)}")


if __name__ == "__main__":
    try:
        # Prompt the user for mode, video URL, and output directory
        mode = Prompt.ask("Enter mode", choices=["video", "playlist"], default="video")
        url = Prompt.ask("Enter video URL:")

        if not url.strip():
            print("URL cannot be empty.")
            sys.exit(1)

        output_dir = Prompt.ask(
            "Enter output directory:", default="./Downloads/Youtube Videos"
        )

        if mode == "video":
            download_video(url, output_dir)
        elif mode == "playlist":
            download_playlist(url, output_dir)
        else:
            print("Invalid mode. Please choose 'video' or 'playlist'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
