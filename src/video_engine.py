from moviepy.editor import (
    ImageClip,
    AudioFileClip,
    CompositeAudioClip,
    CompositeVideoClip,
    TextClip
)
import os

# Optional TTS (Coqui)
try:
    from TTS.api import TTS
    TTS_AVAILABLE = True
except:
    TTS_AVAILABLE = False


def apply_motion(clip, motion_style, duration):
    """
    Apply motion effects to image clip
    """
    if motion_style == "zoom":
        return clip.resize(lambda t: 1 + 0.05 * t)

    elif motion_style == "pan":
        return clip.set_position(lambda t: ('center', int(-50 * t)))

    elif motion_style == "fade":
        return clip.fadein(1).fadeout(1)

    return clip


def generate_tts(chant_text, output_path="temp_tts.wav"):
    """
    Generate speech audio using Coqui TTS
    """
    if not TTS_AVAILABLE or not chant_text:
        return None

    try:
        tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")
        tts.tts_to_file(text=chant_text, file_path=output_path)
        return output_path
    except Exception as e:
        print(f"TTS failed: {e}")
        return None


def generate_video(
    image_path,
    output_path,
    duration=5,
    fps=24,
    motion_style="zoom",
    music_path=None,
    chant_text=None
):
    """
    Generate short video creative from image
    """

    # Create base clip
    clip = ImageClip(image_path).set_duration(duration)

    # Apply motion
    clip = apply_motion(clip, motion_style, duration)

    audio_tracks = []

    # Add background music
    if music_path and os.path.exists(music_path):
        music = AudioFileClip(music_path).subclip(0, duration)
        audio_tracks.append(music)

    # Add TTS chant
    if chant_text:
        tts_file = generate_tts(chant_text)
        if tts_file and os.path.exists(tts_file):
            chant_audio = AudioFileClip(tts_file).set_start(duration - 2)
            audio_tracks.append(chant_audio)

    # Combine audio
    if audio_tracks:
        final_audio = CompositeAudioClip(audio_tracks)
        clip = clip.set_audio(final_audio)

    # Add optional text overlay
    if chant_text:
        txt = TextClip(
            chant_text,
            fontsize=60,
            color="white"
        ).set_duration(2).set_position(("center", "bottom"))

        clip = CompositeVideoClip([clip, txt.set_start(duration - 2)])

    # Export video
    clip.write_videofile(
        output_path,
        fps=fps,
        codec="libx264",
        audio_codec="aac"
    )

    print(f"Video saved -> {output_path}")