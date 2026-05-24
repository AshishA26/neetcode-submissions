#include <algorithm>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Unoptimized solution:
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i; j < nums.size(); j++) {
                if (nums[i] + nums[j] == target && i != j) {
                    vector<int> inds = {i, j};
                    sort(inds.begin(), inds.end());
                    return inds;
                }
            }
        }

        // Optimized solution:
        
    }
};
    
