import paddlehub as hub

module = hub.Module(name="wav2lip")

def inference(img, audio):
    module.wav2lip_transfer(face=img, audio=audio, output_dir='', use_gpu=True)
    return "result.mp4"

inference('monatest.jpeg', 'game.wav')