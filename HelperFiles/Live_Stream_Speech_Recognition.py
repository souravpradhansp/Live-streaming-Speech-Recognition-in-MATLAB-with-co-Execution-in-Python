# This code is used in the 'speechToText_streaming.mlx' example
# Copyright 2023 The MathWorks, Inc.

import torch
import torchaudio

class SpeechRecognizer():
    
    def __init__(self):
        super(SpeechRecognizer, self).__init__()
        bundle = torchaudio.pipelines.EMFORMER_RNNT_BASE_LIBRISPEECH
        self.bundle = bundle
        self.streaming_feature_extractor = bundle.get_streaming_feature_extractor()
        self.decoder = bundle.get_decoder()
        self.token_processor = bundle.get_token_processor()
    
        self.beam_width = 10
    
        self.state = None
        self.hypothesis = None

        self.segment_length = self.bundle.segment_length * self.bundle.hop_length
        self.context_length = self.bundle.right_context_length * self.bundle.hop_length
        self.context = torch.zeros([self.context_length])

    def cacher(self, chunk: torch.Tensor):
        chunk = torch.Tensor(chunk)

        if chunk.size(0) < self.segment_length:
            chunk = torch.nn.functional.pad(chunk, (0, self.segment_length - chunk.size(0)))
        chunk_with_context = torch.cat((self.context, chunk))
        self.context = chunk[-self.context_length :]
        return chunk_with_context

    def streamingInfer(self, chunk: torch.Tensor) -> str:
        segment = self.cacher(chunk)
        features, length = self.streaming_feature_extractor(segment)
        hypos, self.state = self.decoder.infer(
            features, length, self.beam_width, state=self.state, hypothesis=self.hypothesis
            )
        self.hypothesis = hypos[0]
        transcript = self.token_processor(self.hypothesis[0], lstrip=False)
        return transcript