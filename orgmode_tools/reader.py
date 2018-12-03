import re


class Ledger():

    def __init__(self, fname,
                 dateFormat=r'(\d{4})\/(\d{2})\/(\d{2})'):
        
        dateFormatUncaptured = dateFormat.replace('(', '').replace(')', '')
        self._transactions = []
        
        LEDGER_FORMAT_REGEX = \
            r'{}(.*)\n+((^(?!{}).*\n)+)+'.format(
                dateFormat,
                dateFormatUncaptured
            )
        TRANSACTION_FORMAT_REGEX = \
            r'\s*((\S\s{0,1})+)\s*\$*(-*\d+.*\d+)*\n+'
        
        try:
            with open(fname, 'r') as f:
                transactions = re.findall(
                    LEDGER_FORMAT_REGEX, f.read(), re.MULTILINE)
                
                for t in transactions:
                    if(len(t) < 5):
                        raise Exception('Transaction entry invalid.')
                    
                    date = {
                        'y': t[0],
                        'm': t[1],
                        'd': t[2]
                    }
                    name = t[3]
                    entries = [
                        {'account': r[0].strip('\n').strip(' '),
                         'amount': r[2]}
                        for r in re.findall(TRANSACTION_FORMAT_REGEX, t[4])]
                    self._transactions.append(
                        Transaction(date, name, entries)
                    )
                    
        except FileNotFoundError:
            raise Exception(
                'The journal file {} was not found.'.format(
                    fname
                )
            )

        for t in self._transactions:
            print(t)
            print()

            
class Transaction():

    def __init__(self, date, name, entries):
        self.date = date
        self.name = name
        self.entries = entries

    def __str__(self):
        changesSummary = ('; ').join(
            ['the account {} had a change of {}'.format(
                e['account'], e['amount']) for e in self.entries])
        return 'On {}/{}/{}, {}'.format(self.date['d'],
                                        self.date['m'],
                                        self.date['y'],
                                        changesSummary)
        
Ledger('/Users/mammam/Documents/ledger/journal.ledger')

