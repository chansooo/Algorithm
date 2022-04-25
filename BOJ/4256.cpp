#include<bits/stdc++.h>

#define f(i,l,r) for(int i=l;i<=r;++i)
using namespace std;

int a[1001], b[1001];

void sol(int i, int l, int r){
	if(l>r) return;
	if(l == r){
		cout << a[i] << ' ';
		return;
	}
	
	int tmp = b[a[i]];
	sol(i+1, l, tmp-1);
	sol(i+tmp-l+1, tmp+1, r);
	cout << a[i] << ' ';
}

int main(){
	int t; cin >> t;
	while(t--){
		int n; cin >> n;
		f(i, 1, n)cin >> a[i];
		f(i, 1, n){
			int tmp; cin >> tmp;
			b[tmp] = i;
		}
		sol(1, 1, n);
		cout << endl;
	}
	
	int dummy;
	cin >> dummy;
	return 0;
}