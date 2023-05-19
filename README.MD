# File Metadata Extractor

This Python script allows you to extract metadata from different types of files including images, PDFs, Word documents, and audio files.


## Usage

To use the script, you can either directly call the Python file with your target file as an argument, or specify an optional log file to write the metadata to:

```
python metadata.py target.jpg
```

or with a log file:

```
python metadata.py target.jpg -log output.log
```


## Supported File Types

The script currently supports the following file types:

- Images (JPEG, PNG, etc.)
- PDFs
- Word Documents (.docx)
- Audio Files (MP3, MP4)