    def intersection(s1, s2):
        return [max(s1[0], s2[0]), min(s1[1], s2[1])]

    def is_intersection(s):
        return s[0] <= s[1]



class Solution:

    def intervalIntersection(self, firstList, secondList):

        i = 0
        j = 0

        answer = []
        while i < len(firstList) and j < len(secondList):

            inter = intersection(firstList[i], secondList[j])
            if is_intersection(inter):
                answer.append(inter)

            if firstList[i][1] < secondList[j][1]:
                i += 1
            elif firstList[i][1] > secondList[j][1]:
                j += 1
            else:
                i += 1
                j += 1

        return answer
