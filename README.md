# PrimeCenter

## Overview

PrimeCenter is a Python program designed to speed up file transfers and optimize disk space usage on Windows computers. It efficiently manages the transfer of files from a source directory to a destination directory, while also removing large files from the source to optimize disk usage.

## Features

- **File Transfer**: Copies files from a specified source directory to a destination directory.
- **Disk Space Optimization**: Deletes large files in the source directory that exceed a specified size threshold.

## Requirements

- Python 3.x
- Windows Operating System

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/primecenter.git
   ```
2. Navigate to the project directory:
   ```bash
   cd primecenter
   ```

## Usage

1. Open the `prime_center.py` file and modify the `source_dir` and `destination_dir` variables to point to your desired directories.
2. Run the program:
   ```bash
   python prime_center.py
   ```

## Configuration

- **File Size Threshold**: By default, files larger than 100 MB are considered for deletion. You can change this threshold in the `optimize_disk_space` method.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any changes.

## Contact

For any questions or issues, please open an issue on GitHub or contact me at your-email@example.com.