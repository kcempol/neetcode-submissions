class Solution {
    public int climbStairs(int n) {
        ArrayList<Integer> num = new ArrayList<>();
        num.add(1);
        num.add(2);
        int count = 2;
        while(n >= num.size()){
            int sum = num.get(count - 1) + num.get(count - 2);
            num.add(count, sum);
            count++;
        }
        return num.get(n-1);
        

     }
}
