class Solution {
    public int findLucky(int[] arr) {
        int count_arr[]=new int[501];
        int size=arr.length;
        for(int i=0;i<size;i++){
            count_arr[arr[i]]++;
        }
        int max=0;
        for(int i=1;i<=500;i++){
            if(i==count_arr[i]){
                max=i;
            }
        }
        if(max!=0){
        return max;
            }
        else return -1;
    }
}
