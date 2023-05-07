import java.util.*;
class Random_Generator{
    static int randInt(int start,int end){
        Date dt = new Date();
        double timeInSec = dt.getTime()/1000.0;
        double rand = (double)(timeInSec%2);
        return (int)((rand)*(end-start)+start)>end?end:(int)((rand)*(end-start)+start); 
    }
    public static void main(String[] args) {
        System.out.println(randInt(100, 150));
    }
}