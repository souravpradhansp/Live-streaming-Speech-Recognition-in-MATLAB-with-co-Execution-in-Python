# This code is used in the 'speechToText_streaming_from_audio_device.mlx' and 'speechToText_streaming_from_audio_file.mlx' example
# Copyright 2023 The MathWorks, Inc.

import torch
import torchaudio

class SpeechRecognizer():
    def __init__(self):
        super(SpeechRecognizer, self).__init__()
        bundle = torchaudio.pipelines.EMFORMER_RNNT_BASE_LIBRISPEECH
        self.streaming_feature_extractor = bundle.get_streaming_feature_extractor()
        self.decoder = bundle.get_decoder()
        self.token_processor = bundle.get_token_processor()
        self.beam_width = 10
        self.state = None
        self.hypothesis = None

    def streamingInfer(self, segment: torch.Tensor):
        segment = torch.Tensor(segment)
        features, length = self.streaming_feature_extractor(segment)
        hypos, self.state = self.decoder.infer(
            features, length, self.beam_width, state=self.state, hypothesis=self.hypothesis
            )
        self.hypothesis = hypos[0]
        transcript = self.token_processor(self.hypothesis[0], lstrip=False)
        return transcript

    def nonStreamingInfer(self, segment: torch.Tensor):
        segment = torch.Tensor(segment)
        with torch.no_grad():
            features, length = self.non_streaming_feature_extractor(segment)
            hypotheses = self.decoder(features, length, 10)
        transcript = self.token_processor(hypotheses[0][0])
        return transcript
