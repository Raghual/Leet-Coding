class Solution {
    public int getMaximumGenerated(int n) {
        if(n==1){
            return 1;
        }
        if(n==0)return 0;
        int arr[]=new int[n+1];
        arr[0]=0;
        arr[1]=1;
        for(int i=1;i<(n/2)+1;i++){
            if(2*i >=2 && 2*i<=n){
                arr[2*i]=arr[i];
            }
            if((2*i)+1 >=2 && (2*i)+1<=n){
                arr[(2*i)+1]=arr[i]+arr[i+1];
            }
        }
        int max=0;
        for(int i=0;i<n+1;i++){
            if(arr[i]>max)max=arr[i];
        }
        return max;
        
        
    }
}
