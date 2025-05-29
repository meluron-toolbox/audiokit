"""
Author: Ankit Anand
Created on: 04/12/24
"""

from pathlib import Path
import subprocess
import sys
import argparse

MUSESCORE_LOC = "/Applications/MuseScore 4.app/Contents/MacOS/mscore" # Modify as per the location of Musescore on your machine

if not Path(MUSESCORE_LOC).exists():
    sys.exit(f"{MUSESCORE_LOC} DNE, please update the MuseScore location in the python file!")

def render_xmls(refXMLPath:str, outputDp:str):
    """
    To render XML(s) into .wav audio.

    Args
    ----
    refXMLPath: str
        Path to either an XML file or a folder containing .xml files
    outputDp: str
        Directory path to save the rendered audio (The name of the rendered audio will be same as that of the XML)
    
    Returns
    -------
    0: Successful Execution
    
    Note
    ----
    Incase the output directory contains the rendered audio of an XML (same name as the XML), we do not re-render it.
    """
    
    # Convert the str path to Path object for better functionality
    refXMLPath = Path(refXMLPath)
    if not refXMLPath.exists():
        sys.exit("Reference File/Directory does not exist, please try again!")
    
    outputDp = Path(outputDp)
    outputDp.mkdir(parents=True, exist_ok=True) # Create the output dir if it does not exist
    
    # Ignore re-rendering
    alreadyRenderedXMLs = [file.stem for file in outputDp.iterdir() if file.suffix == ".wav"]
    
    if refXMLPath.is_dir():
        for xmlFp in refXMLPath.rglob("*.xml"): # Look for each of the .xml files
            if xmlFp.stem in alreadyRenderedXMLs: # Go to the next iteration if the file has already been rendered
                continue
            audioFn = xmlFp.stem + ".wav" # Audio file name same as xml
            audioFp = outputDp/audioFn # Audio file path
            command = [
                MUSESCORE_LOC,
                "--export-to",
                str(audioFp),
                str(xmlFp)
            ]
            print(".", end="", flush=True)
            subprocess.run(command, stderr=subprocess.DEVNULL)
    elif refXMLPath.is_file():
        audioFn = refXMLPath.stem + ".wav" # Audio file name same as xml
        audioFp = outputDp/audioFn # Audio file path
        command = [
            MUSESCORE_LOC,
            "--export-to",
            str(audioFp),
            str(refXMLPath)
        ]
        print(".", end="", flush=True)
        subprocess.run(command, stderr=subprocess.DEVNULL)

# =================================================================
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert MusicXML files to WAV using MuseScore")
    parser.add_argument("xmlpath", help="Path to XML file or directory containing XML files")
    parser.add_argument("outputpath", help="Directory to save output WAV files")
    args = parser.parse_args()
    
    render_xmls(args.xmlpath, args.outputpath)