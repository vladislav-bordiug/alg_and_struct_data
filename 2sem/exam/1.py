from typing import List
class Solution:
    def checkCdata(self, cdata:str) -> bool:
        content = cdata[2:-1]
        return content.find('[CDATA[') == 0
    def checkTag(self, tag: str, tags: List[str]) -> bool:
        if '/' not in tag:
            name = tag[1:-1]
        else:
            name = tag[2:-1]
        if len(name) == 0 or len(name) > 9:
            return False
        for x in name:
            if not x.isupper():
                return False
        if '/' in tag:
            if len(tags)==0:
                return False
            if tags.pop() != tag[:1] + tag[2:]:
                return False
            return True
        tags.append(tag)
        return True
    def isValid(self, code: str) -> bool:
        tags = []
        i = 0
        end = 0
        first_tag = code[:code.find('>')+1]
        last_tag = ''
        while i < len(code):
            ind = 0
            if i == 0 and code[i] != '<':
                return False
            if i == len(code) - 1 and code[i] != '>':
                return False
            if code[i] == '<':
                if code[i+1] =='/':
                    ind = code[i:].find('>')
                    last_tag = code[i:i+ind+1]
                    if ind == -1 or not self.checkTag(code[i:i+ind+1],tags):
                        return False
                    end = i + ind
                elif code[i+1] == '!':
                    ind = code[i:].find(']]>')
                    if ind == -1 or not self.checkCdata(code[i:i+ind+3]):
                        return False
                    ind += 2
                else:
                    ind = code[i:].find('>')
                    if ind == -1 or not self.checkTag(code[i:i+ind+1],tags):
                        return False
            i += ind + 1
        if len(tags) != 0:
            return False
        if end != len(code) - 1:
            return False
        if first_tag != last_tag[:1] + last_tag[2:]:
            return False
        return True
s = Solution()
tag = input('Enter tag\n')
print('Result:', s.isValid(tag))
