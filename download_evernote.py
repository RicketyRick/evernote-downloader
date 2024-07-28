import os
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.notestore.NoteStore as NoteStore
import evernote.edam.type.ttypes as Types
import evernote.edam.error.ttypes as Errors
from evernote.api.client import EvernoteClient

# Replace with your Evernote developer token
DEV_TOKEN = 'your_developer_token'

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def download_attachments(note, note_store, path):
    resources = note.resources
    if resources:
        for resource in resources:
            data = resource.data.body
            file_name = resource.attributes.fileName
            with open(os.path.join(path, file_name), 'wb') as f:
                f.write(data)

def save_note_content(note, path):
    note_path = os.path.join(path, f"{note.title}.html")
    with open(note_path, 'w', encoding='utf-8') as f:
        f.write(note.content)

def fetch_notes(notebook_guid, note_store, path):
    filter = NoteStore.NoteFilter()
    filter.notebookGuid = notebook_guid
    spec = NoteStore.NotesMetadataResultSpec(includeTitle=True)

    offset = 0
    page_size = 50
    while True:
        note_list = note_store.findNotesMetadata(filter, offset, page_size, spec)
        for note_meta in note_list.notes:
            note = note_store.getNote(note_meta.guid, True, True, False, False)
            note_path = os.path.join(path, note.title)
            create_directory(note_path)
            save_note_content(note, note_path)
            download_attachments(note, note_store, note_path)
        offset += len(note_list.notes)
        if offset >= note_list.totalNotes:
            break

def fetch_notebooks(client):
    note_store = client.get_note_store()
    notebooks = note_store.listNotebooks()
    for notebook in notebooks:
        notebook_path = os.path.join('Evernote_Backup', notebook.name)
        create_directory(notebook_path)
        fetch_notes(notebook.guid, note_store, notebook_path)

def main():
    client = EvernoteClient(token=DEV_TOKEN, sandbox=False)
    user_store = client.get_user_store()
    version_ok = user_store.checkVersion("Evernote EDAMTest (Python)",
                                         UserStoreConstants.EDAM_VERSION_MAJOR,
                                         UserStoreConstants.EDAM_VERSION_MINOR)
    if not version_ok:
        print("Evernote API version not up to date.")
        return

    create_directory('Evernote_Backup')
    fetch_notebooks(client)

if __name__ == "__main__":
    main()
