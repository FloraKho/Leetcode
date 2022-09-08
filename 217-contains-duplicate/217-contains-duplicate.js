/**
 * @param {number[]} nums
 * @return {boolean}
 */
// var containsDuplicate = function(nums) {
//     for(let i = 0; i < nums.length; i++){
//         for(let j = 1; j < nums.length; i++){
//             if(nums[i] === nums[j]){
//                 return true;
//             }
//         }
//     }
//     return false;
// };

var containsDuplicate = function(nums) {
    nums.sort()
    for(let i = 0; i < nums.length - 1; i++){
        if(nums[i] === nums[i + 1]) return true;
    }
    return false;
}

