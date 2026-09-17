class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()
        for email in emails:
            [localname, domain] = email.split('@')
            localname = localname.split('+')[0]
            localname = localname.replace(".", "")
            uniqueEmails.add(localname + '@' + domain)

        return len(uniqueEmails)
                