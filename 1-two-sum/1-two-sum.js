/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let numHash = {}
    
    for(let i = 0; i < nums.length; i++){
        let potentialMatch = target - nums[i]
        
        if(potentialMatch in numHash) return [i, numHash[potentialMatch]]
        numHash[nums[i]] = i
    }
    return []
};