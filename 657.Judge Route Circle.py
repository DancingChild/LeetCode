"""
Initially, there is a Robot at position (0, 0). Given a sequence of
its moves, judge if this robot makes a circle, which means it moves
 back to the original place.

The move sequence is represented by a string. And each move is
 represent by a character. The valid robot moves are R (Right),
 L (Left), U (Up) and D (down). The output should be true or false
 representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
"""


class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        SYMBOLS = {'U': 'D', 'R': 'L', 'D': 'U', 'L': 'R'}
        # SYMBOLS_V, SYMBOLS_K = SYMBOLS.values(), SYMBOLS.keys()
        arr = []
        for c in moves:
            if SYMBOLS[c] in arr:
                arr.remove(SYMBOLS[c])
            else:
                arr.append(c)

        return not arr