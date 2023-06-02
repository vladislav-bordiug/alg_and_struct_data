from collections import deque
class Solution:
    def remove(self, board: str, i: int) -> str:
        if i == len(board):
            return board
        j = i
        while j < len(board)-1 and board[i] == board[j+1]:
            j += 1
        length = j-i + 1
        if length >= 3:
            board = self.remove(board[:i] + board[j+1:],0)
        else:
            board = self.remove(board,i+1)
        return board
    def findMinStep(self, board: str, hand: str) -> int:
        queue = deque([(board,hand)])
        visited = set()
        visited.add((board,hand))
        res = 1
        while True:
            queue2 = deque()
            while queue:
                board, hand = queue.popleft()
                for i in range(len(board)):
                    for j in range(len(hand)):
                        if j > 0 and hand[j] == hand[j-1]:
                            continue
                        if i > 0 and board[i-1] == hand[j]:
                            continue
                        if board[i] == hand[j] or (i > 0 and board[i] == board[i-1] and board[i] != hand[j]):
                            nboard = self.remove(board[:i] + hand[j] + board[i:],0)
                            if not nboard:
                                return res
                            nhand = hand[:j] + hand[j+1:]
                            if (nboard,nhand) in visited:
                                continue
                            else:
                                queue2.append((nboard,nhand))
                                visited.add((nboard,nhand))
            if len(queue2) == 0:
                break
            queue = queue2
            res += 1
        return -1
s = Solution()
board = input('Enter board\n')
hand = input('Enter hand\n')
print('Result:',s.findMinStep(board,hand))
