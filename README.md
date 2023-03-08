# Live-streaming-Speech-Recognition-in-MATLAB-with-co-Execution-in-Python
This repo shows how to use Emformer RNN-T and audio streaming API in MATLAB to perform speech-to-text transcription in real time.
![speech2text image](https://github.com/souravpradhansp/Live-streaming-Speech-Recognition-in-MATLAB-with-co-Execution-in-Python/blob/main/images/helloworld.png?raw=true)

**Creator**: MathWorks Development

## Requirements
- [MATLAB&reg;](http://www.mathworks.com) R2017a or later
- [Audio Toolbox&trade;](https://www.mathworks.com/products/audio.html)
- [Python 3.9](https://www.python.org/downloads/release/python-390/)

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

**2. Construct the Pipeline**

Pre-trained model weights and related pipeline components are bundled as [torchaudio.pipelines.RNNTBundle](https://pytorch.org/audio/stable/generated/torchaudio.pipelines.RNNTBundle.html#torchaudio.pipelines.RNNTBundle).

We use [torchaudio.pipelines.EMFORMER_RNNT_BASE_LIBRISPEECH](https://pytorch.org/audio/stable/generated/torchaudio.pipelines.EMFORMER_RNNT_BASE_LIBRISPEECH.html#torchaudio.pipelines.EMFORMER_RNNT_BASE_LIBRISPEECH), which is a Emformer RNN-T model trained on LibriSpeech dataset.

Streaming inference works on input data with overlap. Emformer RNN-T model treats the newest portion of the input data as the “right context” — a preview of future context. In each inference call, the model expects the main segment to start from this right context from the previous inference call. The following figure illustrates this:

