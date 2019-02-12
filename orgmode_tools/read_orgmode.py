import re


class OrgmodeInfo(object):

    def __init__(self, emacs_file):
        
        self._agenda_files = [
            name for name in
            self._get_org_data('org-agenda-files', emacs_file).split('"')
            if name.strip(' ').strip('(') != 'list' and
            len(name.strip(' ').strip('(').strip(')')) > 0]

        self._todo_keywords = [
            word for word in
            self._get_org_data('org-todo-keywords', emacs_file).split(
                'sequence')[1].split('"')
            if len(word.strip(' ')) > 0 and
            len(word.replace('(', '').replace(')', '')) > 0]

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


