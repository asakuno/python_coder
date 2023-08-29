from typing import List

h, w = list(map(int, input().split()))
r, c = list(map(int, input().split()))

class Map:
    def check_map(self, h: int, w: int, r: int, c: int):
        if h == 1 and w == 1:
            return 0
        else:
            if r >1 and r <= h:
                top = 1 
            else:
                top = 0
            if c > 1 and c <= w:
                left = 1 
            else:
                left = 0
            if c < w:
                right = 1 
            else:
                right = 0
            if r < h:
                bot = 1
            else:
                bot = 0
            return top + left + right + bot
        
class Answer:
    def computed(self, a: int, b: int, c: int, d: int) -> int:
        map_obj = Map()
        return map_obj.check_map(a, b, c, d)

answer = Answer().computed(h, w, r, c)

print(answer)
