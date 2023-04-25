function plotAudioWaveFormWithTranscription(transcriptionStack)

% Get the time, text and audio data from the collected
% transcriptionStack.
timeStack =  [transcriptionStack.time];
textStack =  [transcriptionStack.text];
audioStack = {transcriptionStack.audio};

% Get the audio packet size and define tStart to help with plotting the 
% audio data for the time intervals.
audioSize = numel(transcriptionStack(1).audio);
tStart = 0;

for i = 1:numel(timeStack)
    t = linspace(tStart, time(i), audioSize);
    tStart = time(i);
    plot(t, audioStack{i}, 'Color', [0 0.4470 0.7410]);
    text(timeStack(i), 0.5, textStack(i), 'FontSize', 10);
    hold on;
end

xlabel('Time');
ylabel('Audio Signal with transcription');

end