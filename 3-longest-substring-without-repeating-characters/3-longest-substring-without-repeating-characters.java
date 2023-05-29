class Solution {
    public int lengthOfLongestSubstring(String s) {
        int longest = 0;
        for(int i = 0; i < s.length(); i++){
            String curString = "";
            for(int j = i; j < s.length(); j++){
                if(curString.contains("" + s.charAt(j))){
                    break;
                } else {
                    curString += s.charAt(j);
                    if(longest < curString.length()){
                        longest = curString.length();
                    }
                }
            }
        }
        return longest;
    }
}