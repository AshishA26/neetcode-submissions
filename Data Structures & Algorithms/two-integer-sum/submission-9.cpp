#include <algorithm>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Unoptimized solution:
        // Searches through the list using 2 indices. The second ind
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i+1; j < nums.size(); j++) {
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
    
