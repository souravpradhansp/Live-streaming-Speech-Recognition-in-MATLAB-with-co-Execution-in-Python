# Live-streaming-Speech-Recognition-in-MATLAB-with-co-Execution-in-Python
This repo shows how to use Emformer RNN-T and audio streaming API in MATLAB to perform speech-to-text transcription in real time.
![speech2text image](https://github.com/souravpradhansp/Live-streaming-Speech-Recognition-in-MATLAB-with-co-Execution-in-Python/blob/main/images/helloworld.png?raw=true)

**Creator**: MathWorks Development

## Requirements
- [MATLAB&reg;](http://www.mathworks.com) R2017a or later
- [Audio Toolbox&trade;](https://www.mathworks.com/products/audio.html)
- [Python 3.9;](https://www.python.org/downloads/release/python-390/)

## Get Started
Download or clone this repositiory to your machine and open it in MATLAB&reg;. Download [Python 3.9;](https://www.python.org/downloads/release/python-390/) and make it the default version of the Python interpreter in MATLAB using the instructions mentioned on this page. 

After that, on the MATLAB Command Line Interface, execute the following commands to install the required Python libraries:

``!python pip install torch==1.13.0``

``!python pip install torchaudio==0.13.0``

``!python pip install sentencepiece==0.1.97``


Run ``speechToText_streaming.mlx`` to perform speech-to-text conversion on streaming audio input.

## Workflow Details
**1. Overview**
Performing speech-to-text transcription in real time is composed of the following steps:
- Build the inference pipeline Emformer RNN-T is composed of three components: feature extractor, decoder and token processor. This is implemented in the streamingInfer method of the Live_Stream_Speech_Recognition.py file.
- Format the waveform into chunks of expected cached inputs. This is implemented in the cacher method of the Live_Stream_Speech_Recognition.py file.
- Pass data through the pipeline.
