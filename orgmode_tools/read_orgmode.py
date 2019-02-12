import re


class OrgmodeInfo(object):

    def __init__(self, emacs_file):

        self._agenda_files = [
            name for name in re.findall(
                r'\s*\"(.+?\.org)\"',
                self._get_org_data('org-agenda-files', emacs_file)
            )]

        self._todo_keywords = [
            word for word in re.findall(
                r'.+?\s*\"(.+?(?=\"))',
                self._get_org_data('org-todo-keywords', emacs_file)
            )]

        self._tag_names = [
            {'name': tag_info[0], 'id': tag_info[1]}
            for tag_info in re.findall(
                    r'\(\s*\"@(.+?(?=\"))\"\s*\.\s*\?(\w)\)',
                    self._get_org_data('org-tag-alist', emacs_file)
            )]

    def _get_org_data(self, option, emacs_file):
        data_start = list(re.finditer(option, emacs_file))[0].start()

        while emacs_file[data_start] != '(':
            data_start += 1

        paren_count = 0

        data_end = data_start

        while True:
            if emacs_file[data_end] == '(':
                paren_count += 1
            elif emacs_file[data_end] == ')':
                paren_count -= 1
            data_end += 1
            if paren_count == 0:
                break
        return emacs_file[data_start:data_end]


