# Audio Kit Examples

This document provides examples of how to use each utility in the Audio Kit repository.

## render_xmls.py

Convert MusicXML files to WAV audio using MuseScore.

### Single File Conversion

```bash
# Convert a single MusicXML file to WAV
python render\_xmls.py path/to/score.xml output/directory/
```

### Batch Conversion

```bash
# Convert all XML files in a directory
python render\_xmls.py path/to/xml/directory/ output/directory/
```

### Using in Python Code

```python
from render\_xmls import render\_xmls

# Convert a single file
render\_xmls("path/to/score.xml", "output/directory/")

# Convert all files in a directory
render\_xmls("path/to/xml/directory/", "output/directory/")
```

### Notes

- Files that have already been rendered will be skipped
- Progress is shown with dots (.) for each file processed
- The output directory will be created if it doesn't exist

## create_playlist.py

Create a playlist while listening to songs.

### Single File Conversion

```bash
# Create a playlist
python create\_playlist.py path/to/audio\_directory/
```