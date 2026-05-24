#include <algorithm>
#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Unoptimized solution:
        // Searches through the list using 2 indices. The second indice starts at i+1 
        // and goes to the later numbers only. Time complexity: O(n^2)
        // for (int i = 0; i < nums.size(); i++) {
        //     for (int j = i+1; j < nums.size(); j++) {
        //         if (nums[i] + nums[j] == target) {
        //             vector<int> inds = {i, j};
        //             sort(inds.begin(), inds.end());
        //             return inds;
        //         }
        //     }
        // }

        // Optimized solution: O(n)
        // Use a hashmap to store previous values and calculate the difference
        // between the target and the current num
        std::unordered_map<int, int> prevMap; // val : index
        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];

            // Return the indices of the 2 values if the map contains the difference.
            // No need for sorting because i will always be larger than any index value
            // present in the hashmap
            if (prevMap.contains(diff)) {
                vector<int> inds = {prevMap[diff], i};
                return inds;
            }
            
            // Update hashmap if the map does not contain the difference
            prevMap[nums[i]] = i;
        }
    }
};
    
