class Solution:
    def isPalindrome(self, s: str) -> bool:        
        alpha_num_str = "".join([char for char in s if char.isalnum()])
		
        if alpha_num_str.lower() == "".join([char for char in reversed(alpha_num_str.lower())]):
            return True
        else:
            return False