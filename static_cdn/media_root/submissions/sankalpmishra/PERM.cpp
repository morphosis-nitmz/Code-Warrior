#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,n;
	long int a,b;
	cin>>t;
	while(t--)
	{
		cin>>n>>a>>b;
		long int arr[n];
		for(int i=0;i<n;++i)
		{
			cin>>arr[i];
		}
		long int l=1-b;
		long int r=1+b;
		long int count=0;
		for(int i=0;i<n;++i)
		{
			if(arr[i]<r and arr[i]>l)
			{
				count++;
			}
		}
		if(count<a)
		{
			cout<<"YES"<<'\n';
		}
		else
		{
			cout<<"NO"<<'\n';
		}
	}
	
	return 0;
}
