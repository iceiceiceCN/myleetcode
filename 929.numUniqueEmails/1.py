class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        seed = set()
        for email in emails:
            local, domain = email.split('@')
            if "+" in local:
                local = local[:local.index('+')]
            local = local.replace('.','')
            email = local +'@' + domain
            seed.add(email)
        
        return len(seed)

if __name__ == "__main__":
    a = Solution()
    b = a.numUniqueEmails(["test.email+alex@leetcode.com","test.email.leet+alex@code.com"])