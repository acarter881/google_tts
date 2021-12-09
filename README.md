# google_tts

Using Google's [Cloud Text-to-Speech API](https://cloud.google.com/text-to-speech)

## Table of Contents
- [FAQ](#faq)
- [Sample Output](#sample-output)
- [More Information](#more-information)

## FAQ
1. What is this API?
> Google Cloud Text-to-Speech enables developers to synthesize natural-sounding speech with 100+ voices, available in multiple languages and variants. It applies DeepMind’s groundbreaking research in WaveNet and Google’s powerful neural networks to deliver the highest fidelity possible. As an easy-to-use API, you can create lifelike interactions with your users, across many applications and devices.
2. Does the API cost money to use?
- Please reference [this link](https://cloud.google.com/text-to-speech/pricing)
3. What voices can I choose from?
- Please reference [this link](https://cloud.google.com/text-to-speech/docs/voices)
4. Can I use Speech Synthesis Markup Language (SSML)?
- Yes, please reference [this link](https://cloud.google.com/text-to-speech/docs/ssml) and see the example code below
```javascript
<speak>
  Here are <say-as interpret-as="characters">SSML</say-as> samples.
  I can pause <break time="3s"/>.
  I can play a sound
  <audio src="https://www.example.com/MY_MP3_FILE.mp3">didn't get your MP3 audio file</audio>.
  I can speak in cardinals. Your number is <say-as interpret-as="cardinal">10</say-as>.
  Or I can speak in ordinals. You are <say-as interpret-as="ordinal">10</say-as> in line.
  Or I can even speak in digits. The digits for ten are <say-as interpret-as="characters">10</say-as>.
  I can also substitute phrases, like the <sub alias="World Wide Web Consortium">W3C</sub>.
  Finally, I can speak a paragraph with two sentences.
  <p><s>This is sentence one.</s><s>This is sentence two.</s></p>
</speak>
```
5. Can I get a custom voice? 
- Yes, there is a [Custom Voice program](https://cloud.google.com/text-to-speech/custom-voice/docs) (beta)

## Sample Output
- [Audio File (Ogg)](https://drive.google.com/file/d/1n-rVE0bfroPKlDv8hPpJWgl4pGurU_wV/view?usp=sharing)

## More Information
- [Source Code](https://github.com/googleapis/python-texttospeech)
- [Setup](https://cloud.google.com/text-to-speech/docs/libraries)
