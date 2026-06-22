class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
         hashset_s = {}
         hashset_t = {}
         if len(s) != len(t):
            return False

         for i in range(len(s)):
            hashset_s[s[i]] = hashset_s.get(s[i], 0) + 1
            hashset_t[t[i]] = hashset_t.get(t[i], 0) + 1
         return hashset_s == hashset_t