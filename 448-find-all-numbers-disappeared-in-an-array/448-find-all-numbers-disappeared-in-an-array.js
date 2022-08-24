/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(nums) {
    //find out the range of the array
    //iterate over the nums array
    //check if the number is within the range
    //if not, add it to a new array
  
    const result = [];
    for (let i = 1; i <= nums.length; i++){
        if(!nums.includes(i)){
            result.push(i);
        }
    }
    return result;
};