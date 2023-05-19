import argparse
from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata(img_path, log_file=None):
    image = Image.open(img_path)
    exifdata = image._getexif()

    if exifdata is not None:
        for tag_id in exifdata:
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            
            if isinstance(data, bytes):
                data = data.decode(errors='ignore')

            info = f"{tag:25}: {data}"

            if log_file:
                with open(log_file, 'a') as f:
                    f.write(info + "\n")
            else:
                print(info)
    else:
        print("No metadata found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract image metadata.')
    parser.add_argument('img_path', type=str, help='The path of the image file.')
    parser.add_argument('-log', type=str, help='Optional log file to output data.')
    args = parser.parse_args()
    extract_metadata(args.img_path, args.log)
