from obsidiantools.api import Vault

def main():
    # Initialize vault with task assist data directory
    vault = Vault("task-assist-vault")
    
    # Connect to build indices
    vault.connect()
    
    # Find notes with project tag
    tag = "project"
    print(f"\nNotes with #{tag} tag:")
    for note_path, tags in vault.tags_index.items():
        if tag in tags:
            print(f"\n- {note_path}")
            # Get backlinks for this note
            backlinks = vault.get_backlinks(note_path)
            if backlinks:
                print("  Backlinks:")
                for backlink in backlinks:
                    print(f"  - {backlink}")
            else:
                print("  No backlinks found")

if __name__ == "__main__":
    main()
