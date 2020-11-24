int getDecimalValue(struct ListNode* head){
    int data[31],i=0; 
    struct ListNode *temp;
    temp=head;
    while(temp!=NULL){
        data[i]=temp->val;
        temp=temp->next;
        i++;
    }
    int decimal=0,num=0;
    for(int ind=i-1;ind>=0;ind--){
        decimal+=data[ind]*pow(2,num);
        num++;
    }
    return decimal;
}
