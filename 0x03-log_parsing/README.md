0x03-log_parsing

Steps:
- Iterate over a sys.stdin object, line by line.
- Use regex to check line format
- Strip the line, and store the resulting array
- Store possible values for status codes in a sorted array/dictionary
- Iterate over 10 elements at a row, aggregating the filesize, and counting occurences of    status codes. Check for sigterm, if encountered, print the aggregated lines, reset file size, reset status code occurences