def rename_mp3_files(location):
    import os
    import eyed3

    for root, dirs, files in os.walk(location):
        for m_file in files:
            if m_file.endswith('.mp3'):
                old_filepath = os.path.join(root, m_file)
                id3info = eyed3.load(old_filepath)

                new_filename = '{}.mp3'.format(id3info.tag.artist.replace("/", ", ") + ' - ' +  id3info.tag.title.replace("/", ", "))
                new_filepath = os.path.join(root, new_filename)

                os.rename(old_filepath, new_filepath)

                print (new_filename)