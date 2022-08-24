/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    while (ransomNote.length > 0){
        const nextLetter = ransomNote.substring(0, 1);
        const indexInMagazine = magazine.indexOf(nextLetter);
        
        if(indexInMagazine > -1) {
            magazine = magazine.substring(0, indexInMagazine) + magazine.substring(indexInMagazine + 1);
        } else {
            return false;
        }
        ransomNote = ransomNote.substring(1);
    }
    return true;
};