import ffmpeg_streaming
from ffmpeg_streaming import Formats

if __name__ == '__main__':
    video = ffmpeg_streaming.input('Front/videos/1.mp4')
    dash = video.dash(Formats.h264())
    dash.auto_generate_representations()
    dash.output('Front/local_dash/1/manifest.mpd')

    video = ffmpeg_streaming.input('Front/videos/2.mp4')
    dash = video.dash(Formats.h264())
    dash.auto_generate_representations()
    dash.output('Front/local_dash/2/manifest.mpd')
