import magic

def validate_file_extension(file):
  valid_extension = "text/plain"
  file_extension = magic.from_buffer(file.read(1024), mime=True).lower()

  return file_extension.endswith(valid_extension)