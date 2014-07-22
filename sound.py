from pydub import AudioSegment

address = "static/sound/ing1.wav"

sentence = AudioSegment.from_wav(address)

# shorten: 
# save first 0.5 secs
#sentence = sentence[:500]

# save last 0.5 secs
sentence = sentence[500:]

sentence.export(address, format="wav")