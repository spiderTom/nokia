class Solution
{
public:
double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2)
{
    int a[1010],b[1010];
    m=nums1.size();
    for (int i=0;i<m;i++)
        a[i]=nums1[i];
    n=nums2.size();
    for (int i=0;i<n;i++)
        b[i]=nums2[i];
    if ((n+m)%2==1)
        return find(a,m,b,n,(n+m)/2+1);
    else
        return (find(a,m,b,n,(n+m)/2)+find(a,m,b,n,(n+m)/2+1))/2;
}
private:
int n,m;
double find(int a[],int m,int b[],int n,int k)
{
    if (m>n)
        return find(b,n,a,m,k);
    if (m==0)
        return b[k-1];
    if (k==1)
        return min(a[0],b[0]);
    int pa=min(k/2,m),pb=k-pa;
    if (a[pa-1]<b[pb-1])
        return find(a+pa,m-pa,b,n,k-pa);
    else if (a[pa-1]>b[pb-1])
        return find(a,m,b+pb,n-pb,k-pb);
    else
        return a[pa-1];
}

};