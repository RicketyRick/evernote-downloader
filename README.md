# Evernote Downloader

This script downloads all notes and notebooks from Evernote, handles pagination, and downloads all attachments. It creates directories that represent the structure stored in Evernote.

## Prerequisites

- Python 3.x
- Evernote Developer Token
- Evernote SDK for Python (`evernote3`)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/RicketyRick/evernote-downloader.git
   cd evernote-downloader
   ```

2. **Install Dependencies**

   Install the required Python package using pip:

   ```bash
   pip install evernote3
   ```

## Usage

1. **Obtain Evernote Developer Token**

   To use the Evernote API, you need a developer token. You can obtain it from the [Evernote Developer Website](https://dev.evernote.com/doc/articles/dev_tokens.php).

2. **Configure the Script**

   Open the script file `download_evernote.py` and replace `your_developer_token` with your actual Evernote developer token:

   ```python
   DEV_TOKEN = 'your_developer_token'
   ```

3. **Run the Script**

   Execute the script using Python:

   ```bash
   python evernote_backup.py
   ```

4. **Backup Structure**

   The script will create a directory called `Evernote_Backup` in the current working directory. Inside this directory, it will create subdirectories for each notebook. Each note will have its own subdirectory containing an HTML file for the note content and any attachments.

## Script Details

### Functions

- **create_directory(path)**
  - Creates a directory if it does not already exist.
  
- **download_attachments(note, note_store, path)**
  - Downloads all attachments for a note and saves them in the specified path.
  
- **save_note_content(note, path)**
  - Saves the content of a note as an HTML file in the specified path.
  
- **fetch_notes(notebook_guid, note_store, path)**
  - Fetches all notes for a given notebook, handling pagination, and saves their content and attachments.
  
- **fetch_notebooks(client)**
  - Fetches all notebooks and initiates the download process for each notebook.

### Main Function

The `main()` function initializes the Evernote client, checks the API version, creates the backup directory, and starts the process of fetching notebooks and notes.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the Apache 2.0 License. See the LICENSE file for details.

## Contact

For any questions or support, please open an issue on the GitHub repository.
