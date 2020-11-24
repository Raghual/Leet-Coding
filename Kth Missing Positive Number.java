class Solution {
    public int findKthPositive(int[] arr, int k) {
        int size;
        size=arr.length;
        int ind=0,i,count=0;
        for(i=1;count<k;i++){
            if(ind<size){
            if(i!=arr[ind]){
                count++;
            }
            else{
                ind++;
            }
            }
            else{
                count++;
            }
        }
        i--;
        return i;
    }
}
