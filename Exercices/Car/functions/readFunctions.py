def read_file_without_header(file_path):
    """
    Reads a file, skips the header, and returns a list of lines in the form of tuples.
    Each tuple contains the values from a line split by commas.
    """
    result = []
    with open(file_path, 'r') as file:
        # Skip the header
        next(file)
        # Process each line
        for line in file:
            # Strip whitespace and split by commas
            values = line.strip().split(',')
            result.append(tuple(values))
    return result