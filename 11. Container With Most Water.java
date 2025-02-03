class Solution {
    public int maxArea(int[] height) {
        int leftPointer = 0;
        int rightPointer = height.length - 1;
        int currentSize = size(leftPointer, rightPointer, height);
        while (leftPointer != rightPointer){
            if (height[leftPointer] >= height[rightPointer]){
                int newSize = size(leftPointer,--rightPointer,height);
                if (newSize >= currentSize){
                    currentSize = newSize;
                }
            } else {
                int newSize = size(++leftPointer,rightPointer,height);
                if (newSize >= currentSize){
                    currentSize = newSize;
                }
            }
        }

        return currentSize;
    }

    public int size(int l, int r, int[]array){
        int left = array[l];
        int right = array[r];
        if (right >= left){
            return left * (r-l);
        } else {
            return right * (r-l);
        }
    }
}