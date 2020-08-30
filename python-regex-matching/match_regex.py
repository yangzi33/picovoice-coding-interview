# Matching regex
class Solve:
    def match_regex(self, s: str, p: str) -> bool:
        if not p:
            return not s

        # Check first occurence of string
        # Base case for recursive algorithm
        first_check = not not s and (s[0] == p[0] or p[0] == '.')
        
        # if not first:
        #     return False
        
        # Recursion if length of pattern >= 2
        if len(p) > 1:
            # Check Kleene Star
            if p[1] == '*':
                # perform recursion till 'first' is false
                return (first_check and self.match_regex(s[1:], p)) or self.match_regex(s, p[2:])  
        return self.match_regex(s[1:], p[1:]) and first_check


if __name__ == '__main__':
    # sample test
    solve = Solve()
    print(solve.match_regex('abc', 'a*.c*'))