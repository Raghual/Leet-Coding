class Solution {
    public boolean canFormArray(int[] arr, int[][] pieces) {
        int size=arr.length;
        int size1=pieces.length;
        int new_arr[]=new int[size],ind=0;
        for(int i=0;i<size;i++){
            for(int j=0;j<size1;j++){
                if(arr[i]==pieces[j][0]){
                    int size2=pieces[j].length;
                    for(int k=0;k<size2;k++){
                        new_arr[ind]=pieces[j][k];
                        ind++;
                    }
                }
            }
        }
        int flag=1;
        for(int i=0;i<size;i++){
            if(arr[i]==new_arr[i])flag=1;
            else{
                flag=0;
                break;
            }
        }
        if(flag==1)return true;
        else return false;
    }
}
