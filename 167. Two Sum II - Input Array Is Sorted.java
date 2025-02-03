class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] answer = new int[2];
        int l = 0;
        int r = numbers.length-1;
        while (true) {
            int leftPointer = numbers[l];
            int rightPointer = numbers[r];
            if (leftPointer + rightPointer == target){
                answer[0] = l+1;
                answer[1] = r+1;
                return answer;
            } else if (leftPointer + rightPointer < target){
                l++;
            } else if (leftPointer + rightPointer > target){
                r--;
            }
            
        }
    }
}