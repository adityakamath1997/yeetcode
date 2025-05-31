class Solution(object):
    def findWords(self, words):
        first,second,third="qwertyuiop","asdfghjkl","zxcvbnm"
        m={}
        ans=[]
        for char in first:
            m[char]=1
        for char in second:
            m[char]=2
        for char in third:
            m[char]=3

        for word in words:
            new_word=word.lower()
            first_char=new_word[0]
            check=m[first_char]

            if all(m[ch]==check for ch in new_word):
                ans.append(word)
        return ans





        

        

        