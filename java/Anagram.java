import java.util.*;
public class Anagram {
    /*  Function to check if two strings are anagram
     *   s1, s2: input string
     */
    public static boolean areAnagrams(String s1, String s2) {

        // Your code here
        Map<Character,Integer> map = new HashMap<>();
        for(char c: s1.toCharArray()){
            map.put(c,map.getOrDefault(c,0)+1);
        }
        for(char c:s2.toCharArray()){
            if(!map.containsKey(c) || map.get(c)==0){
                return false;
            } else{
                map.put(c,map.get(c)-1);
            }
        }
        return map.values().stream().allMatch(value->value==0);
    }
} {
    
}
