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