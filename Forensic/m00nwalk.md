# Objetivo
Decode this [message](https://jupiter.challenges.picoctf.org/static/14393e18d98fedbaedbc28896d7ef31a/message.wav) from the moon.
# Solución
```
┌──(kalicura㉿rufian)-[~/SeguridadRedes/Forensic]
└─$ strings message.wav | grep pico
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~/SeguridadRedes/Forensic]
└─$ hexeditor message.wav 
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~/SeguridadRedes/Forensic]
└─$ exiftool message.wav               
ExifTool Version Number         : 12.70
File Name                       : message.wav
Directory                       : .
File Size                       : 11 MB
File Modification Date/Time     : 2020:10:26 13:30:20-05:00
File Access Date/Time           : 2024:03:13 13:12:57-05:00
File Inode Change Date/Time     : 2024:03:13 13:11:01-05:00
File Permissions                : -rw-r--r--
File Type                       : WAV
File Type Extension             : wav
MIME Type                       : audio/x-wav
Encoding                        : Microsoft PCM
Num Channels                    : 1
Sample Rate                     : 48000
Avg Bytes Per Sec               : 96000
Bits Per Sample                 : 16
Duration                        : 0:01:55
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~/SeguridadRedes/Forensic]
└─$ python setup.py install                            
python: can't open file '/home/kalicura/SeguridadRedes/Forensic/setup.py': [Errno 2] No such file or directory
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~/SeguridadRedes/Forensic]
└─$ sstv                                               
usage: sstv [-h] [-d AUDIO_FILE] [-o OUTPUT_FILE] [-s SKIP] [-V] [--list-modes] [--list-audio-formats] [--list-image-formats]

options:
  -h, --help            show this help message and exit
  -d AUDIO_FILE, --decode AUDIO_FILE
                        decode SSTV audio file
  -o OUTPUT_FILE, --output OUTPUT_FILE
                        save output image to custom location
  -s SKIP, --skip SKIP  time in seconds to start decoding signal at
  -V, --version         show program's version number and exit
  --list-modes          list supported SSTV modes
  --list-audio-formats  list supported audio file formats
  --list-image-formats  list supported image file formats

examples:
  Decode local SSTV audio file named 'audio.ogg' to 'result.png':
    $ sstv -d audio.ogg

  Decode SSTV audio file in /tmp to './image.jpg':
    $ sstv -d /tmp/signal.wav -o ./image.jpg

  Start decoding SSTV signal at 50.5 seconds into the audio
    $ sstv -d audio.ogg -s 50.50
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~/SeguridadRedes/Forensic]
└─$ sstv -d message.wav -o ./image.jpg
[sstv] Searching for calibration header... Found!    
[sstv] Detected SSTV mode Scottie 1
[sstv] Decoding image...                                   [####################################################################################################] 100%
[sstv] Drawing image data...
[sstv] ...Done!
```
# Notas
- Se usa una herramienta necesaria (sstv) para decodificar un archivo en .wav a .jpg, el cuál contiene la bandera que buscamos
- picoCTF{beep_boop_im_in_space}
# Referencia