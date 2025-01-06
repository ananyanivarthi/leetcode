class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res=[0]*len(boxes)
        balls,move=0,0
        for i in range(len(boxes)):
            res[i]=balls+move
            move=move+balls
            balls+=int(boxes[i])
        balls,move=0,0
        for i in reversed(range(len(boxes))):
            res[i]+=balls+move
            move=move+balls
            balls+=int(boxes[i])
        return res
