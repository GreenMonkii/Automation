import os, sys
from pytube import Playlist, YouTube
from rich import print
from rich.prompt import Prompt


def download_audio(video_url, output_dir):
    try:
        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Download the audio
        video = YouTube(video_url)
        audio_stream = video.streams.get_audio_only()
        audio_stream.download(output_path=output_dir, filename=f"{video.title}.mp3")
        print("Audio downloaded successfully!")
    except Exception as e:
        print(f"Error downloading audio: {str(e)}")


def download_playlist_audio(playlist_url, output_dir):
    try:
        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Download the playlist
        playlist = Playlist(playlist_url)
        for video in playlist.videos:
            try:
                output_file_path = os.path.join(output_dir, f"{video.title}.mp3")
                if not os.path.isfile(output_file_path):
                    audio_stream = video.streams.get_audio_only()
                    audio_stream.download(
                        output_path=output_dir, filename=f"{video.title}.mp3"
                    )
            except Exception as e:
                print(f"Error downloading audio - {video.title}")
                is_continue = Prompt.ask("Do you want to continue downloading? (y/n)")
                if is_continue.lower() != "y":
                    break
                continue
        print("Playlist audios downloaded successfully!")
    except Exception as e:
        print(f"Error downloading playlist audios: {str(e)}")


if __name__ == "__main__":
    try:
        # Prompt the user for mode, video URL, and output directory
        mode = Prompt.ask("Enter mode", choices=["audio", "playlist"], default="audio")
        url = Prompt.ask("Enter video URL:")

        if not url.strip():
            print("URL cannot be empty.")
            sys.exit(1)

        output_dir = Prompt.ask(
            "Enter output directory:", default="~\\Downloads\\Youtube Audios"
        )
        output_dir = os.path.expanduser(output_dir)

        if mode == "audio":
            download_audio(url, output_dir)
        elif mode == "playlist":
            download_playlist_audio(url, output_dir)
        else:
            print("Invalid mode. Please choose 'audio' or 'playlist'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
