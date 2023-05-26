import yt_dlp

def download_video(url):
    ydl_opts = {
        'outtmpl': '%(uploader)s/%(title)s-%(id)s.%(ext)s',  # Create a directory for each uploader
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_channel(url):
    ydl_opts = {
        'outtmpl': '%(uploader)s/%(title)s-%(id)s.%(ext)s',  # Create a directory for each uploader
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    print("What would you like to do?")
    print("A) Download a specific video")
    print("B) Download a full channel's content or a playlist")
    choice = input("Choose an option (A or B): ")
    if choice.lower() == 'a':
        video_url = input("Enter the video URL: ")
        download_video(video_url)
    elif choice.lower() == 'b':
        channel_url = input("Enter the channel URL or playlist URL: ")
        download_channel(channel_url)
    else:
        print("Invalid option. Please choose either A or B.")

if __name__ == "__main__":
    main()
