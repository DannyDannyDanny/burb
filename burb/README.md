# Burb

Audio processing backend for burb. Feature engineering for audio labeling.

### Audio In

The core of burb is reading an audio file, and extracting information from it. This could be:

* [Audio features](https://devopedia.org/audio-feature-extraction)
* Recording meta data: (samplerate, samples, track length, is_stereo, bitrate)
* For music especially:
    * Release Meta Data (title, artist, album, release_year)
    * Musical information (genre, energy level, tempo, musical key)
A python script checks the upload folder for new files.

### Testing
```
docker-compose up python
```