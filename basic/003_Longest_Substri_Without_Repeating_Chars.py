class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # dictionary for the characters and their index
        d = {}
        # start index of current substring
        start = 0
        # maximum length
        max_len = 0
        for i in range(len(s)):
            # whether current substring would have repeating characters
            if s[i] in d.keys() and d[s[i]] >= start:
                # if the length of current string is larger than maximum length
                this_len = i - start
                if this_len > max_len:
                    max_len = this_len
                # update the start index
                start = d[s[i]] + 1
                d[s[i]] = i
            else:
                # update the dictionary
                d[s[i]] = i
        this_len = len(s) - start
        if this_len > max_len:
            max_len = this_len

        return max_len

    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        # maximum length and current string
        max_len = 0
        cur_str = ''
        for i in s:
            # add the char to current string
            if i not in cur_str:
                cur_str += i
            else:
                # if there are repeating chars
                if len(cur_str) > max_len:
                    max_len = len(cur_str)
                i_idx = cur_str.index(i)
                cur_str = cur_str[i_idx+1 : ] + i
        if len(cur_str) > max_len:
            max_len = len(cur_str)
        return max_len
    '''