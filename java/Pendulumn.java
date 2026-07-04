import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Deque;

public 
class Pendulumn {
    // Calculates the new order of elements based on pendulum arrangement
    public ArrayList<Integer> thePendulum(ArrayList<Integer> arr) {
        // Your code here
        ArrayList<Integer> ans = new ArrayList<>();
        Collections.sort(arr);
        boolean appendFirst = true;
        int count = 0;
        Deque<Integer> q = new ArrayDeque<>();
        for (int i =0;i<arr.size();i++){
            if (count==2){
                appendFirst = false;
                count=0;
            }
            if (appendFirst){
                q.push(arr.get(i));
                count++;
            }
            else{
                q.add(arr.get(i));
                count++;
                if (count==2){
                    appendFirst = true;
                    count=0;
                }
            }
        }
        ArrayList<Integer> list = new ArrayList<>(q);
        return list;
    }
} {
    
}
