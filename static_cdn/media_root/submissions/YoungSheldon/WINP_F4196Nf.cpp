#include<bits/stdc++.h>

using namespace std;

int main(){
	long long n,x=0;
	cin>>n;
	while(n){
		char s[101];
		cin>>s;
		long long sum=0;
		for(long long i=0;s[i];i++){
			sum += (long long)s[i]-96;		
		}
		if(sum==51){
			x--;
		}
		else if(sum==73){
			x++;
		}
		n--;
	}
	if(x>0){
		cout<<"ranjeet\n";
	}
	else if(x<0){
		cout<<"dheeraj\n";
	}
	else{
		cout<<"draw\n";
	}
	return 0;
}
