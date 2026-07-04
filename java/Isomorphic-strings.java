import java.util.HashMap;

class Isomorphic {
    // This function returns true if str1 and str2 are ismorphic
    // else returns false
    public static boolean areIsomorphic(String S1, String S2) {
        // Your code here
        
        if (S1.length()!=S2.length()){
            return false;
        }
       HashMap<Character,Character> s1s2 = new HashMap<>();
       HashMap<Character,Character> s2s1 = new HashMap<>();
       
       for(int i=0;i<S1.length();i++){
           char c1 = S1.charAt(i);
           char c2 = S2.charAt(i);
           if (s1s2.containsKey(c1)){
               if (s1s2.get(c1)!=c2){
                   return false;
               }
           }
           else{
               if(s2s1.containsKey(c2)){
                   return false;
               }
           }
           
           s1s2.put(c1,c2);
           s2s1.put(c2,c1);
       }
       return true;
       
       
        
    }
}