import dropbox

def retrieve_member_list(dbx, recursive=True, debug=False):

    all_members = []
    members = dbx.team_members_list()
    all_members.extend(members.members)
    if debug: 
        for member in members.members:
            print("\ndebug: {}".format(member.profile.email))

    if recursive:
        while members.has_more:
            print("..retrieving another 1000 users")
            #dropbox.dropbox.Dropbox.team_members_list_continue()
            members = dbx.team_members_list_continue(members.cursor)
            all_members.extend(members.members)
            if debug:
                for member in members.members:
                    print("\ndebug: {}".format(member.profile.email))

    return all_members


def dropbox_listing(dbx, user_id, path):

    listing = []

    try:
        dir_listing = dbx.as_user(user_id).files_list_folder(path)

        #fix paging... must go past 1000...

        for item in dir_listing.entries:
            
            if type(item) == dropbox.files.FileMetadata: 
                listing.append("f, " + item.path_display)

            if type(item) == dropbox.files.FolderMetadata: 
                listing.append("F, " + item.path_display)

                dropbox_listing(dbx, user_id, item.path_display)

    except:     
        if path == "":
            path = "{folder root}"
        
        print("[!] failure in dropbox_listing on {} for {}".format(path, user_id))

    return listing

