import gradio as gr
import librosa
import soundfile as sf

def lofi_effect(audio_filepath):
    try:
        y, sr = librosa.load(audio_filepath, sr=None)

        # Slow down the audio to 80%
        y_slow_down = librosa.effects.time_stretch(y, rate=0.8)

        # Shift the pitch lower by 5 semitones
        y_pitch_shift = librosa.effects.pitch_shift(y_slow_down, sr=sr, n_steps=-5)

        # Save the modified audio to a temporary file
        output_path = "modified_audio.wav"
        sf.write(output_path, y_pitch_shift, sr)

        return output_path
    except Exception as e:
        print(f"Error processing audio: {e}")
        return "Error"

# Define the Gradio interface
iface = gr.Interface(
    fn=lofi_effect, 
    inputs=gr.Audio(type="filepath", label="Upload a .wav file"),
    outputs=gr.Audio(label="Processed Lofi Audio"),
    live=False
)

# Launch the interface
iface.launch(share=True)
