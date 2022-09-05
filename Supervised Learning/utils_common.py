from pathlib import Path


def fetch_file(file, data_dir="data"):
    """
    Fetch a file that was previously downloaded into the data folder. 
    
    file: the file in which to fetch
    data_dir: (default="data") the location to fetch the data
    
    return: The pathlib.Path object representing the file.
    """
    data_dir = Path(data_dir)
    data_dir.mkdir(exist_ok = True)
    file_path = data_dir / Path(file)

    return file_path

def num_lines_in_file(file):
    """
    Gets the number of lines in a file.
    
    file: the file
    
    return: The number of lines in a file.
    """
    with open(file, 'r') as f:
        num_lines = sum(1 for l in f)
        
    return num_lines

def print_file_contents(file, num_lines=20):
    """
    Prints the file contents.
    
    file: The file.
    num_lines: (default=20) The number of lines in the file to print.
    """
    print(f'{file} ===========================')
    
    with open(file,'r') as f:
        for i in range(num_lines):
            print(f'{i}\t{repr(f.readline())}')