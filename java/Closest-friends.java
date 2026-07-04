import java.util.*;

class ClosestFriends {
        public static ArrayList<Integer> closestFriends(ArrayList<Integer> arr) {
        // code here
        ArrayList<Integer> heights = new ArrayList<>();
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0;i<arr.size();i++){
            while (!stack.isEmpty() && arr.get(stack.peek())>=arr.get(i)){
                stack.pop();
            }
            if (stack.isEmpty()){
                heights.add(i,-1);
            } else{
                heights.add(stack.peek());
            }
            stack.push(i);
        }
        return heights;
    }
} {
    
}
