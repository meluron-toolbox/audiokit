# Audio Kit Examples

This document provides examples of how to use each utility in the Audio Kit repository.

## renderXMLs.py

Convert MusicXML files to WAV audio using MuseScore.

### Single File Conversion

```bash
# Convert a single MusicXML file to WAV
python renderXMLs.py path/to/score.xml output/directory/
```

### Batch Conversion

```bash
# Convert all XML files in a directory
python renderXMLs.py path/to/xml/directory/ output/directory/
```

### Using in Python Code

```python
from renderXMLs import renderXMLs

# Convert a single file
renderXMLs("path/to/score.xml", "output/directory/")

# Convert all files in a directory
renderXMLs("path/to/xml/directory/", "output/directory/")
```

### Notes

- Files that have already been rendered will be skipped
- Progress is shown with dots (.) for each file processed
- The output directory will be created if it doesn't exist