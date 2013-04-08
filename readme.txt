Castle Doctrine Map Tools

- convert_maps.py can be used to read recording file maps and output into various formats, such as used by http://castlefortify.com/.
- extract_recording_maps.py finds all maps in recording files.

For example, it is possible to convert all maps in a recording file using the command:

 > extract_recording_maps.py -f recordedGame00047.txt | convert_maps.py -o cf
