from pexif import JpegFile
import sys

usage = """Usage: dump_timestamp.py filename.jpg"""

# if len(sys.argv) != 2:
#     print >> sys.stderr, usage
#     sys.exit(1)

# try:
#     ef = JpegFile.fromFile(sys.argv[1])
#     primary = ef.get_exif().get_primary()
#     print "Primary DateTime          :", primary.DateTime
#     print "Extended DateTimeOriginal :", primary.ExtendedEXIF.DateTimeOriginal
#     print "Extended DateTimeDigitized:", primary.ExtendedEXIF.DateTimeDigitized
# except IOError:
#     type, value, traceback = sys.exc_info()
#     print >> sys.stderr, "Error opening file:", value
# except JpegFile.InvalidFile:
#     type, value, traceback = sys.exc_info()
#     print >> sys.stderr, "Error opening file:", value


FILE_NAME ='WechatIMG2080.jpeg' 
TIME = '2019:01:21 12:17:36'
dsc_pic = JpegFile.fromFile(FILE_NAME)
# dsc_pic.exif.primary.DateTime = src_pic.exif.primary.DateTime
# dsc_pic.exif.primary.ExtendedEXIF.DateTimeOriginal = src_pic.exif.primary.ExtendedEXIF.DateTimeOriginal
# dsc_pic.exif.primary.ExtendedEXIF.DateTimeDigitized = src_pic.exif.primary.ExtendedEXIF.DateTimeDigitized

# dt =src_pic.exif.primary.DateTime 
# dto = src_pic.exif.primary.ExtendedEXIF.DateTimeOriginal
# dtd = src_pic.exif.primary.ExtendedEXIF.DateTimeDigitized

dsc_pic.exif.primary.DateTime = TIME 
dsc_pic.exif.primary.ExtendedEXIF.DateTimeOriginal = TIME
dsc_pic.exif.primary.ExtendedEXIF.DateTimeDigitized = TIME


dsc_pic.writeFile(FILE_NAME)