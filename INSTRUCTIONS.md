# Audio Kit Examples

This document provides examples of how to use each utility in the Audio Kit repository.

## > render_xmls.py

Convert MusicXML files to WAV audio using MuseScore.

### Single File Conversion

```bash
# Convert a single MusicXML file to WAV
python render_xmls.py path/to/score.xml output/directory/
```

### Batch Conversion

```bash
# Convert all XML files in a directory
python render_xmls.py path/to/xml/directory/ output/directory/
```

### Using in Python Code

```python
from render_xmls import render_xmls

# Convert a single file
render_xmls("path/to/score.xml", "output/directory/")

# Convert all files in a directory
render_xmls("path/to/xml/directory/", "output/directory/")
```

### Notes

- Files that have already been rendered will be skipped
- Progress is shown with dots (.) for each file processed
- The output directory will be created if it doesn't exist

## > create_playlist.py

Create a playlist while listening to songs. The songs skipped are moved from the original directory to skipped_songs directory (in the root folder level)

```bash
# Create a playlist
python create_playlist.py path/to/audio_directory/
```