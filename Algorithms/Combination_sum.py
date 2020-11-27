# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 15:06:52 2020

@author: popeg
"""

class Solution:

    def combinationSum(self, candidates, target):
        candidates.sort()
        combinations=[]
        self.DFS(candidates,target,0,combinations,[])
        return combinations
 
    def DFS(self,candidates,target,start,combinations,intermedia):
        if target == 0:
            combinations.append(intermedia)
            return
        
        for i in range(start,len(candidates)):
            if target < candidates[i]:
                return
            
            self.DFS(candidates,target-candidates[i],i,combinations,intermedia+[candidates[i]])
 
    
 
test=Solution()
print(test.combinationSum([1,2,3,4],4))