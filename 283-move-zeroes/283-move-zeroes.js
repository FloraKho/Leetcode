/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    //iterate over the array
    // check if the value is zero
    //if value is zero, remove it from the array and add 0 to the end
    //if value is no zero, continue
    let prev = 0;
    for(let i = 0; i < nums.length; i++){
        if(nums[i] !== 0) {
            let temp = nums[prev];
            nums[prev] = nums[i];
            nums[i] = temp;
            prev++;
        }
    }
 return nums;   
}
  