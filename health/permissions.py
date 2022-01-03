
class BelongsToGroup():
    """
    Checks if the user belongs to the group of editors and / or administrators as list, if not ReadOnly
    """
    def list_group(self, user):
        group = list(user.groups.values_list('name', flat=True))
        if len(group) == 0:
            group = ['ReadOnly']
        return group