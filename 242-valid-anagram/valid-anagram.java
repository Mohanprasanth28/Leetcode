class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character,Integer> map = new HashMap<>();
        int len1 = s.length();
        int len2 = t.length();
        if(len1 != len2){
            return false;
        }
        for(char c :s.toCharArray()){
            map.put(c,map.getOrDefault(c,0)+1);
        }
        int vaild =1;
        for(char c: t.toCharArray()){
            if(! map.containsKey(c) || map.get(c)==0){
                vaild = 0;
                return false;
                
            }
            map.put(c,map.get(c)-1);

        }
        
        return true;
        
    }
}