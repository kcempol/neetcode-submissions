class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {};
        for i in range(len(s)):
            seen[s[i]] = seen.get(s[i], 0 ) + 1;
        for i in range(len(t)):
            seen[t[i]] = seen.get(t[i], 0) - 1;
        
        
        return all(count == 0 for count in seen.values())
        