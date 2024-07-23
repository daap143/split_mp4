from moviepy.editor import VideoFileClip
import jason

def split_video(video_file, manifest_file):
    with open(manifest_file, 'r') as f:
        manifest = json.load(f)

    clip = VideoFileClip(video_file)
    for chunk in manifest:
        start_time = chunk['start_time']
        end_time = chunk['end_time']
        chunk_clip = clip.subclip(start_time, end_time)
        chunk_clip.write_videofile(f"chunk_{start_time}_{end_time}.mp4")


split_video('input.mp4', 'manifest.json')
