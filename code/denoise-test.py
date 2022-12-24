from IPython import display as disp
import torch
import torchaudio

from denoiser import pretrained
from denoiser.dsp import convert_audio


model = pretrained.dns64()
wav, sr = torchaudio.load('WOL_vs_ARS_2022-11-12.mp3')
wav = convert_audio(wav, sr, model.sample_rate, model.chin)
with torch.no_grad():
    denoised = model(wav[None])[0]
disp.display(disp.Audio(wav.data.cpu().numpy(), rate=model.sample_rate))
disp.display(disp.Audio(denoised.data.cpu().numpy(), rate=model.sample_rate))