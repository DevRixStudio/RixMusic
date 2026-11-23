from rixmusic_errors import PermissionDenied

class PermissionManager:
    """In-memory owner/admin permissions, keyed by chat and user IDs."""
    def __init__(self, owners=None):
        self.owners = {str(x) for x in (owners or [])}
        self.admins = {}

    def add_owner(self, user_id):
        self.owners.add(str(user_id))

    def is_owner(self, user_id):
        return str(user_id) in self.owners

    def add_admin(self, chat_id, user_id):
        self.admins.setdefault(str(chat_id), set()).add(str(user_id))

    def remove_admin(self, chat_id, user_id):
        admins = self.admins.get(str(chat_id), set())
        uid = str(user_id)
        if uid in admins:
            admins.remove(uid)
            return True
        return False

    def is_admin(self, chat_id, user_id):
        uid = str(user_id)
        return self.is_owner(uid) or uid in self.admins.get(str(chat_id), set())

    def require_admin(self, chat_id, user_id):
        if not self.is_admin(chat_id, user_id):
            raise PermissionDenied("This action requires chat admin/owner permission.")
