class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        vs1 = version1.split(".")
        vs2 = version2.split(".")

        m = len(vs1)
        n = len(vs2)

        for i in range(max(m,n)):
            v1 = int(vs1[i]) if i<m else 0
            v2 = int(vs2[i]) if i<n else 0

            if v1<v2:
                return -1
            if v1>v2:
                return 1
        return 0
        